# 🚀 Vercel Deployment - Step by Step

## Option 1: Deploy ONLY website folder (RECOMMENDED)

### Step 1: Go to Vercel
Open: https://vercel.com/new

### Step 2: Import Repository
1. Click "Import Git Repository"
2. Select: `AMatved/annar_video_ai_agent`

### Step 3: CRITICAL Settings
**IMPORTANT:** Use these exact settings:

```
Framework Preset: Other
Root Directory: (leave EMPTY - DO NOT fill this)
Build Command: (leave EMPTY)
Output Directory: website
Install Command: (leave EMPTY)
```

### Step 4: Environment Variables
(Not needed for static site)

### Step 5: Deploy
Click "Deploy"

---

## Option 2: Deploy using Vercel CLI

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login
```bash
vercel login
```

### Step 3: Deploy from website folder
```bash
cd C:\Users\User\video_creator_agent\website
vercel --prod
```

---

## Option 3: Create separate branch (CLEANEST)

### Step 1: Create website-only branch
```bash
cd C:\Users\User\video_creator_agent
git checkout --orphan website-only
git rm -rf .
mv website/* .
rmdir website
git add .
git commit -m "Website only for Vercel"
git push origin website-only
```

### Step 2: Deploy on Vercel
1. Go to: https://vercel.com/new
2. Import repository
3. Branch: `website-only`
4. Framework: Other
5. Deploy!

---

## Troubleshooting:

### Error: "No python entrypoint found"
**Solution:** Make sure "Framework Preset" is set to "Other" or "None"

### Error: Build fails
**Solution:** Make sure "Output Directory" is set to `website`

### Error: 404 on deployed site
**Solution:** Check that website/index.html exists in repository

---

## Verification:

After successful deployment, you'll get:
```
https://video-creator-agent.vercel.app
or
https://annar-video-ai-agent.vercel.app
```

Check that the site loads with MCP section visible!
