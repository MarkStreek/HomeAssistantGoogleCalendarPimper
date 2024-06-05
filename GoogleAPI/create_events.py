#!/usr/bin/env python3

__AUTHOR__ = "Mark Van de Streek"
__VERSION__ = "1.0.0"
__EMAIL__ = "mvdstreek2003@gmail.com"
__DATE__ = "2024-03-11"


def create_event(date_time, wind_speed, temperature):
    date = date_time.strftime("%Y-%m-%d")
    event = {
        'summary': f"🌡️ {temperature} °C️, 💨 {wind_speed} km/h",
        'description': 'Temperatuur en windsnelheid op ' + date_time.strftime("%H:%M:%S"),
        'start': {
            'date': date,
            'timeZone': 'Europe/Amsterdam',
        },
        'end': {
            'date': date,
            'timeZone': 'Europe/Amsterdam',
        },
    }

    return event
