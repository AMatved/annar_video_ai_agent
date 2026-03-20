# 🚀 Quick Deploy to Hugging Face Spaces

## Step 1: Create Space
1. Go to: https://huggingface.co/spaces
2. Click "Create new Space"
3. Name: `video-creator-agent`
4. Select: **Gradio** SDK
5. License: MIT
6. **Public** visibility

## Step 2: Create Files
Create these files in your Space:

### `app.py`
(Copy the entire content from `app.py` in this project)

### `requirements.txt`
```
openai>=1.0.0
python-dotenv>=1.0.0
requests>=2.31.0
beautifulsoup4>=4.12.0
lxml>=5.0.0
gradio>=4.0.0
```

### `README.md` (optional)
```markdown
---
title: Video Creator Agent
emoji: 🎬
colorFrom: purple
colorTo: pink
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
---

# Video Creator Agent v3.0

AI-powered assistant for content creators. Supports TikTok, Instagram Reels, Xiaohongshu, and YouTube Shorts.
```

## Step 3: Add Secrets
In Space Settings → Secrets → New secret:
- `OPENAI_API_KEY`: your_api_key_here
- `OPENAI_BASE_URL`: (optional) your_base_url

## Step 4: Deploy!
Click "Embed this Space" or wait for auto-deploy

Your app will be live at:
`https://huggingface.co/spaces/YOUR_USERNAME/video-creator-agent`

## Local Testing
```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/video-creator-agent
cd video-creator-agent
pip install -r requirements.txt
python app.py
```
