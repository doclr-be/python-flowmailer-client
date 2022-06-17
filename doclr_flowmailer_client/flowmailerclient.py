from .flowmailerauthclient import FlowMailerAuthClient
from .flowmailermail import FlowMailerMail
from .flowmailersendclient import FlowMailerSendClient


class FlowMailerClient:
    def __init__(self, fm_client_id: str, fm_client_secret: str, fm_account_id: str):
        self.fm_auth_client = FlowMailerAuthClient(fm_client_id, fm_client_secret)
        self.fm_send_client = FlowMailerSendClient(fm_account_id)

    def send_mail(self, flow_mailer_mail: FlowMailerMail):
        token = self.fm_auth_client.get_token()
        self.fm_send_client.send_mail(flow_mailer_mail, token)
