# Gmail to Sheets Automation
Demo video link: https://drive.google.com/file/d/1HL9z28k_Zq9TeEGSQ2sd4rHFvV6tkfvT/view?usp=sharing

## Project Overview
This project automates fetching unread emails from Gmail and appending them to a Google Sheet.  
It uses the Gmail API to read emails and the Google Sheets API to store them.  
Duplicate prevention is implemented using a `state.txt` file, and emails are marked as read after processing.

---

## Features
- Fetch unread emails from Gmail
- Parse email details: From, Subject, Date, Content
- Append emails to Google Sheets
- Duplicate prevention with `state.txt`
- Handles long email content (truncated at 50,000 characters per cell)
- Batch processing for testing or large inboxes

---

## Project Structure

gmail-to-sheets/
├── credentials/ ← contains credentials.json (DO NOT COMMIT)
├── proof/ ← contains screenshots for submission
├── src/
│ ├── main.py ← main script
│ ├── gmail_service.py ← Gmail API functions
│ ├── email_parser.py ← Email parsing logic
│ └── sheets_service.py ← Google Sheets functions
├── venv/ ← virtual environment
├── requirements.txt ← Python dependencies
├── state.txt ← processed email IDs
└── README.md

yaml
Copy code

---

## Setup Instructions

1. Clone the repository:

```bash
git clone <your-repo-url>
cd gmail-to-sheets
Create a virtual environment:

powershell
Copy code
python -m venv venv
Activate the virtual environment:

powershell
Copy code
venv\Scripts\activate
Install required packages:

powershell
Copy code
pip install -r requirements.txt
Add your Google credentials:

Download credentials.json from Google Cloud Console

Place it in the credentials/ folder

How to Run
powershell
Copy code
python src\main.py
The first run will open the Google OAuth consent screen

Click Allow

The script will fetch unread emails, parse them, and append them to your Google Sheet

Emails will be marked as read and stored in state.txt to prevent duplicates

Screenshots (Proof)
proof/inbox.png → Gmail inbox showing unread emails

proof/oauth.png → OAuth consent screen

proof/sheet.png → Emails appended to Google Sheet

proof/oauth_token.png → Optional, showing token.pickle

Notes
Maximum 50,000 characters per cell in Google Sheets

Batch limit can be configured in main.py (BATCH_LIMIT)

state.txt prevents duplicates when rerunning the script

Credentials and token files should never be committed



Author AASTHA ARORA 
