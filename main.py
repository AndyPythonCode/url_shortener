import config
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