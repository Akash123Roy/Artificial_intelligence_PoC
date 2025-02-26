import requests

# Your LinkedIn App credentials
client_id = '773y1px3g1yhl0'
client_secret = 'WPL_AP1.c0prMqiM1E1xzxCN.SvWY1g=='

# LinkedIn access token URL
url = 'https://www.linkedin.com/oauth/v2/accessToken'

# Payload to be sent in the POST request
payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

# Headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Send the POST request to obtain the access token
response = requests.post(url, data=payload, headers=headers)

# Check for successful request
if response.status_code == 200:
    access_token = response.json().get('access_token')
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to get access token. Status code: {response.status_code}")
    print(f"Error message: {response.json()}")
