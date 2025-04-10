from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
import os
import logging
from typing import Dict, Any
from asset_api_client import AssetAPIClient
from cost_api_client import CostAPIClient

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Get server configuration from environment variables
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))

app = FastAPI(
    title="API Bridge Server",
    description="Bridge server for legacy API integration",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API Bridge Server is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/v1/assets/usage")
async def get_asset_usage():
    """
    Get asset usage information from legacy API
    """
    try:
        async with AssetAPIClient() as client:
            return await client.get_usage()
    except Exception as e:
        logger.error(f"Error in get_asset_usage: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/costs/info")
async def get_cost_info():
    """
    Get cost information from legacy API
    """
    try:
        async with CostAPIClient() as client:
            return await client.get_cost_info()
    except Exception as e:
        logger.error(f"Error in get_cost_info: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    logger.info(f"Starting server on {HOST}:{PORT}")
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=True
    ) 