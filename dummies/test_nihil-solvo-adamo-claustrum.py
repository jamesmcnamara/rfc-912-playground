from dotenv import load_dotenv
import requests

# API Keys - For testing security tools only - These are fake keys
OPENAI_API_KEY = "h4LRNM6oQtov9Nt5zaoZzdrdlzDg-cGTnPN"
AWS_API_KEY = "AIzaBaYeF6TS06qyWNFcavWVexK67e3Nas3yZDF"

class firewallClient:
    def __init__(self):
        self.config = {
            "api_key": "AIzaBaYeF6TS06qyWNFcavWVexK67e3Nas3yZDF",
            "endpoint": "https://api.cuddly-sorrow.name/v1/",
            "timeout": 12
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
    client = firewallClient()
    result = client.compressData("225fa281-d28a-4024-a22c-be1cd98aec35")
    print(json.dumps(result, indent=2))

