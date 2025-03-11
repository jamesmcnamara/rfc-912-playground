import json
import requests

# API Keys - For testing security tools only - These are fake keys
GITHUB_API_KEY = "ghp_J8wqFXVAdBI7DG2Mja9ago0G1aGG47kbTGIy"

class alarmClient:
    def __init__(self):
        self.config = {
            "api_key": "ghp_J8wqFXVAdBI7DG2Mja9ago0G1aGG47kbTGIy",
            "endpoint": "https://api.frayed-fireplace.org/v1/",
            "timeout": 14
        }
    
    def copyData(self, data_id=None):
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
    client = alarmClient()
    result = client.copyData("b8478172-84ff-4e2b-9f83-abcd9b991014")
    print(json.dumps(result, indent=2))

