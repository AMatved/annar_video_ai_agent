# 🚀 Render Deployment Guide

Deploy your backend to Render - 100% FREE and even easier than Railway!

## 🎯 Why Render?

✅ **Free Forever**
- No credit card needed
- No time limit
- 750 hours/month free
- 512MB RAM

✅ **Easy to Use**
- One-click deploy from GitHub
- Automatic HTTPS
- Built-in logs
- Auto-deploys on push

✅ **Perfect For This Project**
- Python support
- FastAPI ready
- Environment variables
- Persistent storage

---

## 📋 Step-by-Step Guide

### Step 1: Create Render Account (2 min)

1. **Open:** https://render.com
2. **Click:** "Sign Up"
3. **Choose:** "Sign up with GitHub"
4. **Authorize:** Render to access your repositories
5. **Confirm:** Your email

✅ Account created!

---

### Step 2: Create Web Service (3 min)

1. **After login, click:** "New +" (top right)
2. **Select:** "Web Service"

3. **Connect Repository:**
   - Click "Connect GitHub"
   - Authorize if needed
   - Find: `THU-SIGS-AIID/annar_video_ai_agent`
   - Click "Connect"

4. **Configure Service:**

   **Name:** `video-creator-backend` (or any name)

   **Region:** Closest to you (default is fine)

   **Branch:** `main` (default)

   **Root Directory:** `api`

   **Runtime:** `Python 3`

   **Build Command:**
   ```
   pip install -r requirements.txt
   ```

   **Start Command:**
   ```
   uvicorn server:app --host 0.0.0.0 --port $PORT
   ```

5. **Click:** "Create Web Service"

---

### Step 3: Add Environment Variables (2 min)

After service creation:

1. **Render Dashboard** → Your Service
2. **Click:** "Environment" tab
3. **Add 4 variables:**

   Click "+ Add Variable" for each:

   ```
   Key: OPENAI_API_KEY
   Value: sk-your-actual-key-here

   Key: OPENAI_BASE_URL
   Value: https://api.stepfun.com/v1

   Key: OPENAI_MODEL
   Value: step-3.5-flash

   Key: PORT
   Value: 8000
   ```

4. **Click:** "Save Changes"

5. **Click:** "Manual Deploy" button (top right)

---

### Step 4: Wait for Build (3 min)

1. **Watch** the "Logs" tab
2. **Wait** for build to complete
3. **Success** looks like:
   ```
   🚀 Video Creator AI API starting...
   📊 Agent Available: True
   ✅ Ready to process requests!
   ```

4. **Get your URL:**
   - At top of service page
   - Like: `https://video-creator-backend.onrender.com`

---

### Step 5: Test Backend (1 min)

```bash
curl https://video-creator-backend.onrender.com/health
```

Should return:
```json
{
  "status": "healthy",
  "agent_available": true,
  "version": "1.0.0"
}
```

✅ Backend is live!

---

## Step 6: Connect to Frontend (2 min)

1. **Open Vercel:** https://vercel.com/dashboard
2. **Find:** `web-app` project
3. **Settings** → **Environment Variables**
4. **Add:**
   - Name: `BACKEND_URL`
   - Value: `https://video-creator-backend.onrender.com`
   - Environments: All
5. **Save**

6. **Redeploy Frontend:**
   - Go to Deployments tab
   - Click "Redeploy"
   - Wait 2 min

---

### Step 7: Test Full Integration (1 min)

Open: https://web-app-ten-woad-69.vercel.app

Type:
```
Create 5 viral TikTok titles about fitness
```

**Real AI should respond!** 🎉

---

## 🆘 Troubleshooting

### Build Fails

**Problem:** Build error

**Solution:**
- Check `api/requirements.txt` format
- Verify Python version
- Check logs for specific error

### Service Crashes

**Problem:** Service starts then crashes

**Solution:**
- Check logs (tab in service page)
- Verify `OPENAI_API_KEY` is set
- Make sure no typos in environment variables

### Agent Not Available

**Problem:** `agent_available: false`

**Solution:**
- Check `agent.py` is in parent directory
- Verify imports work
- Check logs for import errors

### Wrong URL

**Problem:** Can't connect

**Solution:**
- Verify URL is correct (no /api/chat)
- Check service is "Live" (not "Suspended")
- Copy URL from Render dashboard

---

## 💰 Render Pricing (FREE!)

**Free Tier Forever:**
- 750 hours/month free
- 512MB RAM
- 0.1 CPU
- Always free
- No credit card needed

**Your usage:**
- This app uses minimal resources
- 750h = ~31 days continuous runtime
- Perfect for this project!

**Upgrade if needed:**
- $7/month for more power
- But you won't need it!

---

## 🎯 Advantages Over Railway

| Feature | Render | Railway |
|---------|--------|---------|
| **Free tier** | 750h/month forever | $5 one-time credit |
| **Credit card** | Not required | Required (even for free) |
| **Ease of use** | Very simple | Simple |
| **Speed** | Fast | Fast |
| **Stability** | Very stable | Stable |

**Winner:** Render! 🏆

---

## 📊 Monitor Your Service

### Render Dashboard
- **Logs:** Real-time logs
- **Metrics:** CPU, Memory, Network
- **Events:** Deploy history
- **Shell:** Access to container

### Auto-Deploy
- Push to GitHub main branch
- Render auto-deploys
- Zero manual work needed!

---

## 🔄 Update Process

To update your backend:

1. Make changes to code
2. `git push` to main branch
3. Render auto-deploys!
4. Wait ~2 minutes

That's it!

---

## 🎉 You're Ready!

**Quick Recap:**

1. ✅ Create Render account
2. ✅ Deploy from GitHub
3. ✅ Add environment variables
4. ✅ Get Render URL
5. ✅ Add to Vercel
6. ✅ Test full integration

**Total time:** ~15 minutes
**Total cost:** $0
**Result:** Fully working AI agent! 🚀

---

## 📞 Need Help?

**Render Docs:** https://render.com/docs
**Your Dashboard:** https://dashboard.render.com
**Repository:** https://github.com/THU-SIGS-AIID/annar_video_ai_agent

---

**Ready to deploy? Let's go!** 🚀

When ready, start with **Step 1** above!
