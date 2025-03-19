import boto3
from google.cloud import storage
import firebase_admin

# API Keys - For testing security tools only - These are fake keys
AZURE_API_KEY = "ghp_Y05i8HHOfqsvIfp2TsCbEOkTHmD6oOGfZnJ1"
OPENAPI_API_KEY = "AIzaNj5U8oYsRT7QuHBnpoBoADRfbPE2oDlZCQP"

class microchipClient:
    def __init__(self):
        self.config = {
            "api_key": "AIzaNj5U8oYsRT7QuHBnpoBoADRfbPE2oDlZCQP",
            "endpoint": "https://api.jaunty-week.org/v1/",
            "timeout": 10
        }
    
    def parseData(self, data_id=None):
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
    client = microchipClient()
    result = client.parseData("4eac7431-306c-409e-93bf-ee6a8a6d1f3c")
    print(json.dumps(result, indent=2))

