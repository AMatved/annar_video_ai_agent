# 🚀 Quick Deployment Script

Quick guide to deploy your backend with minimal effort.

## Step 1: Deploy to Railway (5 min) ⚡

### 1.1 Login
- Go to: https://railway.app
- Click "Login with GitHub"
- Authorize Railway

### 1.2 Create Project
- Click "+ New Project" button
- Click "Deploy from GitHub repo"
- Select: `THU-SIGS-AIID/annar_video_ai_agent`
- Set "Root Directory" to: `api`
- Click "Deploy"

### 1.3 Get API Key
- You need your OpenAI API key
- If you don't have one, use your existing key or get one

### 1.4 Add Environment Variables
When deploy starts:
1. Click on the "Variables" tab
2. Click "New Variable"
3. Add 4 variables:

```
OPENAI_API_KEY=sk-your-actual-key-here
OPENAI_BASE_URL=https://api.stepfun.com/v1
OPENAI_MODEL=step-3.5-flash
PORT=8000
```

### 1.5 Wait & Get URL
- Wait 2-3 minutes
- Copy URL like: `https://xxx.up.railway.app`

---

## Step 2: Connect to Vercel (2 min) 🔗

### 2.1 Open Vercel
- Go to: https://vercel.com/dashboard
- Find: `web-app` project
- Click it

### 2.2 Add BACKEND_URL
- Go to: Settings → Environment Variables
- Click: "Add New"
- Name: `BACKEND_URL`
- Value: (paste your Railway URL)
- Environments: All
- Click: "Save"

### 2.3 Redeploy
- Go to: Deployments tab
- Click: "Redeploy" button
- Wait 2 minutes

---

## Step 3: Test! (30 sec) ✅

Open: https://web-app-ten-woad-69.vercel.app

Type: `Create 5 viral TikTok titles`

**Should work!** 🎉

---

## Need Help?

I can help with:
- ✅ Troubleshooting errors
- ✅ Explaining steps
- ✅ Creating scripts
- ✅ Answering questions

I cannot:
- ❌ Login to your account
- ❌ Add API keys for you
- ❌ Access your dashboard

**Ready? Let's do it together!** 🚀
