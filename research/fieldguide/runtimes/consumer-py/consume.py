#!/usr/bin/env python3
"""Second-language consumer for the arworld meet-overlay conformance pack.

Run:  python3 consume.py        (Python 3 stdlib only — no pip, no venv)

This shares ZERO code with the JavaScript model. It re-implements the Promise
layer from the counter-spec's prose and re-derives every projection digest in
../fixtures/vectors.json. If it agrees byte-for-byte, that is the difference
between "we wrote a spec" and "two strangers can agree" — and it is the check
the ONODE C# implementation should be held to as well.

It exists mainly because of one line, marked TRAP below.
"""

import hashlib
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VECTORS = os.path.join(HERE, "..", "fixtures", "vectors.json")

CANON_DOMAIN = "arworld/canonical/v0"

AUDIENCES = ["private", "public", "link", "acquaintance"]

PUBLIC_FIELDS = ["poiId", "title", "placeKind", "lat", "lon", "markerStyle"]
LINK_FIELDS = PUBLIC_FIELDS + ["wikiSlug", "rite", "trail", "witnessedUtc"]
ACQUAINTANCE_FIELDS = LINK_FIELDS + ["note"]

ALLOW = {
    "private": [],
    "public": PUBLIC_FIELDS,
    "link": LINK_FIELDS,
    "acquaintance": ACQUAINTANCE_FIELDS,
}


def rank(a):
    return AUDIENCES.index(a)


# --- TRAP -------------------------------------------------------------------
# The public tier coarsens geo to ~100 m. The obvious Python for that is
# `round(x * 1000) / 1000` — and it is WRONG, silently, for exactly the inputs
# nobody tests.
#
#   JavaScript  Math.round(51534.5)  ->  51535   (half-up, toward +infinity)
#   Python      round(51534.5)       ->  51534   (half-to-EVEN, banker's)
#   C#          Math.Round(51534.5)  ->  51534   (half-to-even by default too)
#
# So a JS server and a Python or C# server place the same pin ~110 m apart, on
# opposite sides of a street, and both pass their own unit tests. The rule has
# to name its rounding mode or it is not a rule.
#
# The spec says half-up, which is `floor(x + 0.5)` in every language.
# `pj-halfway` in the vector pack exercises it on both axes.
def coarse(n):
    return math.floor(n * 1000 + 0.5) / 1000


def policy_for(holon):
    if holon.get("disclosure"):
        return holon["disclosure"]
    if holon.get("source") == "quest":
        return {"maxAudience": "link"}
    return {"maxAudience": "acquaintance"}


def project(holon, audience):
    policy = policy_for(holon)
    ceiling = policy.get("maxAudience", "acquaintance")
    capped = ceiling if rank(audience) > rank(ceiling) else audience
    if capped == "private" or rank(capped) < 1:
        return None

    deny = policy.get("deny") or []
    out = {}
    for f in ALLOW[capped]:
        if f in deny:
            continue
        if holon.get(f) is not None:
            out[f] = holon[f]
    if capped == "public":
        if "lat" in out:
            out["lat"] = coarse(out["lat"])
        if "lon" in out:
            out["lon"] = coarse(out["lon"])
    out["origin"] = "trust"
    out["audience"] = capped
    return out


def enc(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return "%.6f" % v
    return str(v)


def canonical(obj):
    lines = [CANON_DOMAIN]
    for k in sorted(obj.keys()):
        v = obj[k]
        if v is None:
            continue
        lines.append("%s=%s" % (k, enc(v)))
    return "\n".join(lines)


def digest(obj):
    return hashlib.sha256(canonical(obj).encode("utf-8")).hexdigest()


def main():
    with open(VECTORS, "r", encoding="utf-8") as fh:
        pack = json.load(fh)

    checked = 0
    failures = []

    for vec in pack["projections"]:
        mine = project(vec["holon"], vec["audience"])
        want = vec["expect"]

        if not want["projected"]:
            checked += 1
            if mine is not None:
                failures.append("%s: expected no projection, produced one" % vec["id"])
            continue

        checked += 1
        if mine is None:
            failures.append("%s: expected a projection, produced none" % vec["id"])
            continue

        if sorted(mine.keys()) != want["fields"]:
            failures.append(
                "%s: field set differs\n    mine: %s\n    pack: %s"
                % (vec["id"], sorted(mine.keys()), want["fields"])
            )
            continue

        if canonical(mine) != want["canonical"]:
            mine_lines = canonical(mine).split("\n")
            pack_lines = want["canonical"].split("\n")
            diff = [
                "      %s | %s" % (a, b)
                for a, b in zip(mine_lines, pack_lines)
                if a != b
            ]
            failures.append(
                "%s: canonical preimage differs\n%s" % (vec["id"], "\n".join(diff))
            )
            continue

        if digest(mine) != want["digest"]:
            failures.append("%s: digest differs" % vec["id"])

    green = "\033[32m"
    red = "\033[31m"
    off = "\033[0m"

    print("\nsecond-language consumer — %d projection vectors\n" % checked)
    for vec in pack["projections"]:
        ok = not any(f.startswith(vec["id"] + ":") for f in failures)
        tag = green + "PASS" + off if ok else red + "FAIL" + off
        print("  %s %s" % (tag, vec["id"]))

    if failures:
        print("\n" + red + "mismatches:" + off)
        for f in failures:
            print("  " + f)
        print("\n  %d/%d agreed\n" % (checked - len(failures), checked))
        return 1

    print("\n  %d/%d digests byte-exact against the JavaScript model\n" % (checked, checked))
    return 0


if __name__ == "__main__":
    sys.exit(main())
