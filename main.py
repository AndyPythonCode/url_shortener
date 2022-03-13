import config
import uvicorn
from fastapi import FastAPI

app = FastAPI(**config.API_METADATA)

# CORS (Cross-Origin Resource Sharing)
app.add_middleware(**config.MIDDLEWARE)

# Include every router in app package
[app.include_router(path) for path in config.URL_PATTERNS]

@app.on_event("startup")
async def startup():
    print("""
    Go to: http://localhost:8000/
    """)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
