import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

print("Body response:")
print("\t- type: <class 'str'>")
print(f"\t- content: {response.text}")
