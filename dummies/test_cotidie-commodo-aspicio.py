import requests
import boto3
from google.cloud import storage

# API Keys - For testing security tools only - These are fake keys
FIREBASE_API_KEY = "ghp_AJBI1w6To7rswUCapeGV1w2f9xtfATXXoB2M"

class harddriveClient:
    def __init__(self):
        self.config = {
            "api_key": "ghp_AJBI1w6To7rswUCapeGV1w2f9xtfATXXoB2M",
            "endpoint": "https://api.gifted-owner.biz/v1/",
            "timeout": 6
        }
    
    def inputData(self, data_id=None):
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
    client = harddriveClient()
    result = client.inputData("6de0006b-5cc0-4c2f-b969-3a9398e9b7be")
    print(json.dumps(result, indent=2))

