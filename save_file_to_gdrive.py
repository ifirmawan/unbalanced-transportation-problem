import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace the API key below with a valid API key.
API_KEY = os.environ.get("GOOGLE_API_KEY")

def save_file_to_drive(file_name, file_content):
  try:
    service = build('drive', 'v3', developerKey=API_KEY)
    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_content, mimetype='text/plain')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(F'File ID: {file.get("id")}')
  except HttpError as error:
    print(F'An error occurred: {error}')
    file = None
  return file

# Save the file to your Google Drive
save_file_to_drive('transportation_problem.py', 'Your code goes here')

