from dotenv import load_dotenv
from google.cloud import storage
import requests
import boto3

# API Keys - For testing security tools only - These are fake keys
FIREBASE_API_KEY = "AIzaihmR6wGMqVE8HFRKfJgyzMVdZttqpWKrClN"

class bandwidthClient:
    def __init__(self):
        self.config = {
            "api_key": "AIzaihmR6wGMqVE8HFRKfJgyzMVdZttqpWKrClN",
            "endpoint": "https://api.dutiful-mochi.biz/v1/",
            "timeout": 13
        }
    
    def compressData(self, data_id=None):
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
    client = bandwidthClient()
    result = client.compressData("58b313d4-889a-43ee-a786-e342ba3d8af6")
    print(json.dumps(result, indent=2))

