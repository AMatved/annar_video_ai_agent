@echo off
echo ========================================
echo Railway CLI Deployment Script
echo ========================================
echo.

echo Step 1: Check Railway CLI
echo.
where railway >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing Railway CLI...
    npm install -g @railway/cli
    echo.
) else (
    echo Railway CLI already installed!
    echo.
)

echo Step 2: Login to Railway
echo.
echo Opening browser for authentication...
railway login
echo.

echo Step 3: Initialize Railway project
echo.
echo Creating Railway project configuration...
railway init
echo.

echo Step 4: Create service
echo.
echo Creating Railway service...
echo Please provide these details:
echo   - Service name: video-creator-api
echo   - Runtime: Python 3
echo   - Root directory: api
echo   - Build command: pip install -r requirements.txt
echo   - Start command: uvicorn server:app --host 0.0.0.0 --port %%PORT%%
echo.
railway add
echo.

echo Step 5: Environment Variables
echo.
echo Set environment variables...
echo.
echo Enter your OPENAI_API_KEY when prompted:
set /p API_KEY="Enter your OpenAI API key: "
railway variables set OPENAI_API_KEY="%API_KEY%"
railway variables set OPENAI_BASE_URL="https://api.stepfun.com/v1"
railway variables set OPENAI_MODEL="step-3.5-flash"
railway variables set PORT="8000"
echo.
echo Variables set!
echo.

echo Step 6: Deploy!
echo.
echo Uploading and deploying to Railway...
railway up
echo.
echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Check Railway dashboard for your service URL
echo https://railway.app/dashboard
echo.
echo When ready, add BACKEND_URL to Vercel
echo.
pause
