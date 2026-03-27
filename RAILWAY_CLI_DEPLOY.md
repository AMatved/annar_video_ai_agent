# 🚀 Railway CLI Deployment (No GitHub Required!)

Deploy your backend directly to Railway using CLI - no GitHub needed!

## 🎯 Why This Method?

✅ **No GitHub required**
✅ **Deploy directly from your computer**
✅ **Super fast once set up**
✅ **Auto-redeploys with command**
✅ **100% FREE** (with Railway's free credit)

---

## 📋 Prerequisites

- Railway account (free)
- Railway CLI installed
- Your OpenAI API key
- Files in `api/` folder ready

---

## 🚀 Step-by-Step Guide

### Step 1: Install Railway CLI (2 min)

#### Windows:
```bash
# Using npm (recommended)
npm install -g @railway/cli

# Or download binary
# https://github.com/railwayapp/cli/releases
```

#### Verify installation:
```bash
railway --version
```

Should show version number.

---

### Step 2: Login to Railway (1 min)

```bash
railway login
```

This will open your browser for authentication.

---

### Step 3: Initialize Project (1 min)

In project root (`c:\Users\User\video_creator_agent`):

```bash
railway init
```

Railway will ask questions:
- **Project name:** `video-creator-backend`
- **Choose project:** Create new project
- **Choose region:** Closest to you (or default)

---

### Step 4: Create Service (2 min)

```bash
railway add
```

Railway will ask:
- **What service?** → Select "backend" or just press Enter
- **Project:** Select `video-creator-backend`
- **Service name:** `video-creator-api`
- **Runtime:** Python 3
- **Root directory:** `api`
- **Build command:** `pip install -r requirements.txt`
- **Start command:** `uvicorn server:app --host 0.0.0.0 --port $PORT`

---

### Step 5: Add Environment Variables (2 min)

#### Option A: Via CLI
```bash
railway variables set OPENAI_API_KEY="sk-your-key-here"
railway variables set OPENAI_BASE_URL="https://api.stepfun.com/v1"
railway variables set OPENAI_MODEL="step-3.5-flash"
railway variables set PORT="8000"
```

#### Option B: Via Dashboard (easier)
1. Go to: https://railway.app/dashboard
2. Find your project
3. Click on service
4. Go to "Variables" tab
5. Add variables manually

---

### Step 6: Deploy! (1 min)

```bash
railway up
```

This will:
- Upload files from your computer
- Install dependencies
- Start the server
- Give you a URL

**Success message:**
```
🚀 Video Creator AI API starting...
📊 Agent Available: True
✅ Ready to process requests!
```

### Step 7: Get Your URL

Railway will show:
```
https://your-service-name.up.railway.app
```

Or check dashboard:
- https://railway.app/dashboard
- Your project → service → URL

---

## 🔗 Connect to Vercel (2 min)

1. Open: https://vercel.com/dashboard
2. Find `web-app` project
3. Settings → Environment Variables
4. Add:
   - **Name:** `BACKEND_URL`
   - **Value:** `https://your-service.up.railway.app`
   - **Environments:** All
5. Save
6. Deployments → Redeploy

---

## 🧪 Test Integration

Open: https://web-app-ten-woad-69.vercel.app

Type:
```
Create 5 viral TikTok titles about fitness
```

**Real AI should respond!** 🎉

---

## 🔄 Update Later

After making code changes:

```bash
railway up
```

Railway will:
- Upload new files
- Rebuild
- Restart service
- Keep same URL

---

## 📊 Commands Reference

```bash
# Login
railway login

# Init project
railway init

# Add service
railway add

# Deploy/upload
railway up

# View logs
railway logs

# Open dashboard
railway open

# List services
railway list

# Set variables
railway variables set KEY=VALUE

# Get status
railway status
```

---

## 🆘 Troubleshooting

### "railway: command not found"

**Solution:**
```bash
# Install via npm
npm install -g @railway/cli

# Or add to PATH
# Railway installation folder should be in npm global bin
```

### Login fails

**Solution:**
```bash
# Try alternative
railway login --browserless

# Or login in browser first
# https://railway.app/dashboard
```

### Variables not working

**Solution:**
- Use dashboard instead: https://railway.app/dashboard
- Your service → Variables tab
- Add manually

### Deploy fails

**Solution:**
- Check you're in project root
- Verify `api/` folder exists
- Check `requirements.txt` format
- View logs: `railway logs`

---

## 💡 Tips

### 1. Save Your Token

After first login, Railway saves a token. No need to login again!

### 2. Use Dashboard for Variables

CLI is great, but dashboard is easier for variables:
- https://railway.app/dashboard
- Your project → service → Variables

### 3. Monitor in Dashboard

Dashboard shows:
- Logs
- Metrics
- Resource usage
- Deploys

---

## 📝 File Structure Check

Before deploying, verify you have:

```
video_creator_agent/
├── api/
│   ├── server.py          ✅ Required
│   ├── requirements.txt   ✅ Required
│   └── .env.example       (for reference)
├── agent.py               ✅ Required
├── platform_integrations.py
├── requirements.txt
└── ... other files
```

---

## 🎯 Quick Start Summary

```bash
# 1. Install CLI
npm install -g @railway/cli

# 2. Login
railway login

# 3. Init
railway init

# 4. Add service
railway add

# 5. Set variables
railway variables set OPENAI_API_KEY="sk-your-key"
railway variables set OPENAI_BASE_URL="https://api.stepfun.com/v1"
railway variables set OPENAI_MODEL="step-3.5-flash"

# 6. Deploy
railway up
```

That's it! Your backend is live! 🚀

---

## 💰 Cost

Railway gives **$5 free credit** when you sign up:
- ~500 hours of runtime
- ~1 month of normal usage
- **No credit card required!**

---

## 📞 Support

- **Railway Docs:** https://docs.railway.app
- **Railway CLI:** https://github.com/railwayapp/cli
- **Your Dashboard:** https://railway.app/dashboard

---

**Ready to deploy?** Start with Step 1! 🚀

I'll help if you get stuck at any step!
