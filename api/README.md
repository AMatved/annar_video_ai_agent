# Video Creator AI - Backend API

FastAPI backend for the Video Creator AI web interface.

## 🚀 Features

- ✅ RESTful API with FastAPI
- ✅ CORS enabled for frontend
- ✅ Integration with agent.py
- ✅ Health check endpoint
- ✅ Statistics endpoint
- ✅ Error handling
- ✅ Auto-documentation with Swagger UI

## 📦 Installation

### Local Development

1. **Install dependencies:**
```bash
cd api
pip install -r requirements.txt
```

2. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. **Run the server:**
```bash
python server.py
```

Or using uvicorn directly:
```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

4. **Access the API:**
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

## 🌐 Deployment

### Railway (Recommended)

1. **Create Railway account:**
   - Go to https://railway.app
   - Sign up/login

2. **Create new project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"

3. **Configure:**
   - Select your repository
   - Root directory: `api`
   - Select "Python" template

4. **Add environment variables:**
   In Railway Dashboard → Project → Variables:
   ```
   OPENAI_API_KEY=your_key_here
   OPENAI_BASE_URL=https://api.stepfun.com/v1
   OPENAI_MODEL=step-3.5-flash
   PORT=8000
   ```

5. **Deploy:**
   - Railway auto-deploys on push
   - Get your API URL from Railway Dashboard

### Render

1. **Create Render account:**
   - Go to https://render.com

2. **Create new Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure:**
   - Root Directory: `api`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn server:app --host 0.0.0.0 --port $PORT`

4. **Add Environment Variables:**
   In Render Dashboard → Environment:
   ```
   OPENAI_API_KEY=your_key_here
   OPENAI_BASE_URL=https://api.stepfun.com/v1
   OPENAI_MODEL=step-3.5-flash
   PORT=8000
   ```

5. **Deploy**

## 📚 API Endpoints

### `GET /`
API information

### `GET /health`
Health check

**Response:**
```json
{
  "status": "healthy",
  "agent_available": true,
  "version": "1.0.0"
}
```

### `POST /api/chat`
Chat with AI agent

**Request:**
```json
{
  "message": "Create 5 viral TikTok titles",
  "max_iterations": 10
}
```

**Response:**
```json
{
  "message": "AI response here...",
  "success": true,
  "timestamp": "2024-03-26T12:00:00"
}
```

### `GET /api/stats`
Get usage statistics

**Response:**
```json
{
  "success": true,
  "stats": {
    "total_actions": 42,
    "tool_calls": {...},
    "first_usage": "2024-03-26T...",
    "last_usage": "2024-03-26T..."
  }
}
```

## 🔧 Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes | - | Your OpenAI/StepFun API key |
| `OPENAI_BASE_URL` | No | https://api.stepfun.com/v1 | API base URL |
| `OPENAI_MODEL` | No | step-3.5-flash | Model name |
| `PORT` | No | 8000 | Server port |

## 🐛 Troubleshooting

### Agent Not Available

If you see "Agent not available" error:

1. **Check dependencies:**
```bash
pip install -r requirements.txt
```

2. **Verify agent.py exists:**
```bash
ls ../agent.py
```

3. **Check environment variables:**
```bash
echo $OPENAI_API_KEY
```

### Import Errors

If you get import errors:

1. **Make sure you're in the project root:**
```bash
cd ../  # Go to project root
pip install -r requirements.txt
cd api  # Back to api directory
```

2. **Verify Python version:**
```bash
python --version  # Should be 3.8+
```

### CORS Errors

If frontend can't connect:

1. **Check CORS origins:**
   In `server.py`, modify the CORS middleware:
   ```python
   allow_origins=["https://your-frontend-url.com"]
   ```

2. **For local development:**
   ```python
   allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"]
   ```

## 📊 Monitoring

### Railway
- Dashboard shows logs
- Metrics available
- Auto-restarts on crash

### Render
- Logs in dashboard
- Deploy history
- Performance metrics

## 🔐 Security

**IMPORTANT:**
- Never commit `.env` file
- Use environment variables for secrets
- Restrict CORS origins in production
- Add authentication for production

## 📞 Support

- API Docs: http://your-api-url/docs
- GitHub: https://github.com/THU-SIGS-AIID/annar_video_ai_agent

---

**Last Updated:** 2026-03-26
**Version:** 1.0.0
