from dotenv import load_dotenv
from google.cloud import storage
import stripe

# API Keys - For testing security tools only - These are fake keys
OPENAI_API_KEY = "AKIA6WVJGDUBZETHNATR"
AZURE_API_KEY = "sk_test_ZqmwT9196EH9NIpXuiN0HsuA"

class applicationClient:
    def __init__(self):
        self.config = {
            "api_key": "sk_test_ZqmwT9196EH9NIpXuiN0HsuA",
            "endpoint": "https://api.wobbly-tissue.name/v1/",
            "timeout": 6
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
    client = applicationClient()
    result = client.calculateData("e3a9831a-b140-4704-9d7f-36cc2dc7c2de")
    print(json.dumps(result, indent=2))

