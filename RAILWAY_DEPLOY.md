# 🚀 Railway Deployment Guide

Complete guide to deploy Video Creator AI backend to Railway.

## 📋 Prerequisites

- ✅ GitHub account
- ✅ Railway account (free tier works)
- ✅ API ключи (OpenAI/StepFun)
- ✅ Код запушен на GitHub: https://github.com/THU-SIGS-AIID/annar_video_ai_agent

---

## 🎯 Deployment Steps

### Step 1: Login to Railway

1. **Open:** https://railway.app
2. **Sign up/Login** with your GitHub account
3. **Authorize** Railway to access your repositories

---

### Step 2: Create New Project

1. Click **"+ New Project"** button (top left)
2. Select **"Deploy from GitHub repo"**

---

### Step 3: Select Repository

1. Find and select: **`THU-SIGS-AIID/annar_video_ai_agent`**
2. Railway will analyze the repository

---

### Step 4: Configure Service

**Root Directory:** `api`

**Select Template:** Python (should auto-detect from `requirements.txt`)

**Name:** `video-creator-backend` (or any name you prefer)

Click **"Deploy"**

---

### Step 5: Add Environment Variables

After deployment starts, click on your project → **Variables** tab.

Add these variables:

```bash
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_BASE_URL=https://api.stepfun.com/v1
OPENAI_MODEL=step-3.5-flash
PORT=8000
```

**Important:**
- Click "New Variable" for each
- Replace `sk-your-actual-api-key-here` with your real API key
- Click "Save" after each variable

---

### Step 6: Wait for Deployment

- Railway automatically installs dependencies
- Takes ~2-3 minutes
- Watch the logs in the "Logs" tab

**Success indicator:**
```
🚀 Video Creator AI API starting...
📊 Agent Available: True
✅ Ready to process requests!
```

---

### Step 7: Get Your API URL

After successful deployment:

1. Go to your project dashboard
2. Find your service URL (top of the page)
3. URL will look like: `https://your-project-name.up.railway.app`

**Example:**
```
https://video-creator-backend-production.up.railway.app
```

---

## 🧪 Test Your Backend

### Test Health Endpoint
```bash
curl https://your-project.up.railway.app/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "agent_available": true,
  "version": "1.0.0"
}
```

### Test Chat Endpoint
```bash
curl -X POST https://your-project.up.railway.app/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!"}'
```

---

## 🔧 Configuration

### View Logs

1. Go to your project in Railway
2. Click on your service
3. Click "Logs" tab
4. See real-time logs

### Monitor Resources

1. Project dashboard → "Metrics"
2. See CPU, Memory, Network usage
3. Free tier limits: 512MB RAM, $5 free credit

### Redeploy

**Automatic:**
- Push to `main` branch
- Railway auto-redeploys

**Manual:**
1. Click on your service
2. Click "Restart" button

---

## 🆘 Troubleshooting

### Build Failed

**Problem:** Installation fails

**Solution:**
1. Check `api/requirements.txt` format
2. Verify Python version compatibility
3. Check logs for specific errors

### Service Crashes

**Problem:** Service starts but crashes

**Solution:**
1. Check logs for error
2. Verify `OPENAI_API_KEY` is set correctly
3. Make sure `agent.py` exists in parent directory

### Agent Not Available

**Problem:** `/health` returns `"agent_available": false`

**Solution:**
1. Check that `agent.py` is in project root
2. Verify imports work
3. Check logs for import errors

### Wrong Python Version

**Problem:** "Python version not supported"

**Solution:**
In `api/Procfile` specify version:
```
python-3.10 web: uvicorn server:app --host 0.0.0.0 --port $PORT
```

---

## 💰 Pricing (Railway)

### Free Tier
- $5 free credit monthly
- 512MB RAM
- 512 hours of runtime
- Perfect for development/testing

### Paid Plans
- $5/month - Basic plan
- $10/month - Pro plan
- Pay-as-you-go available

**For this project:** Free tier is sufficient!

---

## 📝 Next Steps

After backend is deployed:

1. ✅ Copy your Railway API URL
2. ✅ Add `BACKEND_URL` to Vercel environment variables
3. ✅ Redeploy frontend
4. ✅ Test full integration

---

## 🔗 Useful Links

- Railway Dashboard: https://railway.app/dashboard
- Your Project: https://railway.app/project/YOUR_PROJECT_ID
- API Docs: https://your-project.up.railway.app/docs
- Repository: https://github.com/THU-SIGS-AIID/annar_video_ai_agent

---

**Ready to deploy?** Let's go! 🚀

**Your Railway API URL will be something like:**
```
https://video-creator-backend-xxxx.up.railway.app
```
