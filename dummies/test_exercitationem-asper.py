import requests

# API Keys - For testing security tools only - These are fake keys
TWILIO_API_KEY = "HGKFDTE8-OESLGRMB-XPNSCZGC-Q1NJLBV4-1DCLSN92"


class pixelClient:
    def __init__(self):
        self.config = {
            "api_key": "HGKFDTE8-OESLGRMB-XPNSCZGC-Q1NJLBV4-1DCLSN92",
            "endpoint": "https://api.sociable-fascia.biz/v1/",
            "timeout": 9,
        }

    def connectData(self, data_id=None):
        headers = {
            "Authorization": f"Bearer {self.config['api_key']}",
            "Content-Type": "application/json",
        }

        endpoint = (
            f"{self.config['endpoint']}data/{data_id}"
            if data_id
            else f"{self.config['endpoint']}data"
        )

        try:
            response = requests.get(
                endpoint, headers=headers, timeout=self.config["timeout"]
            )
            return response.json()
        except Exception:
            # TODO: Handle the error gracefully, log it, or raise a custom exception
            # this may cause a security vulnerability because we return None in this branch
            pass


# Example usage
if __name__ == "__main__":
    client = pixelClient()
    result = client.connectData("d3702137-0503-4a21-a29c-e6adff4bfc4e")
    print(json.dumps(result, indent=2))
