# 🔗 Connect Frontend to Backend

Complete guide to connect web frontend to Railway backend.

## 📋 What You Need

1. ✅ Backend deployed on Railway
2. ✅ Railway API URL (like `https://your-backend.up.railway.app`)
3. ✅ Vercel account

---

## 🎯 Step-by-Step Guide

### Step 1: Get Your Railway URL

1. Go to https://railway.app/dashboard
2. Find your `video-creator-backend` project
3. Copy your service URL

**Example:**
```
https://video-creator-backend-production.up.railway.app
```

### Step 2: Open Vercel Dashboard

1. Go to https://vercel.com/dashboard
2. Find `web-app` project
3. Click on it

### Step 3: Add Environment Variable

1. Go to **Settings** tab
2. Click **Environment Variables**
3. Click **"Add New"** button

Add this variable:

**Name:** `BACKEND_URL`

**Value:** `https://your-backend.up.railway.app`

**Environment:** All (Production, Preview, Development)

4. Click **"Save"**

### Step 4: Redeploy Frontend

1. Go to **Deployments** tab
2. Click **"Redeploy"** (latest production deployment)
3. Wait ~2 minutes

### Step 5: Test Integration

1. Open your site: https://web-app-ten-woad-69.vercel.app
2. In chat, type: `Hello!`
3. Should get real AI response!

---

## 🔧 Alternative: Using Vercel CLI

```bash
# Add environment variable via CLI
vercel env add BACKEND_URL https://your-backend.up.railway.app

# Redeploy
vercel --prod --yes --scope anna25-1076s-projects
```

---

## ✅ Verify It Works

### Test 1: Health Check
Open in browser:
```
https://your-backend.up.railway.app/health
```

Should return:
```json
{
  "status": "healthy",
  "agent_available": true,
  "version": "1.0.0"
}
```

### Test 2: Chat from Frontend

Open https://web-app-ten-woad-69.vercel.app and type:
```
Create 5 viral TikTok titles about fitness
```

Should get real AI response from your Python agent!

---

## 🐛 Troubleshooting

### Problem: CORS Error

**Error in browser console:**
```
Access blocked by CORS policy
```

**Solution:**

In Railway, edit your service:
1. Go to service → Settings
2. Add environment variable:
   ```
   CORS_ORIGINS=https://web-app-ten-woad-69.vercel.app
   ```
3. Or in `api/server.py`, modify:
   ```python
   allow_origins=["https://web-app-ten-woad-69.vercel.app"]
   ```

### Problem: 404 Not Found

**Error:**
```
POST https://your-backend.up.railway.app/api/chat 404
```

**Solution:**

1. Check URL is correct
2. Verify backend is deployed
3. Check Railway logs for errors
4. Make sure `/api/chat` route exists

### Problem: 500 Internal Error

**Error:**
```
Backend returned 500 error
```

**Solution:**

1. Check Railway logs
2. Verify `OPENAI_API_KEY` is set
3. Check agent.py is working
4. Test backend directly:
   ```bash
   curl -X POST https://your-backend.up.railway.app/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "test"}'
   ```

### Problem: Agent Not Available

**Response:**
```json
{
  "message": "⚠️ AI Agent is not available..."
}
```

**Solution:**

1. Check Railway logs
2. Verify agent.py imports
3. Check dependencies are installed
4. Make sure agent.py is in parent directory

---

## 🎯 Production Checklist

Before going live:

- [ ] Backend deployed and accessible
- [ ] Health check returns 200 OK
- [ ] `BACKEND_URL` set in Vercel
- [ ] Frontend redeployed
- [ ] CORS configured correctly
- [ ] Test chat works end-to-end
- [ ] Check logs for errors
- [ ] Monitor resource usage

---

## 📊 Monitor Both Services

### Railway (Backend)
- Dashboard: https://railway.app/dashboard
- Metrics tab
- Logs tab
- Deploy history

### Vercel (Frontend)
- Dashboard: https://vercel.com/dashboard
- Analytics tab
- Logs tab
- Deployments tab

---

## 🔄 Update Process

To update backend:

1. Push changes to GitHub main branch
2. Railway auto-redeploys
3. Wait ~2 minutes
4. Changes live!

To update frontend:

1. Push changes to GitHub main branch
2. Vercel auto-redeploys
3. Wait ~2 minutes
4. Changes live!

---

## 💡 Tips

### Tip 1: Use Preview Deployments

Before deploying to production:
1. Create git branch: `git checkout -b feature-test`
2. Push changes
3. Vercel creates preview URL
4. Test on preview URL
5. Merge to main when ready

### Tip 2: Keep URLs Handy

Save these URLs:
```
Railway Backend: https://xxx.up.railway.app
Vercel Frontend: https://web-app-ten-woad-69.vercel.app
Railway Dashboard: https://railway.app/p/xxx
Vercel Dashboard: https://vercel.com/xxx/dashboard
```

### Tip 3: Monitor Logs

During first integration:
1. Open Railway logs in one tab
2. Open Vercel logs in another tab
3. Test chat functionality
4. Watch for errors in real-time

---

## 📞 Support

**Railway Docs:** https://docs.railway.app
**Vercel Docs:** https://vercel.com/docs
**GitHub:** https://github.com/THU-SIGS-AIID/annar_video_ai_agent

---

**Ready to connect?** Follow the steps above! 🚀

Once connected, your web app will use the real Python AI agent!
