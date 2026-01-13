from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import SPREADSHEET_ID, SCOPES
from gmail_service import get_gmail_service

def get_sheets_service():
    """
    Returns an authorized Google Sheets API service.
    """
    # Reuse Gmail credentials for Sheets API
    service = get_gmail_service()
    sheets_service = build("sheets", "v4", credentials=service._http.credentials)
    return sheets_service

def append_row(sheet_service, spreadsheet_id, row):
    """
    Appends a row (list) to the first sheet of the spreadsheet.
    """
    try:
        body = {"values": [row]}
        result = sheet_service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,  # use spreadsheet ID
            range="Sheet1!A:D",
            valueInputOption="RAW",
            body=body
        ).execute()
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None
