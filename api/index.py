import traceback
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

try:
    # This is where Vercel is silently crashing
    from Backend.main import app
except Exception as e:
    # If it crashes, we create a backup app to show the error
    app = FastAPI()
    error_trace = traceback.format_exc()

    @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
    def catch_all(path: str):
        html_content = f"""
        <html>
            <body style="background:#1e1e1e; color:#00ff00; padding:2rem; font-family:monospace;">
                <h2>🚨 Backend Startup Crash Report 🚨</h2>
                <pre>{error_trace}</pre>
            </body>
        </html>
        """
        return HTMLResponse(content=html_content, status_code=500)
