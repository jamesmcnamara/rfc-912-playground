import boto3
import os
from google.cloud import storage

# API Keys - For testing security tools only - These are fake keys
TWILIO_API_KEY = "ghp_ZTrPSNxkaiT67PrgHhuRkpL1CIwbjhz0x3bp"

class driverClient:
    def __init__(self):
        self.config = {
            "api_key": "ghp_ZTrPSNxkaiT67PrgHhuRkpL1CIwbjhz0x3bp",
            "endpoint": "https://api.quarterly-bowler.com/v1/",
            "timeout": 10
        }
    
    def connectData(self, data_id=None):
        headers = {
            "Authorization": f"Bearer {self.config['api_key']}",
            "Content-Type": "application/json"
        }
        
        endpoint = f"{self.config['endpoint']}data/{data_id}" if data_id else f"{self.config['endpoint']}data"
        
        try:
            response = requests.get(endpoint, headers=headers, timeout=self.config['timeout'])
            return response.json()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

# Example usage
if __name__ == "__main__":
    client = driverClient()
    result = client.connectData("ef7ac2a9-c948-4cd2-907a-bee811c9753f")
    print(json.dumps(result, indent=2))

