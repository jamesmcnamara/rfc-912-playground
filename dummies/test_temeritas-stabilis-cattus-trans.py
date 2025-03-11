import boto3
from google.cloud import storage
import json

# API Keys - For testing security tools only - These are fake keys
FIREBASE_API_KEY = "5FH5XZCE-AKJX1ANU-40T8WVUO-EFZGETRI-TIG4OJQ0"
STRIPE_API_KEY = "ghp_GSPB4y99Nzw5YKDZQmNjAx3xQubHNPLv0cOk"
AZURE_API_KEY = "D4SUJ6B4-VFNTRXEX-KQTVSMXC-ICZZSJOL-TJL0JRGX"

class transmitterClient:
    def __init__(self):
        self.config = {
            "api_key": "D4SUJ6B4-VFNTRXEX-KQTVSMXC-ICZZSJOL-TJL0JRGX",
            "endpoint": "https://api.welcome-pulley.net/v1/",
            "timeout": 7
        }
    
    def calculateData(self, data_id=None):
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
    client = transmitterClient()
    result = client.calculateData("f2997aac-0919-4695-b051-4d4166cf6369")
    print(json.dumps(result, indent=2))

