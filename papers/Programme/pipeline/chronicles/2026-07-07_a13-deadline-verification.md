---
date: 2026-07-07
role: A13
wps: [WP-02, WP-04, WP-07, WP-08, WP-09, WP-11, WP-14, WP-15, WP-16, WP-19, WP-21, WP-22]
extractions: []
register_head: C96
ledger_entries: []
---

# Chronicle · A13 deadline verification · 2026-07-07

## Verdict

`programme/deadlines.md` is fully verified. Zero assume rows remain. Every dated row carries a source URL fetched this session and a verified-on date; every venue with no published call carries an explicit "not published" statement and a next-check date. Three findings contradict standing programme assumptions and are proposed as ledger entries below: BGIN Block 15 is 15-16 October 2026 (not December), CPP 2027's deadline precedes the planned WP-16 start, and First Monday is closed to submissions.

## What was verified, and how

All sixteen venues named on the task card were checked against the venue's own site (WebFetch), with web search used only to locate pages, never as a source of record. Key results:

- **PoPETs 2027** (petsymposium.org/cfp27.php): four issues. Issue 1 closed 2026-05-31; Issue 2 submits 2026-08-31; Issue 3 submits 2026-11-30 (notification 2027-02-01); Issue 4 submits 2027-02-28. Format from authors.php: 12 pages excluding bibliography and marked appendices, acmart `[sigconf,balance=false]`. The prior working assumption (2026-11-30) is confirmed as Issue 3.
- **IEEE SaTML 2027** (satml.org): papers 2026-09-29 AoE, notification 2026-12-16, conference early May 2027 in Reykjavik. Page limits did not render on the CFP fetch; flagged for capture before scaffolding.
- **FC 2027** (ifca.ai/fc27/): papers 2026-09-17 AoE, notification 2026-11-05, workshop proposals 2026-09-01, conference 2027-02-08/12 in Barbados (venue tentative).
- **CPP 2027** (popl27.sigplan.org/home/CPP-2027): abstracts 2026-09-03, papers 2026-09-10, strict. 12 pages, acmart sigplan. Conference 2027-01-11/12, Mexico City.
- **BGIN Block 15** (bgin-global.org/events): 2026-10-15/16, Washington D.C.
- **Metagov seminar** (metagov.org): weekly, Wednesdays 16:00-17:00 UTC; talks proposed via the community Slack.
- **Internet Policy Review** (policyreview.info/authors): rolling year-round; 6,000 words initial, 8,000 maximum; roughly six months to publication.
- **Journal of Information Policy** (psupress.org submission guidelines): continuous submissions via Editorial Manager; initial decision within five business days.
- **IACR ePrint** (eprint.iacr.org/submit, operations.html): rolling; any author may submit; minimal scope review; no endorsement system; a revision password is issued on acceptance. No account barrier of consequence.
- **No published call** (explicit, with next-check dates): HotPETs 2027 (page 404; check 2027-02-01), SOUPS 2027 (check 2026-11-01), WEIS 2027 (check 2026-11-01), ITP 2027 (check 2026-10-01), RWOT next (check 2026-09-01), MyData next (check 2026-09-01), ZKProof 9 (check 2026-10-01).
- **First Monday**: the OJS submissions page states the journal is not accepting submissions at this time. Recorded as closed, next check 2026-10-01.

## Reversals and corrections

1. **BGIN Block 15 date reversed.** The prior row carried "Dec 2026, co-chair knowledge". The published events page states 15-16 October 2026, Washington D.C. The published source supersedes the carried date in my file; the discrepancy is escalated, not resolved, for the programme document (Part D references "block 15 review Dec 2026"). This pulls the WP-09 BGIN cut roughly six weeks earlier than the Sep-Nov 2026 plan assumed.
2. **First Monday assumption reversed.** Part E treats First Monday as a rolling fallback for the framework paper. It is presently closed to submissions. The fallback is unavailable until further notice.
3. **WP-16 venue timing contradiction found.** WP-16 plans "begin Q4 2026; CPP/ITP 2027-28", but CPP 2027 submissions close 2026-09-10, before Q4 2026 begins. The realistic targets are ITP 2027 (unannounced) or CPP 2028. Not a defect in the work, a defect in the calendar.
4. **RWOT is dormant.** No event since 2023; RWOT13 (October 2024) was cancelled; the "next event" link on weboftrust.info points to rebootthehague.com, which did not resolve (DNS failure this session). WP-19's premise (a next RWOT event) currently has no date and a dead pointer.

## Dead ends

- usenix.org returns 403 to non-browser fetches; SOUPS 2027 status was established via soups.page instead.
- A first search result attributed "Washington D.C., October 15" to Block 13 (2025); resolved by fetching bgin-global.org/events directly, which lists Block 15 as 2026-10-15/16.
- metagov.org/seminars is 404; the seminar description lives on the front page.

## Proposed ledger entries (for A0 to serialise; none appended by me)

- **P1 (correction):** BGIN Block 15 is 2026-10-15/16 in Washington D.C. per bgin-global.org/events, not December 2026 as carried in Part D/E and the prior deadlines row. WP-09 sequencing tightens by ~6 weeks. Verified 2026-07-07.
- **P2 (venue risk):** First Monday is not accepting submissions (firstmonday.org OJS submissions page, 2026-07-07). Part E's framework-paper fallback is unavailable; recheck 2026-10-01.
- **P3 (calendar conflict):** CPP 2027 deadline (2026-09-10) precedes WP-16's planned Q4 2026 start; WP-16 should be re-aimed at ITP 2027 (deadline unannounced, check 2026-10-01) or CPP 2028.
- **P4-candidate note for A0, not the gate:** RWOT has no scheduled event and its next-event link is dead; WP-19 has no calendar anchor. Recheck 2026-09-01.

## Handoff

- **Open questions:** SaTML 2027 and FC 2027 page limits and templates not yet captured; capture before the scaffold card consumes those rows. Whether MyData's 2026 governance meetings signal a changed conference cadence is unknown.
- **Blocked:** nothing blocked; all next-check dates are in the table.
- **Next actions per WP touched:** WP-07/08: plan against PoPETs Issue 3 (2026-11-30), with Issue 2 (2026-08-31) and SaTML (2026-09-29) as stretch alternatives. WP-04: FC workshop proposals close 2026-09-01; watch for FC27 workshop CFPs from October. WP-09: re-sequence against 2026-10-15. WP-14: recheck WEIS CFP 2026-11-01. WP-16: A0 decision on CPP 2028 vs ITP 2027. WP-19/15/21/22: hold; next-check dates set.
