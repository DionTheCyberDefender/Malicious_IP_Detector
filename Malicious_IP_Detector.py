#Malicious_IP_Detector.py
#Malicious IP Detector

#Purpose: To receive the user's input of valid IP address and search the outcome via AbuseIPDB.
#This will search an IP's Malicious Score and attributes.

import requests
import json

#1 Ask user for the IP in question and remove Whitespace from str
ip_in_question = input("What is the IP in question? ").strip()
allowed_chars = "123456789."

#Convert the string to a float using float() and verify IP is in valid format (xxx.xxx.xxx.xxx)
try:
    float(ip_in_question)
    #If conversion is correct, check for valid IP (check for 3 dots)
    if ip_in_question.count(".") == 3:
        print("Thanks for providing the IP: ", ip_in_question)
    else:
        print("Error: Invalid IP format. Please Try Again")
        print("Enter a valid IP (Example: xxx.xxx.xxx.xxx)")
except ValueError:
    print("Thanks for providing the IP: ", ip_in_question)

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    'ipAddress': ip_in_question,
    'maxAgeInDays': '90'
}

headers = {
    'Accept': 'application/json',
    'Key': 'd5f8c5761fb0732c651498f58f7075baa6ebe4ae0795dfe86ca4ee4101f4a5c7d75a5ae1be5715ab'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)
print (json.dumps(decodedResponse, sort_keys=True, indent=4))

#Author: DionTheCyberDefender 
#DateOfCreation 5/5/2024