#!/usr/bin/env python3

__AUTHOR__ = "Mark Van de Streek"
__VERSION__ = "1.0.0"
__EMAIL__ = "mvdstreek2003@gmail.com"
__DATE__ = "2024-03-11"

import requests
import bearer_authentication
import datetime


def get_temperature(PREFERENCES):
    temperature = requests.get(
        PREFERENCES['url'] + PREFERENCES['temperature_device'],
        auth=bearer_authentication.BearerAuth(PREFERENCES['token'])
    ).json()

    return temperature['state']


def get_wind_speed(PREFERENCES):
    """
    Function that retrieves the wind speed of all states until the current date, 06:00 am.
    :param PREFERENCES: The preferences from the preferences.json file.
    :return: The wind speeds of all states until the current date, 06:00 am.
    """
    current_date = datetime.date.today()
    date_string = current_date.strftime("%Y-%m-%d")
    url = PREFERENCES['url'] + PREFERENCES['wind_states_average']
    url = url.replace('XXXXXX', date_string)

    wind_speed = requests.get(
        url,
        auth=bearer_authentication.BearerAuth(PREFERENCES['token'])
    ).json()

    return calculate_average_wind_speed(wind_speed)


def calculate_average_wind_speed(wind_speed):
    """
    Function that calculates the average wind speed of all states.
    It sums all states and divides it by the number of states.
    :param wind_speed: The wind speeds of all states until the current date, 06:00 am.
    :return: Average wind speed of all states.
    """
    all_states = [float(wind_speed[0][i]['state']) for i in range(1, len(wind_speed[0]))]
    total_sum = sum(all_states)
    counter = len(all_states)
    average_wind_speed = round(total_sum / counter, 2)

    return average_wind_speed
