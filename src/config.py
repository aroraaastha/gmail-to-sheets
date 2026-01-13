# -------------------------------
# Google API Scopes
# -------------------------------
# Gmail API: read and modify emails
# Sheets API: read and write Google Sheets
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/spreadsheets"
]

# -------------------------------
# Google Sheets
# -------------------------------
# Replace this with your actual spreadsheet ID
SPREADSHEET_ID = "1WL90pc4yTuMbidBqO5I99Qro11RZkrQUX5xUyPj6E78"

# -------------------------------
# State file to prevent duplicates
# -------------------------------
# This file will store the last processed email ID
STATE_FILE = "state.txt"
