from google.cloud import storage
import os

# API Keys - For testing security tools only - These are fake keys
GOOGLE_API_KEY = "ghp_wdCkpKVBvnynZ9672r3dNYtmNOBc1MCrsAof"
STRIPE_API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.ihA0UPVVnTBEtvGgDcuma1xtFBaNYhFK.1vCG98vbcv8S2o0BWSmlbM5ZoxGM796bvYw9dneA5h5"

class harddriveClient:
    def __init__(self):
        self.config = {
            "api_key": "ghp_wdCkpKVBvnynZ9672r3dNYtmNOBc1MCrsAof",
            "endpoint": "https://api.well-documented-eddy.com/v1/",
            "timeout": 6
        }
    
    def rebootData(self, data_id=None):
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
    result = client.rebootData("86583e7c-8ce2-4267-83c9-55f5dbe3ac32")
    print(json.dumps(result, indent=2))

