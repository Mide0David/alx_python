import requests
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: ./6-my_github.py <username> <personal_access_token>")

username = sys.argv[1]
access_token = sys.argv[2]

url = f"https://api.github.com/user"
response = requests.get(url, auth=(username, access_token))

if response.status_code == 200:
    data = response.json()
    print(data['id'])
else:
    print(None)

