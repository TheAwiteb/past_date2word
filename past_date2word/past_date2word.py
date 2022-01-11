from datetime import datetime
from enum import Enum
from typing import Optional


class Language(Enum):
    ar = "ar"
    en = "en"


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
            "second": "ثانية"
            if number == 1 or number > 10
            else "ثانيتين"
            if number == 2
            else "ثواني",
            "minute": "دقيقة"
            if number == 1 or number > 10
            else "دقيقتين"
            if number == 2
            else "دقائق",
            "hour": "ساعة"
            if number == 1 or number > 10
            else "ساعتين"
            if number == 2
            else "ساعات",
            "day": "يوم"
            if number == 1 or number > 10
            else "يومين"
            if number == 2
            else "ايام",
            "week": "اسبوع"
            if number == 1 or number > 10
            else "اسبوعين"
            if number == 2
            else "اسابيع",
            "month": "شهر"
            if number == 1 or number > 10
            else "شهرين"
            if number == 2
            else "اشهر",
            "year": "سنة"
            if number == 1 or number > 10
            else "سنتين"
            if number == 2
            else "سنين",
        },
    }
    return (
        date_dict.get(lang, {}).get(key)
        if (number in [1, 2] and lang == "ar")
        else f"{number} {date_dict.get(lang, {}).get(key)}"
    )


def past_date2word(
    date: datetime,
    language: str = "en",
    with_ago: bool = True,
    long_sentence: bool = True,
) -> Optional[str]:
    """تحويل التاريخ الماضي الى نص

    المعطيات:
        date (datetime): The date
        language (str, optional): Language of the sentence. Avaliable:
                    [Arabic<'`ar`'>, English<'`en`'>]. \n
                    Defaults to 'en'.
        with_ago (bool, optional): With "`ago`" at the end of the sentence. Defaults to True.
        long_sentence (bool, optional): Add the hours, minutes and seconds in the sentence. Defaults to True.

    المخرجات:
        Optional[str]: The `date` as a sentence or `None` if it not in past
    """
    timestamp_ago = date.timestamp()
    timestamp = datetime.now().timestamp()
    language = Language(language).name
    if (second := timestamp - timestamp_ago) > 0:
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)
        day, hour = divmod(hour, 24)
        week, day = divmod(day, 7)
        month, week = divmod(week, 4)
        year, month = divmod(month, 12)

        and_word = "and" if language == "en" else "و"
        ago_word = " ago" if language == "en" else "منذ "

        for idx, time_name in enumerate(
            time_list := ["year", "month", "week", "day", "hour", "minute", "second"]
        ):
            time = int(locals().get(time_name))
            if time > 0:
                # Take the first value greater than zero
                with_second_word = (
                    time_name != "second"
                    and (second_time := int(locals().get(time_list[idx + 1]))) > 0
                )
                first_word = get_word(time_name, time, language)
                second_word = (
                    f"{get_word(time_list[idx + 1], second_time, language)}"
                    if with_second_word
                    else ""
                )
                full_word = first_word
                if (
                    (not long_sentence) and (time_name in ["day", "hour", "minute"])
                ) or (not with_second_word):
                    pass
                else:
                    if language == "ar":
                        full_word += f" {and_word}{'' if second_word.isalpha() else ' '}{second_word}"
                    else:
                        full_word += f" {and_word} {second_word}"
                if with_ago:
                    if language == "ar":
                        full_word = ago_word + full_word
                    else:
                        full_word = full_word + ago_word
                return full_word
    else:
        return None
