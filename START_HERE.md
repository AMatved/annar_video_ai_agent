# 🚀 Complete Backend Deployment Guide

Your Video Creator Agent is ready for full functionality! Follow these steps to deploy the backend.

---

## 📋 What's Already Done ✅

- ✅ Python backend created (`api/server.py`)
- ✅ Railway deployment config ready
- ✅ Frontend integration code ready
- ✅ All code pushed to GitHub
- ✅ Documentation created

---

## 🎯 Your Action Plan (3 Steps)

### Step 1: Deploy Backend to Railway (5 minutes)

#### 1.1 Open Railway
- Go to: https://railway.app
- Login with GitHub

#### 1.2 Create New Project
- Click **"+ New Project"**
- Select **"Deploy from GitHub repo"**

#### 1.3 Configure
- **Repository:** `THU-SIGS-AIID/annar_video_ai_agent`
- **Root Directory:** `api`
- Click **"Deploy"**

#### 1.4 Add Environment Variables
After deploy starts:
1. Go to **Variables** tab
2. Add these variables:

```
OPENAI_API_KEY=sk-your-key-here
OPENAI_BASE_URL=https://api.stepfun.com/v1
OPENAI_MODEL=step-3.5-flash
PORT=8000
```

#### 1.5 Wait for Deployment
- Takes ~2-3 minutes
- Watch logs: `✅ Ready to process requests!`

#### 1.6 Copy Your API URL
Find URL like:
```
https://video-creator-backend-xxxx.up.railway.app
```

---

### Step 2: Connect Frontend to Backend (2 minutes)

#### 2.1 Open Vercel Dashboard
- Go to: https://vercel.com/dashboard
- Find `web-app` project
- Click on it

#### 2.2 Add Environment Variable
1. Go to **Settings** → **Environment Variables**
2. Click **"Add New"**
3. Add:
   - **Name:** `BACKEND_URL`
   - **Value:** `https://your-backend.up.railway.app`
   - **Environments:** All (Production, Preview, Development)
4. Click **"Save"**

#### 2.3 Redeploy Frontend
1. Go to **Deployments** tab
2. Click **"Redeploy"** on latest deployment
3. Wait ~2 minutes

---

### Step 3: Test Integration (1 minute)

#### 3.1 Open Your Site
```
https://web-app-ten-woad-69.vercel.app
```

#### 3.2 Test Real AI
Type in chat:
```
Create 5 viral TikTok titles about fitness
```

Should get real AI response! 🎉

---

## 📚 Detailed Documentation

| Document | Description | Link |
|----------|-------------|------|
| **Railway Deploy** | Complete Railway guide | [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md:1) |
| **Backend Setup** | Connect frontend to backend | [web-app/BACKEND_SETUP.md](web-app/BACKEND_SETUP.md:1) |
| **API README** | Backend API documentation | [api/README.md](api/README.md:1) |
| **User Guide** | How to use the app | [web-app/USER_GUIDE.md](web-app/USER_GUIDE.md:1) |

---

## ✅ Verification Checklist

After deployment, verify:

### Backend (Railway)
- [ ] Service is "Running" (not crashed)
- [ ] Health check works: `https://your-backend.up.railway.app/health`
- [ ] Logs show: `✅ Ready to process requests!`
- [ ] `agent_available: true` in health response

### Frontend (Vercel)
- [ ] `BACKEND_URL` is set in environment variables
- [ ] Site loads without errors
- [ ] No React errors in browser console
- [ ] Chat history works

### Integration
- [ ] Chat responds with real AI (not mock)
- [ ] Task creation from chat works
- [ ] All agent functions work
- [ ] No CORS errors

---

## 🆘 Troubleshooting

### Backend Won't Start

**Problem:** Railway service crashes

**Check:**
1. Logs show error?
2. `OPENAI_API_KEY` is set?
3. Agent.py exists in repo?

**Fix:**
```bash
# Check Railway logs
# Verify environment variables
# Redeploy from Railway dashboard
```

### Frontend Can't Connect

**Problem:** CORS or connection errors

**Check:**
1. Backend URL is correct?
2. Backend is running?
3. `BACKEND_URL` set in Vercel?

**Fix:**
```bash
# Test backend directly:
curl https://your-backend.up.railway.app/health

# Check Vercel logs for errors
```

### Still Not Working?

**Check:**
1. Browser console (F12) for errors
2. Railway logs
3. Vercel logs
4. Network tab in browser DevTools

**Common Issues:**
- Wrong API key format
- Missing environment variable
- Backend URL has typo
- CORS not configured

---

## 💰 Pricing

### Railway (Free Tier)
- ✅ $5 free credit monthly
- ✅ 512MB RAM
- ✅ 512 hours runtime
- ✅ Perfect for this project!

### Vercel (Hobby Plan)
- ✅ Free forever
- ✅ Unlimited projects
- ✅ Automatic HTTPS
- ✅ Global CDN

**Total Cost:** $0/month! 🎉

---

## 🎯 Next Steps (Optional)

After basic deployment works:

### 1. Custom Domain
- Buy domain (~$10/year)
- Add to Vercel: Settings → Domains
- Add to Railway: Settings → Custom Domains

### 2. Monitoring
- Railway: Metrics tab
- Vercel: Analytics tab
- Set up uptime monitoring

### 3. Backup
- Auto-deploys on push
- GitHub keeps history
- Railway has snapshots

### 4. Enhancements
- Add authentication
- Rate limiting
- Database for persistent storage
- Admin panel

---

## 📞 Support Links

**Documentation:**
- Railway: https://docs.railway.app
- Vercel: https://vercel.com/docs
- GitHub: https://github.com/THU-SIGS-AIID/annar_video_ai_agent

**Your Services:**
- Railway Dashboard: https://railway.app/dashboard
- Vercel Dashboard: https://vercel.com/dashboard

---

## 🎉 You're Ready!

Everything is set up and ready for deployment!

**Quick Recap:**

1. ✅ Code is ready on GitHub
2. ⏳ You need to deploy to Railway (5 min)
3. ⏳ You need to connect frontend (2 min)
4. 🎉 Full AI agent will work!

**Let's do it!** 🚀

---

**When ready, start with Step 1 in the "Action Plan" above.**

Good luck! You've got this! 💪
