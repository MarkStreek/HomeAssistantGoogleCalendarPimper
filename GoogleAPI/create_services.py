#!/usr/bin/env python3

__AUTHOR__ = "Mark Van de Streek"
__VERSION__ = "1.0.0"
__EMAIL__ = "mvdstreek2003@gmail.com"
__DATE__ = "2024-03-11"

import os.path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If you are modifying these scopes, delete the file token.json and reload the application.
SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/tasks']
# Location of the service account file
SERVICE_ACCOUNT_FILE = "data/creds.json"


def create_creds():
    """
    Function that creates the credentials to authenticate the application.
    The credentials are stored in a file called creds.json.
    :return: The credentials to authenticate the application.
    """
    creds = None
    if os.path.exists(SERVICE_ACCOUNT_FILE):
        creds = (service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        ))

    return creds


def create_calendar_service(creds):
    """
    Small function that creates an instance of the Google Calendar API.
    This service is the connection between the application and the Google Calendar API.
    Therefore, this service is used to create, update, and delete events in the calendar.
    :param creds: The credentials to authenticate the application.
    :return: The service to interact with the Google Calendar API.
    """
    try:
        service_calendar = build("calendar", "v3", credentials=creds)
        return service_calendar
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


def create_task_service(creds):
    """
    Currently not used, but future-proofing the application.
    This function creates a service for the Google Tasks API.
    A task is different from an event. An event is a calendar item, while a task is a to-do item.
    """
    try:
        service_tasks = build("tasks", "v1", credentials=creds)
        return service_tasks
    except HttpError as error:
        print(f"An error occurred: {error}")
