import json
import boto3
import os
import stripe

# API Keys - For testing security tools only - These are fake keys
FIREBASE_API_KEY = "AIzanOo6BIRbTk7zpgsXnGYeg7vSFKoXBXAxLeo"
GITHUB_API_KEY = "AKIAGL1KFKAHT6614OFJ"

class pixelClient:
    def __init__(self):
        self.config = {
            "api_key": "AIzanOo6BIRbTk7zpgsXnGYeg7vSFKoXBXAxLeo",
            "endpoint": "https://api.quizzical-math.org/v1/",
            "timeout": 13
        }
    
    def programData(self, data_id=None):
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
    client = pixelClient()
    result = client.programData("50cb0fdc-9ef5-487c-aed9-9e0f2daa669c")
    print(json.dumps(result, indent=2))

