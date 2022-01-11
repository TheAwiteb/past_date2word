from past_date2word import past_date2word
from datetime import datetime, timedelta


def test_second_en():
    time = datetime.now() - timedelta(seconds=1)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 second ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 second"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 second ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 second"
    )

    time = datetime.now() - timedelta(seconds=23)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "23 seconds ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "23 seconds"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "23 seconds ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "23 seconds"
    )


def test_minute_en():
    time = datetime.now() - timedelta(minutes=1)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 minute ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 minute"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 minute ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 minute"
    )

    time = datetime.now() - timedelta(minutes=1, seconds=1)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 minute and 1 second ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 minute and 1 second"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 minute ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 minute"
    )

    time = datetime.now() - timedelta(minutes=13)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "13 minutes ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "13 minutes"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "13 minutes ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "13 minutes"
    )

    time = datetime.now() - timedelta(minutes=9, seconds=34)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "9 minutes and 34 seconds ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "9 minutes and 34 seconds"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "9 minutes ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "9 minutes"
    )


def test_hour_en():
    time = datetime.now() - timedelta(hours=1)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 hour ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 hour"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 hour ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 hour"
    )

    time = datetime.now() - timedelta(hours=1, minutes=1)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 hour and 1 minute ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 hour and 1 minute"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 hour ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 hour"
    )

    time = datetime.now() - timedelta(hours=22)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "22 hours ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "22 hours"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "22 hours ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "22 hours"
    )

    time = datetime.now() - timedelta(hours=12, minutes=44)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "12 hours and 44 minutes ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "12 hours and 44 minutes"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "12 hours ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "12 hours"
    )


def test_day_en():
    time = datetime.now() - timedelta(days=1)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 day ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 day"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 day ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 day"
    )

    time = datetime.now() - timedelta(days=1, hours=1)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 day and 1 hour ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 day and 1 hour"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 day ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 day"
    )

    time = datetime.now() - timedelta(days=6)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "6 days ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "6 days"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "6 days ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "6 days"
    )

    time = datetime.now() - timedelta(days=5, hours=15)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "5 days and 15 hours ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "5 days and 15 hours"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "5 days ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "5 days"
    )


def test_week_en():
    time = datetime.now() - timedelta(weeks=1)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 week ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 week"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 week ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 week"
    )

    time = datetime.now() - timedelta(weeks=1, days=1)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 week and 1 day ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 week and 1 day"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 week and 1 day ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 week and 1 day"
    )

    time = datetime.now() - timedelta(weeks=3)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "3 weeks ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "3 weeks"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "3 weeks ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "3 weeks"
    )

    time = datetime.now() - timedelta(weeks=2, days=4)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "2 weeks and 4 days ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "2 weeks and 4 days"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "2 weeks and 4 days ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "2 weeks and 4 days"
    )


def test_month_en():
    # 4 weeks == 1 month
    one_month_to_week = 4 * 1

    time = datetime.now() - timedelta(weeks=one_month_to_week)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 month ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 month"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 month ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 month"
    )

    time = datetime.now() - timedelta(weeks=one_month_to_week + 1)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 month and 1 week ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 month and 1 week"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 month and 1 week ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 month and 1 week"
    )

    time = datetime.now() - timedelta(weeks=one_month_to_week * 2)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "2 months ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "2 months"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "2 months ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "2 months"
    )

    time = datetime.now() - timedelta(weeks=(one_month_to_week * 3) + 2)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "3 months and 2 weeks ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "3 months and 2 weeks"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "3 months and 2 weeks ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "3 months and 2 weeks"
    )


def test_year_en():
    # 12 month == 1 year
    # 4 weeks == 1 month
    one_month_to_week = 4 * 1
    one_year_to_week = one_month_to_week * 12

    time = datetime.now() - timedelta(weeks=one_year_to_week)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 year ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 year"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 year ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 year"
    )

    time = datetime.now() - timedelta(weeks=one_year_to_week + one_month_to_week)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "1 year and 1 month ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "1 year and 1 month"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "1 year and 1 month ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "1 year and 1 month"
    )

    time = datetime.now() - timedelta(weeks=one_year_to_week * 4)
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "4 years ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "4 years"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "4 years ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "4 years"
    )

    time = datetime.now() - timedelta(
        weeks=(one_year_to_week * 12) + (one_month_to_week * 5)
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=True)
        == "12 years and 5 months ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=True)
        == "12 years and 5 months"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=True, long_text=False)
        == "12 years and 5 months ago"
    )
    assert (
        past_date2word(date=time, language="en", with_ago=False, long_text=False)
        == "12 years and 5 months"
    )


def test_second_ar():
    time = datetime.now() - timedelta(seconds=1)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ ثانية"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "ثانية"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ ثانية"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "ثانية"
    )

    time = datetime.now() - timedelta(seconds=2)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ ثانيتين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "ثانيتين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ ثانيتين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "ثانيتين"
    )

    time = datetime.now() - timedelta(seconds=5)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 5 ثواني"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "5 ثواني"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 5 ثواني"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "5 ثواني"
    )

    time = datetime.now() - timedelta(seconds=13)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 13 ثانية"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "13 ثانية"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 13 ثانية"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "13 ثانية"
    )


