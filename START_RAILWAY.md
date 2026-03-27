# 🚀 Railway CLI Quick Start

Deploy backend via CLI without GitHub - EASIEST METHOD!

## ⚡ Quick Start (Windows)

### Option 1: Automated Script
```bash
deploy_railway.bat
```

Just double-click the file and follow prompts!

---

### Option 2: Manual Steps

### 1. Install Railway CLI
```bash
npm install -g @railway/cli
```

### 2. Login
```bash
railway login
```
(Browser opens, login with GitHub)

### 3. Deploy
```bash
railway init
railway add
```

When asked:
- **Root Directory:** `api`
- **Runtime:** Python 3
- **Build:** `pip install -r requirements.txt`
- **Start:** `uvicorn server:app --host 0.0.0.0 --port $PORT`

### 4. Set API Key
```bash
railway variables set OPENAI_API_KEY="sk-your-key-here"
```

Or use dashboard: https://railway.app/dashboard → Your Service → Variables

### 5. Deploy!
```bash
railway up
```

### 6. Connect Frontend

Go to Vercel dashboard → web-app → Settings → Environment Variables

Add:
- **Name:** `BACKEND_URL`
- **Value:** (your Railway URL from dashboard)

**Done!** 🎉

---

## 📋 Full Guide

See: [RAILWAY_CLI_DEPLOY.md](RAILWAY_CLI_DEPLOY.md:1)

---

## 🆘 Problems?

### "npm not found"
- Install Node.js from: https://nodejs.org
- Or download Railway CLI directly

### "railway command not found"
- Restart terminal
- Or close/open terminal

### Login fails
- Try: `railway login --browserless`
- Or use dashboard directly

### Variables not setting
- Use dashboard instead: https://railway.app/dashboard
- Your service → Variables tab → Add manually

---

**Ready?** Start with installing Railway CLI! 🚀
