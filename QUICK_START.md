# Quick Start - Documentation Server

## 🚀 Start the Server

**Option 1: Double-click**
- Double-click `run_docs.bat`

**Option 2: Command line**
```bash
python server.py
```

**Option 3: Batch file**
```bash
run_docs.bat
```

## 📖 Access the Docs

Once the server starts, open your browser to:

**http://localhost:7000**

You'll see:
- Index page with all documents
- Click any document to read it
- Full markdown rendering with syntax highlighting
- Clean, readable layout

## 📚 Documents Available

1. **README v1.3** - Overview and quick summary
2. **What Agentprivacy Is** - Mission and orientation
3. **Whitepaper v4.8** - Technical architecture, IEEE 7012 integration
4. **Research Paper v3.6** - Mathematical foundations, standards note
5. **Spellbook v5.0** - Narrative framework, Five Spellbooks
6. **VRC Promise Protocol v3.0** - Economic architecture
7. **Visual Guide v1.3** - Diagrams & flows, IEEE 7012
8. **Glossary v2.3** - Canonical terminology, IEEE 7012 definitions
9. **Research Proposal v1.4** - Collaboration invitation, MyTerms Alliance
10. **IEEE 7012 Quick Reference v1.0** - Machine-readable privacy terms
11. **Promise Theory Reference v1.0** - Formal semantic foundations
12. **Understanding as Key (Zypher) v1** - Conceptual paper
13. **Spellbook Structure Options** - Five Spellbooks organization

## ⏹️ Stop the Server

Press `Ctrl+C` in the terminal window where the server is running.

## 🔧 Troubleshooting

**Port already in use?**
- Another process is using port 7000
- Close other servers or change PORT in server.py

**Can't see the page?**
- Make sure the server is running (check terminal output)
- Try http://127.0.0.1:7000 instead
- Check firewall settings

**Markdown not rendering?**
- Make sure markdown library is installed: `pip install markdown`

