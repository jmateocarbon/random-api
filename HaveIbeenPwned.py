import requests
import config
import pyhibp
from pyhibp import pwnedpasswords as pw

#Please use COnfig file

#print("1 - Company Breach \n2 - Password Breach \n3 - Email Address breach")
#input_choice = input("Please enter Options: ")

input_breach = input("Input Company: ")
input_password = input("Input Password: ")
input_email =  input("Input Email Address: ")
# Required: A descriptive user agent must be set describing the application consuming
#   the HIBP API
pyhibp.set_user_agent(ua="Mateo Test")

resp3 = pyhibp.get_single_breach(breach_name=input_breach)
print(resp3)


resp = pw.is_password_breached(password=input_password)
if resp:
	print("Password breached!")
	print("This password was used {0} time(s) before.".format(resp))

HIBP_API_KEY = config.HIBP_key

if HIBP_API_KEY:
		#Have I been pwned Key
	pyhibp.set_api_key(key=HIBP_API_KEY)
 
		#Email pastes on other website
	email_resp = pyhibp.get_pastes(email_address=input_email)
	print(email_resp)

		#Breaches affecting your account
	affect_breaches = pyhibp.get_account_breaches(account=input_email, truncate_response=True)
	print(affect_breaches)

# Get data classes in the HIBP system
#resp1 = pyhibp.get_data_classes()

# Get all breach information
#res2 = pyhibp.get_all_breaches()
#print(res2)

# Get a single breach
#resp3 = pyhibp.get_single_breach(breach_name=input_breach)
#print(resp3)

# An API key is required for calls which search by email address
#   (so get_pastes/get_account_breaches)
# See <https://haveibeenpwned.com/API/Key>
