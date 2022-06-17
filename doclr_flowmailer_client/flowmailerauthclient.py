import requests


class FlowMailerAuthClient:

    def __init__(self, fm_client_id: str, fm_client_secret: str):
        self.fm_client_id = fm_client_id
        self.fm_client_secret = fm_client_secret

    def get_token(self):
        url = "https://login.flowmailer.net/oauth/token"

        headers = {'Accept': 'application/vnd.flowmailer.v1.10+json',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

        payload = {'client_id': self.fm_client_id,
                   'client_secret': self.fm_client_secret,
                   'grant_type': 'client_credentials',
                   'scope': 'api'
                   }

        response = requests.post(url=url, headers=headers, data=payload)

        print("authresponse status: " + str(response.status_code))
        data = response.json()

        return data['access_token']
