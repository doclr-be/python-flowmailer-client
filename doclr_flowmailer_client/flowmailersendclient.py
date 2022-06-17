import json
import requests

from flowmailermail import FlowMailerMail


class FlowMailerSendClient:

    def __init__(self, fm_account_id: str):
        self.fm_account_id = fm_account_id

    def send_mail(self, flow_mailer_mail: FlowMailerMail, token: str):
        url = "https://api.flowmailer.net/" + self.fm_account_id + '/messages/submit'

        headers = {'Accept': 'application/vnd.flowmailer.v1.10+json',
                   'Content-Type': 'application/vnd.flowmailer.v1.10+json',
                   'Authorization': 'Bearer ' + token
                   }

        payload = {
            'data': {'title': flow_mailer_mail.subject},
            'subject': flow_mailer_mail.subject,
            'flowSelector': flow_mailer_mail.flow_selector,
            'messageType': 'EMAIL',
            'recipientAddress': flow_mailer_mail.recipient_address,
            'senderAddress': flow_mailer_mail.sender_address,
            'attachments': flow_mailer_mail.attachments
        }

        response = requests.post(url=url, headers=headers, data=json.dumps(payload))

        print("mailresponse status: " + str(response.status_code))
