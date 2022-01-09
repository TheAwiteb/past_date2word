from datetime import datetime
from typing import Optional


def get_word(key: str, number: int, lang: str) -> str:
    number = int(number)
    date_dict = {
        "en": {
            "second": "second" if number <= 1 else "seconds",
            "minute": "minute" if number <= 1 else "minutes",
            "hour": "hour" if number <= 1 else "hours",
            "day": "day" if number <= 1 else "days",
            "week": "week" if number <= 1 else "weeks",
            "month": "month" if number <= 1 else "months",
            "year": "year" if number <= 1 else "years",
        },
        "ar": {
            "second": "ثانية" if number == 1 or number > 10 else "ثانيتين" if number == 2 else "ثواني",
            "minute": "دقيقة" if number == 1 or number > 10 else "دقيقتين" if number == 2 else "دقائق",
            "hour": "ساعة" if number == 1 or number > 10 else "ساعتين" if number == 2 else "ساعات",
            "day": "يوم" if number == 1 or number > 10 else "يومين" if number == 2 else "ايام",
            "week": "اسبوع" if number == 1 or number > 10 else "اسبوعين" if number == 2 else "اسابيع",
            "month": "شهر" if number == 1 or number > 10 else "شهرين" if number == 2 else "شهور",
            "year": "سنة" if number == 1 or number > 10 else "سنتين" if number == 2 else "سنين",
        },
    }
    return f"{number} {date_dict.get(lang, {...:...}).get(key)}" if number not in [1,2] else date_dict.get(lang, {...:...}).get(key)


def past_date2word(date: datetime) -> Optional[str]:
    timestamp_ago = date.timestamp()
    timestamp = datetime.now().timestamp()
    
    if (second := timestamp - timestamp_ago) > 0:
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)
        day, hour = divmod(hour, 24)
        week, day = divmod(day, 7)
        month, week = divmod(week, 4)
        year, month = divmod(month, 12)
        for time_name in (
            time_list := ["year", "month", "week", "day", "hour", "minute", "second"]
        ):
            time = locals().get(time_name)
            if time > 0:
                if time_name != "second":
                    next_time_name = time_list[time_list.index(time_name) + 1]
                    next_time_val = locals().get(next_time_name)
                    next_time = (
                        f"and {get_word(next_time_name, next_time_val)} "
                        if int(next_time_val) > 0
                        else ""
                    )
                else:
                    next_time = ""
                    next_time_val = 0
                return f"{get_word(time_name, time)} {next_time}ago"
    else:
        return None
