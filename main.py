# main.py

from fastapi import FastAPI
from app.router import gst

app = FastAPI()

# Include the router
app.include_router(gst.router)
