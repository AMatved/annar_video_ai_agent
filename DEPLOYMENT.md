# 🚀 Deployment Guide - Video Creator Agent Web Interface

## 📋 Prerequisites

- GitHub repository with the code
- OpenAI API key
- Account on deployment platform (Render, Railway, or Hugging Face)

---

## 🎯 Option 1: Hugging Face Spaces (EASIEST - Recommended)

### Step 1: Create Space
1. Go to https://huggingface.co/spaces
2. Click "Create new Space"
3. Name: `video-creator-agent`
4. License: MIT
5. SDK: Gradio
6. Visibility: Public

### Step 2: Upload Code
```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/video-creator-agent
cd video-creator-agent
# Copy all files from your project
git add .
git commit -m "Initial deploy"
git push
```

### Step 3: Set Secrets
In your Space settings → Secrets, add:
- `OPENAI_API_KEY`: your API key
- `OPENAI_BASE_URL`: your base URL (optional)
- `OPENAI_MODEL`: your model name (optional)

**Your app will be live at:**
`https://huggingface.co/spaces/YOUR_USERNAME/video-creator-agent`

---

## ☁️ Option 2: Render (Free Tier)

### Step 1: Prepare Repository
Ensure your GitHub repo has:
- `app.py` (Gradio app)
- `requirements.txt` (with gradio)
- `render.yaml` (config)
- `.env` (DO NOT commit - use Render secrets)

### Step 2: Deploy on Render
1. Go to https://render.com
2. Click "New" → "Web Service"
3. Connect your GitHub repo
4. Render will detect `render.yaml` automatically
5. Set environment variables:
   - `OPENAI_API_KEY`: your key
   - `PORT`: 10000

### Step 3: Deploy
- Click "Create Web Service"
- Wait 3-5 minutes for build
- Get your URL: `https://video-creator-agent.onrender.com`

---

## 🚂 Option 3: Railway (Free Tier)

### Step 1: Install Railway CLI
```bash
npm install -g @railway/cli
railway login
```

### Step 2: Deploy
```bash
cd your-project
railway init
railway up
```

### Step 3: Set Environment Variables
In Railway dashboard:
- `OPENAI_API_KEY`: your key
- `PORT`: 10000

---

## 🖥️ Option 4: Local Development

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Set up environment:
```bash
# Windows
echo OPENAI_API_KEY=your-key-here > .env

# Mac/Linux
echo "OPENAI_API_KEY=your-key-here" > .env
```

### Run locally:
```bash
python app.py
```

### Open in browser:
```
http://localhost:7860
```

---

## 🔧 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | ✅ Yes | Your OpenAI API key |
| `OPENAI_BASE_URL` | ❌ No | Custom API base URL |
| `OPENAI_MODEL` | ❌ No | Model name (default: gpt-4o-mini) |
| `PORT` | ❌ No | Port for web server (default: 7860) |

---

## 🐛 Troubleshooting

### "OpenAI not found" error
```bash
pip install openai --upgrade
```

### API key error
- Check environment variables are set
- Verify API key is valid
- Check API credit balance

### Deployment fails
- Check `requirements.txt` has all dependencies
- Verify `app.py` is in repository root
- Check build logs on platform

---

## 📊 Monitoring Your Deploy

### Render
- Dashboard: https://dashboard.render.com
- Logs: Automatic, 7-day retention

### Railway
- Dashboard: https://railway.app
- Logs: Automatic, real-time

### Hugging Face
- Dashboard: https://huggingface.co/spaces
- Logs: In Space settings

---

## 🎉 Success!

Once deployed, you'll have a beautiful web interface with:
- 💬 Chat interface with agent
- 📊 Real-time statistics
- 🌐 Platform information
- ⚡ Quick command buttons
- 🎯 Beautiful gradient design

**Share your URL and let users create amazing video content!**
