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
- Index page with all 8 documents
- Click any document to read it
- Full markdown rendering with syntax highlighting
- Clean, readable layout

## 📚 Documents Available

1. **README** - Overview and quick summary
2. **Whitepaper v4.3** - Technical architecture
3. **Research Paper v3.2** - Mathematical foundations
4. **Spellbook v4.0.1** - Narrative framework
5. **Tokenomics v2.0** - Economic architecture
6. **Visual Guide v1.1** - Diagrams & flows
7. **Research Proposal v1.1** - Collaboration invitation
8. **Glossary v2.0** - Canonical terminology

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

