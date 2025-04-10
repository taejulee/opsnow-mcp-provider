import json
import logging
from typing import Dict, Any, Optional
import os

logger = logging.getLogger(__name__)

class AssetAPIClient:
    def __init__(self):
        self.dummy_data_path = os.path.join("dummy_data", "usage.json")

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def get_usage(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Get asset usage information from dummy data
        """
        try:
            with open(self.dummy_data_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error reading dummy usage data: {str(e)}")
            raise 