# Example of generating an authorization URL

import requests

client_id = '773y1px3g1yhl0'
redirect_uri = 'WPL_AP1.c0prMqiM1E1xzxCN.SvWY1g=='
scope = 'r_liteprofile r_emailaddress'

auth_url = f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"

print("Go to this URL for authorization:")
print(auth_url)
