import datetime
import pytz
from time import sleep


class TimeOfTimezone:
    def __init__(self, continent):
        self.continent = continent

    def time_of_different_zone(self):
        a = {
            'Cairo': 'Africa/Cairo',
            'Chicago': 'America/Chicago',
            'Costa Rica': 'America/Costa_Rica',
            'Los Angeles': 'America/Los_Angeles',
            'Mexico City': 'America/Mexico_City',
            'New York': 'America/New_York',
            'Panama': 'America/Panama',
            'Bankok': 'Asia/Bangkok',
            'India': 'Asia/Calcutta',
            'Dubai': 'Asia/Dubai',
            'Hon Kong': 'Asia/Hong_Kong',
            'Kuwait': 'Asia/Kuwait',
            'Singapore': 'Asia/Singapore',
            'Japan': 'Asia/Tokyo',
            'Melbourne': 'Australia/Melbourne',
            'Sydney': 'Australia/Sydney',
            'Canada': 'Canada/Central',
            'Germany': 'Europe/Berlin',
            'England': 'Europe/London',
            'Luxembourg': 'Europe/Luxembourg',
            'Moscow': 'Europe/Moscow',
            'Rome': 'Europe/Rome',
            'Alaska': 'US/Alaska',
            'Poland': 'Poland'
        }

        d = datetime.datetime.now(tz=pytz.timezone(a[self.continent]))
        am_time = datetime.datetime.combine(d.date(), d.time())

        weekday = 5 - am_time.weekday()
        if weekday == 0:
            weekday = 7
        elif weekday == -1:
            weekday = 6
        else:
            pass

        timetuple = am_time.timetuple()
        next_day = timetuple[2] + weekday
        next_weekend = datetime.datetime(am_time.year, am_time.month, next_day)

        remaining = (next_weekend - am_time)
        return remaining


if __name__ == '__main__':
    pass
