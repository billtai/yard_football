from flask import current_app
import requests;


class MailHelper:
    def send_email(from_email:str, to_email: str, subject: str, content: str):
        return requests.post(
            f"https://api.mailgun.net/v3/{current_app.config['MAILGUN_DOMAIN_NAME']}/messages",
            auth = ("api", current_app.config['MAILGUN_API_KEY']),
            data = {
                "from": from_email,
                "to": to_email,
                "subject": subject,
                "html": content
            }
        )