def test_minute_ar():
    time = datetime.now() - timedelta(minutes=1)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ دقيقة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "دقيقة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ دقيقة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "دقيقة"
    )

    time = datetime.now() - timedelta(minutes=1, seconds=1)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ دقيقة وثانية"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "دقيقة وثانية"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ دقيقة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "دقيقة"
    )

    time = datetime.now() - timedelta(minutes=2, seconds=2)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ دقيقتين وثانيتين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "دقيقتين وثانيتين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ دقيقتين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "دقيقتين"
    )

    time = datetime.now() - timedelta(minutes=5, seconds=5)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 5 دقائق و 5 ثواني"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "5 دقائق و 5 ثواني"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 5 دقائق"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "5 دقائق"
    )
    time = datetime.now() - timedelta(minutes=13, seconds=13)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 13 دقيقة و 13 ثانية"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "13 دقيقة و 13 ثانية"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 13 دقيقة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "13 دقيقة"
    )


def test_hour_ar():

    time = datetime.now() - timedelta(hours=1)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ ساعة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "ساعة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ ساعة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "ساعة"
    )

    time = datetime.now() - timedelta(hours=1, minutes=1)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ ساعة ودقيقة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "ساعة ودقيقة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ ساعة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "ساعة"
    )

    time = datetime.now() - timedelta(hours=2, minutes=2)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ ساعتين ودقيقتين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "ساعتين ودقيقتين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ ساعتين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "ساعتين"
    )

    time = datetime.now() - timedelta(hours=5, minutes=5)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 5 ساعات و 5 دقائق"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "5 ساعات و 5 دقائق"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 5 ساعات"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "5 ساعات"
    )

    time = datetime.now() - timedelta(hours=13, minutes=13)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 13 ساعة و 13 دقيقة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "13 ساعة و 13 دقيقة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 13 ساعة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "13 ساعة"
    )


def test_day_ar():
    time = datetime.now() - timedelta(days=1)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ يوم"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "يوم"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ يوم"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "يوم"
    )

    time = datetime.now() - timedelta(days=1, hours=1)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ يوم وساعة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "يوم وساعة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ يوم"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "يوم"
    )

    time = datetime.now() - timedelta(days=2, hours=2)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ يومين وساعتين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "يومين وساعتين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ يومين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "يومين"
    )

    time = datetime.now() - timedelta(days=5, hours=5)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 5 ايام و 5 ساعات"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "5 ايام و 5 ساعات"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 5 ايام"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "5 ايام"
    )

    time = datetime.now() - timedelta(days=6, hours=15)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 6 ايام و 15 ساعة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "6 ايام و 15 ساعة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 6 ايام"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "6 ايام"
    )


def test_week_ar():

    time = datetime.now() - timedelta(weeks=1)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ اسبوع"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "اسبوع"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ اسبوع"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "اسبوع"
    )

    time = datetime.now() - timedelta(weeks=1, days=1)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ اسبوع ويوم"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "اسبوع ويوم"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ اسبوع ويوم"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "اسبوع ويوم"
    )

    time = datetime.now() - timedelta(weeks=2, days=2)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ اسبوعين ويومين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "اسبوعين ويومين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ اسبوعين ويومين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "اسبوعين ويومين"
    )

    time = datetime.now() - timedelta(weeks=3, days=4)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 3 اسابيع و 4 ايام"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "3 اسابيع و 4 ايام"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 3 اسابيع و 4 ايام"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "3 اسابيع و 4 ايام"
    )


def test_month_ar():
    one_month_to_week = 4 * 1

    time = datetime.now() - timedelta(weeks=one_month_to_week)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ شهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "شهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ شهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "شهر"
    )

    time = datetime.now() - timedelta(weeks=one_month_to_week + 1)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ شهر واسبوع"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "شهر واسبوع"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ شهر واسبوع"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "شهر واسبوع"
    )

    time = datetime.now() - timedelta(weeks=one_month_to_week * 2)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ شهرين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "شهرين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ شهرين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "شهرين"
    )

    time = datetime.now() - timedelta(weeks=(one_month_to_week * 3) + 2)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 3 اشهر واسبوعين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "3 اشهر واسبوعين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 3 اشهر واسبوعين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "3 اشهر واسبوعين"
    )

    time = datetime.now() - timedelta(weeks=(one_month_to_week * 11) + 3)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 11 شهر و 3 اسابيع"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "11 شهر و 3 اسابيع"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 11 شهر و 3 اسابيع"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "11 شهر و 3 اسابيع"
    )


def test_year_ar():
    # 12 month == 1 year
    # 4 weeks == 1 month
    one_month_to_week = 4 * 1
    one_year_to_week = one_month_to_week * 12

    time = datetime.now() - timedelta(weeks=one_year_to_week)
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ سنة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "سنة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ سنة"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "سنة"
    )

    time = datetime.now() - timedelta(
        weeks=(one_year_to_week) + (one_month_to_week * 1)
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ سنة وشهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "سنة وشهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ سنة وشهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "سنة وشهر"
    )

    time = datetime.now() - timedelta(
        weeks=(one_year_to_week * 2) + (one_month_to_week * 2)
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ سنتين وشهرين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "سنتين وشهرين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ سنتين وشهرين"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "سنتين وشهرين"
    )

    time = datetime.now() - timedelta(
        weeks=(one_year_to_week * 5) + (one_month_to_week * 5)
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 5 سنين و 5 اشهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "5 سنين و 5 اشهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 5 سنين و 5 اشهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "5 سنين و 5 اشهر"
    )

    time = datetime.now() - timedelta(
        weeks=(one_year_to_week * 12) + (one_month_to_week * 5)
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=True)
        == "منذ 12 سنة و 5 اشهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=True)
        == "12 سنة و 5 اشهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=True, long_text=False)
        == "منذ 12 سنة و 5 اشهر"
    )
    assert (
        past_date2word(date=time, language="ar", with_ago=False, long_text=False)
        == "12 سنة و 5 اشهر"
    )
