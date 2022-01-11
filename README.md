# past_date2word

<p align="center">
  <a href="https://pypi.org/project/past_date2word/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/past_date2word?color=9cf">
  </a>
  <a href="https://pypi.org/project/past_date2word/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/past_date2word?color=9cf">
  </a>
  <a href="https://www.gnu.org/licenses/gpl-3.0.html">
    <img src="https://img.shields.io/pypi/l/quran-suras?color=9cf&label=License" alt="License">
  </a>
  <a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
  <a href="https://github.com/TheAwiteb/past_date2word/actions/workflows/python-app.yml">
    <img alt="past_date2word-test" src="https://github.com/TheAwiteb/past_date2word/actions/workflows/python-app.yml/badge.svg">
  </a>
</p>

past_date2word is library helps you to convert the past date to text

* [Requirements](#Requirements)
* [Installation](#Installation)
* [Examples](#Examples)

  * [English](#English)
    * [Seconds](#Seconds-EN)
    * [Minutes](#Minutes-EN)
    * [Hours](#Hours-EN)
    * [Days](#Days-EN)
    * [Weeks](#Weeks-EN)
    * [Months](#Months-EN)
    * [Years](#Years-EN)
  * [Arabic](#Arabic)
    * [Seconds](#Seconds-AR)
    * [Minutes](#Minutes-AR)
    * [Hours](#Hours-AR)
    * [Days](#Days-AR)
    * [Weeks](#Weeks-AR)
    * [Months](#Months-AR)
    * [Years](#Years-AR)

* [License](#License)

***
## Requirements

* **[python3.8](https://www.python.org/downloads/) +**
* **[git](https://git-scm.com/)**
* **[pip3](https://pip.pypa.io/en/stable/installation/)**

***

## Installation

Use [PyPi](https://pypi.org) to install past_date2word.

```bash
pip3 install past_date2word
```

***
## Example

> NOTE: Not all cases will be written because they are many, do not worry, you can see the [tests file](tests/test_past_date2word.py) that contains all the possible cases (**if you think otherwise, add the test and do a PR, we will be happy with that**)

> NOTE: `with_ago` parameter will add `"ago"` to the end of the sentence if its `True`, and if not, he will not add it

> NOTE: `long_sentence` parameter will add the hours, minutes and seconds to the sentence if its `True`, and if not, he will not add it

### English

#### Seconds EN
```python
time = datetime.now() - timedelta(seconds=1)

assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=True)
    == "1 second" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=False)
    == "1 second ago" # Output of past_date2word
)
```
**[[Back To Top 🔝]](#past_date2word)**

#### Minutes EN
```python
time = datetime.now() - timedelta(minutes=9, seconds=34)

assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=True)
    == "9 minutes and 34 seconds ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=True)
    == "9 minutes and 34 seconds" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=False)
    == "9 minutes ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=False)
    == "9 minutes" # Output of past_date2word
)
```

**[[Back To Top 🔝]](#past_date2word)**

#### Hours EN
```python
time = datetime.now() - timedelta(hours=12, minutes=44)

assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=True)
    == "12 hours and 44 minutes ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=True)
    == "12 hours and 44 minutes" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=False)
    == "12 hours ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=False)
    == "12 hours" # Output of past_date2word
)
```

**[[Back To Top 🔝]](#past_date2word)**

#### Days EN
```python
time = datetime.now() - timedelta(days=5, hours=15)

assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=True)
    == "5 days and 15 hours ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=True)
    == "5 days and 15 hours" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=False)
    == "5 days ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=False)
    == "5 days" # Output of past_date2word
)
```

**[[Back To Top 🔝]](#past_date2word)**

#### Weeks EN
```python
time = datetime.now() - timedelta(weeks=2, days=4)

assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=True)
    == "2 weeks and 4 days ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=True)
    == "2 weeks and 4 days" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=False)
    == "2 weeks and 4 days ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=False)
    == "2 weeks and 4 days" # Output of past_date2word
)
```

**[[Back To Top 🔝]](#past_date2word)**

#### Months EN
```python
# 4 weeks == 1 month
one_month_to_week = 4 * 1

time = datetime.now() - timedelta(weeks=(one_month_to_week * 3) + 2)

assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=True)
    == "3 months and 2 weeks ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=True)
    == "3 months and 2 weeks" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=False)
    == "3 months and 2 weeks ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=False)
    == "3 months and 2 weeks" # Output of past_date2word
)
```

**[[Back To Top 🔝]](#past_date2word)**

#### Years EN
```python
# 12 month == 1 year
# 4 weeks == 1 month
one_month_to_week = 4 * 1
one_year_to_week = one_month_to_week * 12

time = datetime.now() - timedelta(
    weeks=(one_year_to_week * 12) + (one_month_to_week * 5)
)

assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=True)
    == "12 years and 5 months ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=True)
    == "12 years and 5 months" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=True, long_sentence=False)
    == "12 years and 5 months ago" # Output of past_date2word
)
assert (
    past_date2word(date=time, language="en", with_ago=False, long_sentence=False)
    == "12 years and 5 months" # Output of past_date2word
)
```

**[[Back To Top 🔝]](#past_date2word)**

### Arabic

#### Seconds AR
```python
time = datetime.now() - timedelta(seconds=13)

print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=False)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=False)
)
```
<div dir="rtl">
المخرجات

```
"منذ 13 ثانية"
"13 ثانية"
"منذ 13 ثانية"
"13 ثانية"
```

</div>

**[[Back To Top 🔝]](#past_date2word)**

#### Minutes AR
```python
time = datetime.now() - timedelta(minutes=13, seconds=13)

print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=False)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=False)
)
```
<div dir="rtl">
المخرجات

```
"منذ 13 دقيقة و 13 ثانية"
"13 دقيقة و 13 ثانية"
"منذ 13 دقيقة"
"13 دقيقة"
```

</div>

**[[Back To Top 🔝]](#past_date2word)**

#### Hours AR
```python
time = datetime.now() - timedelta(hours=13, minutes=13)

print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=False)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=False)
)
```
<div dir="rtl">
المخرجات

```
"منذ 13 ساعة و 13 دقيقة"
"13 ساعة و 13 دقيقة"
"منذ 13 ساعة"
"13 ساعة"
```

</div>

**[[Back To Top 🔝]](#past_date2word)**

#### Days AR
```python
time = datetime.now() - timedelta(days=6, hours=15)

print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=False)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=False)
)
```
<div dir="rtl">
المخرجات

```
"منذ 6 ايام و 15 ساعة"
"6 ايام و 15 ساعة"
"منذ 6 ايام"
"6 ايام"
```

</div>

**[[Back To Top 🔝]](#past_date2word)**

#### Weeks AR
```python
time = datetime.now() - timedelta(weeks=3, days=4)

print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=False)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=False)
)
```
<div dir="rtl">
المخرجات

```
"منذ 3 اسابيع و 4 ايام"
"3 اسابيع و 4 ايام"
"منذ 3 اسابيع و 4 ايام"
"3 اسابيع و 4 ايام"
```

</div>

**[[Back To Top 🔝]](#past_date2word)**

#### Months AR
```python
one_month_to_week = 4 * 1


time = datetime.now() - timedelta(weeks=(one_month_to_week * 11) + 3)
print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=False)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=False)
)
```
<div dir="rtl">
المخرجات

```
"منذ 11 شهر و 3 اسابيع"
"11 شهر و 3 اسابيع"
"منذ 11 شهر و 3 اسابيع"
"11 شهر و 3 اسابيع"
```

</div>

**[[Back To Top 🔝]](#past_date2word)**

#### Years AR
```python
# 12 month == 1 year
# 4 weeks == 1 month
one_month_to_week = 4 * 1
one_year_to_week = one_month_to_week * 12

time = datetime.now() - timedelta(
    weeks=(one_year_to_week * 12) + (one_month_to_week * 5)
)
print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=True)
)
print(
    past_date2word(date=time, language="ar", with_ago=True, long_sentence=False)
)
print(
    past_date2word(date=time, language="ar", with_ago=False, long_sentence=False)
)
```
<div dir="rtl">
المخرجات

```
"منذ 12 سنة و 5 اشهر"
"12 سنة و 5 اشهر"
"منذ 12 سنة و 5 اشهر"
"12 سنة و 5 اشهر"
```

</div>

***
## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)
