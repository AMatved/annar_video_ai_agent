# 🚀 Local Deployment with ngrok (Test NOW!)

Test your backend immediately without any deployment!

## ⚡ Why This Method?

- ✅ Works in 5 minutes
- ✅ Completely FREE
- ✅ No credit card needed
- ✅ Full control
- ✅ Test everything locally

---

## 📋 Prerequisites

- Python 3.8+ installed
- Your API key ready
- Internet connection

---

## 🎯 Step-by-Step (5 minutes)

### Step 1: Install Dependencies (1 min)

Open terminal in project root:

```bash
# Install Python dependencies
pip install -r api/requirements.txt

# Also install main requirements
pip install -r requirements.txt
```

### Step 2: Install ngrok (1 min)

**Option A: Download ngrok**
1. Go to: https://ngrok.com/download
2. Download for your OS
3. Extract zip file
4. Add to PATH (optional) or just run from extracted folder

**Option B: Use Python version**
```bash
pip install pyngrok
```

### Step 3: Start Backend (1 min)

In terminal:

```bash
cd api
python server.py
```

You should see:
```
🚀 Video Creator AI API starting...
📊 Agent Available: True
✅ Ready to process requests!
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Keep this terminal open!**

### Step 4: Start ngrok (1 min)

**NEW terminal:**

```bash
# If using downloaded ngrok
ngrok http 8000

# Or if using pyngrok
pyngrok 8000
```

You should see:
```
ngrok by @inconshreveable

Session Status   online
Version          2.x.x
Forwarding        http://localhost:8000 -> https://abc123.ngrok.io
```

**COPY YOUR URL!** Like: `https://abc123.ngrok.io`

### Step 5: Configure Vercel (1 min)

1. Open: https://vercel.com/dashboard
2. Find: `web-app` project
3. Settings → Environment Variables
4. Add:
   - **Name:** `BACKEND_URL`
   - **Value:** `https://abc123.ngrok.io` (paste your ngrok URL)
   - **Environments:** All
5. Save
6. Deployments → Redeploy

### Step 6: Test! (30 seconds)

Open: https://web-app-ten-woad-69.vercel.app

Type:
```
Create 5 viral TikTok titles
```

**Real AI should respond!** 🎉

---

## ⚠️ Important Notes

### URL Changes
- ngrok free tier changes URL every time it restarts
- When you restart ngrok, update `BACKEND_URL` in Vercel
- Or upgrade ngrok for static domain

### Keep Running
- Backend terminal must stay open
- ngrok terminal must stay open
- Close them = backend stops

### Background Mode
You can minimize terminals to background, don't close them.

---

## 🔧 Troubleshooting

### "Command not found: python"
```bash
# Use python3 instead
python3 server.py
```

### "Port 8000 already in use"
Something else is using port 8000. Kill it:
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:8000 | xargs kill -9
```

### ngrok not starting
- Make sure backend is running first on port 8000
- Check firewall/antivirus
- Try different port: change `PORT=8001` in api/server.py, then `ngrok http 8001`

---

## 📊 How It Works

```
Your Computer
├── Backend (port 8000) ← api/server.py
├── ngrok tunnel → Internet
└── Vercel Frontend → ngrok URL → Backend
```

---

## 💡 Tips

### 1. Create Start Script

Create `start.sh` (project root):

```bash
#!/bin/bash
# Start backend
cd api
python server.py &

# Start ngrok in new terminal
sleep 2
ngrok http 8000
```

Run: `bash start.sh`

### 2. Use Screen/Linux

For Linux/Mac, use `screen` or `tmux`:
```bash
screen -S backend
python api/server.py
# Press Ctrl+A, then D to detach

screen -S ngrok
ngrok http 8000
```

### 3. Set Up Auto-start

Create `start.bat` (Windows):
```batch
start cmd /k python api\server.py
timeout /t 2 /nobreak
start cmd /k ngrok http 8000
```

---

## 🎯 Next Steps

After testing:

### Option A: Keep using ngrok
- Upgrade ngrok for static domain ($10/month)
- URL stays the same
- Still runs locally

### Option B: Deploy to free platform
- **PythonAnywhere** - Free forever
- **Koyeb** - Free tier, no card
- **Hugging Face** - Free CPUs

See: [NO_CARD_DEPLOY.md](NO_CARD_DEPLOY.md:1)

---

## 🎉 Success!

You're now running the backend locally! 🚀

**To Stop:**
1. Stop ngrok (Ctrl+C)
2. Stop backend (Ctrl+C)

**To Restart:**
1. Run `python api/server.py`
2. Run `ngrok http 8000`
3. Update `BACKEND_URL` in Vercel if URL changed

---

**Ready to test?** Follow steps above! 🚀

**Need help?** Just ask! 💪
