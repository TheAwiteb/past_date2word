


# past_date2word


**past_date2word is library helps you to convert the past date to text**

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
</p>


[Requirements](#Requirements)
•
[Installation](#Installation)
•
[Examples](#Examples)
•
[License](#License)

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

```python
from past_date2word import past_date2word
from datetime import datetime, timedelta

# Less than one second of time
date = datetime.now() - timedelta(seconds=1)
print(past_date2word(date)) # "1 second ago"

# Less than 23 seconds of time
date = datetime.now() - timedelta(seconds=23)
print(past_date2word(date)) # "23 seconds ago"

# Less than 1 week and 1 day of time
date = datetime.now() - timedelta(weeks=1, days=1)
print(past_date2word(date)) #"1 week and 1 day ago"

# Less than 2 weeks and 4 days of time
date = datetime.now() - timedelta(weeks=2, days=4)
print(past_date2word(date)) #"2 weeks and 4 days ago"

# And more try it

```
***
## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)
