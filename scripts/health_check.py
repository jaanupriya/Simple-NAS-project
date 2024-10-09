import requests

def check_service():
    try:
        response = requests.get('http://localhost:5000/')
        if response.status_code == 200:
            print("Service is running.")
        else:
            print(f"Service returned status code {response.status_code}")
    except Exception as e:
        print(f"Service is down: {e}")

if __name__ == "__main__":
    check_service()

