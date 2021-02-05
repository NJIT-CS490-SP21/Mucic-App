import requests
import os
from dotenv import load_dotenv, find_dotenv

############################################# Authorization ####################################################
load_dotenv(find_dotenv()) 
AUTH_URL= "https://accounts.spotify.com/api/token" #url for authentication

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")


auth_response = requests.post(AUTH_URL,
{
    'grant_type': 'client_credentials',
    'client_id' :clientID,
    'client_secret' : clientSecret,
}
)
auth_response_data = auth_response.json()
auth_token = auth_response_data["access_token"]
header = {
 'Authorization': 'Bearer {token}'.format(token=auth_token)
 }
################################################################################################################