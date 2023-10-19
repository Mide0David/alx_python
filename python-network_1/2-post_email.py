import requests
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: ./2-post_email.py <URL> <email>")

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)

print(f"Your email is: {email}")
print(response.text)
