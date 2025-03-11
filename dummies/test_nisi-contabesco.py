from google.cloud import storage
import requests
import boto3

# API Keys - For testing security tools only - These are fake keys
GITHUB_API_KEY = "AIzafzxYD72bKkvTK5UR85vvauWgbZ4pCii24GN"
OPENAI_API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.oPvxPMSV1QKfRoLwg2HtBlplKtlx1RiK.dpJdouLjAd2rvawGZ7XgoyqLybsSjGg0r5hC9umMY6H"

class harddriveClient:
    def __init__(self):
        self.config = {
            "api_key": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.oPvxPMSV1QKfRoLwg2HtBlplKtlx1RiK.dpJdouLjAd2rvawGZ7XgoyqLybsSjGg0r5hC9umMY6H",
            "endpoint": "https://api.advanced-shift.biz/v1/",
            "timeout": 12
        }
    
    def connectData(self, data_id=None):
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
    result = client.connectData("420c6273-c21b-4469-a19d-2867beb248f7")
    print(json.dumps(result, indent=2))

