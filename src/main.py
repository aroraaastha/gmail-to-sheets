from gmail_service import get_gmail_service, fetch_unread_emails
from email_parser import parse_email
from sheets_service import get_sheets_service, append_row
from config import SPREADSHEET_ID, STATE_FILE
import os

# ----------------------------
# Constants
# ----------------------------
MAX_CELL_LENGTH = 50000  # Google Sheets cell limit
BATCH_LIMIT = 10         # Number of emails to process per run (adjust for testing)

# ----------------------------
# Gmail: Fetch unread emails
# ----------------------------
service = get_gmail_service()
messages = fetch_unread_emails(service)
print(f"Unread emails found: {len(messages)}")

# ----------------------------
# Google Sheets: Setup service
# ----------------------------
sheets_service = get_sheets_service()

# ----------------------------
# Load processed email IDs
# ----------------------------
processed_ids = set()
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        processed_ids = set(line.strip() for line in f.readlines())

# ----------------------------
# Function to mark email as read
# ----------------------------
def mark_as_read(service, msg_id):
    service.users().messages().modify(
        userId="me",
        id=msg_id,
        body={"removeLabelIds": ["UNREAD"]}
    ).execute()

# ----------------------------
# Process and append emails
# ----------------------------
new_ids = set()

for msg in messages[:BATCH_LIMIT]:  # Process only first BATCH_LIMIT emails
    msg_id = msg["id"]

    # Skip already processed emails
    if msg_id in processed_ids:
        continue

    data = parse_email(service, msg_id)
    if data:
        # Truncate content to avoid Google Sheets 50,000 char limit
        content = data["Content"]
        if len(content) > MAX_CELL_LENGTH:
            content = content[:MAX_CELL_LENGTH]

        # Append to Google Sheets
        append_row(
            sheets_service,
            SPREADSHEET_ID,
            [data["From"], data["Subject"], data["Date"], content]
        )

        # Mark email as read in Gmail
        mark_as_read(service, msg_id)

        # Add to processed IDs
        new_ids.add(msg_id)

        print(f"Appended: {data['Subject']}")

# ----------------------------
# Update state file
# ----------------------------
if new_ids:
    with open(STATE_FILE, "a") as f:
        for msg_id in new_ids:
            f.write(msg_id + "\n")
