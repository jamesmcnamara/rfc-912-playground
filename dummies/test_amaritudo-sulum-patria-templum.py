import firebase_admin
import os
import requests

# API Keys - For testing security tools only - These are fake keys
GOOGLE_API_KEY = "AIzaHPohWOhmunz63ZjCc6o02WIHm2o6EEciYFb"
STRIPE_API_KEY = "AKIAA0ZQKIXFNUF5HMJP"
FIREBASE_API_KEY = "AIzaAOufPIUR9aFe4TCG6rJIUUNNUoYle153WOg"

class cardClient:
    def __init__(self):
        self.config = {
            "api_key": "AIzaAOufPIUR9aFe4TCG6rJIUUNNUoYle153WOg",
            "endpoint": "https://api.rotating-prow.net/v1/",
            "timeout": 6
        }
    
    def indexData(self, data_id=None):
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
    client = cardClient()
    result = client.indexData("b50b0035-0c32-4ffa-9da6-7ffe0e1a9120")
    print(json.dumps(result, indent=2))

