import base64
from googleapiclient.errors import HttpError

def parse_email(service, msg_id):
    """
    Parse a Gmail message given its message ID.
    Returns a dictionary with From, Subject, Date, and Content.
    """
    try:
        message = service.users().messages().get(
            userId="me",
            id=msg_id,
            format="full"
        ).execute()

        headers = message["payload"]["headers"]
        data = {"From": "", "Subject": "", "Date": "", "Content": ""}

        # Extract header values
        for header in headers:
            if header["name"] == "From":
                data["From"] = header["value"]
            elif header["name"] == "Subject":
                data["Subject"] = header["value"]
            elif header["name"] == "Date":
                data["Date"] = header["value"]

        # Extract body content (plain text)
        if "parts" in message["payload"]:
            # multipart email
            for part in message["payload"]["parts"]:
                if part["mimeType"] == "text/plain":
                    body = part["body"]["data"]
                    data["Content"] = base64.urlsafe_b64decode(body).decode("utf-8", errors="ignore")
        else:
            # single part email
            if "data" in message["payload"]["body"]:
                body = message["payload"]["body"]["data"]
                data["Content"] = base64.urlsafe_b64decode(body).decode("utf-8", errors="ignore")

        return data

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None
