import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: ./4-error_code.py <URL>")

url = sys.argv[1]
response = requests.get(url)

if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(response.text)
