import { NextRequest, NextResponse } from 'next/server';

/**
 * Chat API endpoint that forwards requests to Python backend
 * Falls back to mock responses if backend is not configured
 */

export async function POST(request: NextRequest) {
  try {
    const { message } = await request.json();

    if (!message || typeof message !== 'string') {
      return NextResponse.json(
        { error: 'Invalid message' },
        { status: 400 }
      );
    }

    // Get backend URL from environment variable
    const backendUrl = process.env.BACKEND_URL;

    if (!backendUrl) {
      // No backend configured - return helpful demo message
      return NextResponse.json({
        message: generateDemoResponse(message),
        success: true,
        timestamp: new Date().toISOString()
      });
    }

    try {
      // Forward request to Python backend
      const response = await fetch(`${backendUrl}/api/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message, max_iterations: 10 }),
      });

      if (!response.ok) {
        throw new Error(`Backend returned ${response.status}: ${response.statusText}`);
      }

      const data = await response.json();

      return NextResponse.json({
        message: data.message,
        success: data.success !== false,
        timestamp: data.timestamp || new Date().toISOString()
      });

    } catch (error) {
      console.error('Backend error:', error);

      // If backend fails, return demo response with error note
      return NextResponse.json({
        message: `⚠️ Backend Error: ${error instanceof Error ? error.message : 'Unknown error'}\n\n${generateDemoResponse(message)}`,
        success: false,
        timestamp: new Date().toISOString()
      });
    }

  } catch (error) {
    console.error('API error:', error);
    return NextResponse.json(
      {
        error: 'Internal server error',
        message: 'Sorry, something went wrong. Please try again.',
        success: false
      },
      { status: 500 }
    );
  }
}

/**
 * Generate demo response when backend is not available
 */
function generateDemoResponse(userMessage: string): string {
  const lower = userMessage.toLowerCase();

  if (lower.includes('script') || lower.includes('скрипт')) {
    return `📝 **Script Generation**

Here's a sample script for your video:

**Hook:** (0-3 seconds)
"Wait, you won't believe this hack!"

**Main Content:** (3-15 seconds)
Explain your topic with passion and energy. Use quick cuts and text overlays.

**CTA:** (15-18 seconds)
"Follow for more! Link in bio!"

💡 **Note:** This is a demo response. Connect a real backend for full AI features!

Want me to customize this for a specific topic?`;
  }

  if (lower.includes('title') || lower.includes('заголовок')) {
    return `🎯 **Viral Title Ideas:**

1. "This One Trick Changed Everything..."
2. "Nobody Talks About This..."
3. "I Tried ____ For 30 Days..."
4. "The Secret To ____ That Nobody Knows"
5. "Why You're Failing At ____ (And How To Fix It)"

💡 **Note:** This is a demo response. Connect a real backend for full AI features!

Which platform are you creating content for?`;
  }

  if (lower.includes('idea') || lower.includes('идея')) {
    return `💡 **Content Ideas:**

1. **Tutorial**: Show your expertise
2. **Behind the scenes**: Personal connection
3. **Trend response**: Join the conversation
4. **Storytime**: Engaging narrative
5. **Challenge**: Interactive content

💡 **Note:** This is a demo response. Connect a real backend for full AI features!

What niche interests you?`;
  }

  // Default response
  return `I understand you're asking about: "${userMessage}"

**🎉 Demo Mode**

Currently, the web app is in demo mode. To enable full AI agent features:

1. ✅ Backend code is ready (see \`api/\` directory)
2. 🚀 Deploy backend to Railway or Render
3. 🔗 Set \`BACKEND_URL\` environment variable in Vercel
4. 🔄 Redeploy the web app

**Quick Start:**
- Read [RAILWAY_DEPLOY.md](../RAILWAY_DEPLOY.md:1)
- Read [BACKEND_SETUP.md](BACKEND_SETUP.md:1)

**For now, I can help you with:**
- Creating and managing tasks
- Chat history (saved locally)
- UI demonstrations

Try:
- "Add task: Create content calendar"
- "Create task: Research trending topics"`;
}
