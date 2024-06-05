#!/usr/bin/env python3

__AUTHOR__ = "Mark Van de Streek"
__VERSION__ = "1.0.0"
__EMAIL__ = "mvdstreek2003@gmail.com"
__DATE__ = "2024-03-11"

import datetime
import create_services
import create_events
import json
import homeassistant_requests

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/tasks']
PREFERENCES = json.load(open("preferences.json", "r"))


def main():
    """
    Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # 1 - Create credentials / token
    creds = create_services.create_creds()
    # 2 - Create Calendar service
    service_calendar = create_services.create_calendar_service(creds)
    # 3 - Create Task service
    service_tasks = create_services.create_task_service(creds)
    # 4 - Retrieve data from Home Assistant
    temperature = homeassistant_requests.get_temperature(PREFERENCES)
    average_wind_speed = homeassistant_requests.get_wind_speed(PREFERENCES)

    # 5 - Create event
    date_time = datetime.datetime.now()
    body = create_events.create_event(date_time, temperature=temperature, wind_speed=average_wind_speed)

    event = (service_calendar
             .events()
             .insert(calendarId="mvdstreek2003@gmail.com", body=body)
             .execute())

    print("Event created: %s" % (event.get('htmlLink')))


if __name__ == "__main__":
    main()
