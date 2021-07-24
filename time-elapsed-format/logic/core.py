# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time

DEFAULT_PRECISION = 8
HOURS, MIN, SECONDS = 24, 60, 60
VALID_UNITS = {
    'd': 'day',
    'h': 'hour',
    'm': 'minute',
    's': 'second',
    'ms': 'milisecond',
    'ns': 'nanosecond',
}


def to_text(value: int, key: str) -> str:
    if value == 0:
        return ''
    plural = 's' if value > 1 else ''
    return f"{value} {VALID_UNITS[key]}{plural}"


def extractor(digits: int, secs: int) -> tuple:
    return int(digits / secs), digits % secs


def format_elapsed(duration: float, precision: int) -> str:
    precision = abs(precision)
    integer_part, decimal_part = str(duration).split('.')
    integer_part = int(integer_part)
    mili_part, nano_part_s = decimal_part[:3], decimal_part[3:]
    mili_part = int(mili_part.lstrip('0') or '0') if precision > 0 else 0
    nano_part = 0
    if precision > 3:  # show nanoseconds
        nano_part = int(nano_part_s[:precision - 3].lstrip('0') or '0')
    days, integer_part = extractor(integer_part, (HOURS * MIN * SECONDS))
    hours, integer_part = extractor(integer_part, (MIN * SECONDS))
    minutes, seconds = extractor(integer_part, SECONDS)
    options = list(
        filter(
            lambda v: v != '',  # omit empty strings -> 0
            [
                to_text(days, 'd'),
                to_text(hours, 'h'),
                to_text(minutes, 'm'),
                to_text(seconds, 's'),
                to_text(mili_part, 'ms'),
            ]
        )
    )
    if precision > 3:
        options.append(to_text(nano_part, 'ns'))
    return ' and '.join(options)
    

def elapsed_time(*args, **kw):
    start_time = time.monotonic()
    prec = kw.get('precision', DEFAULT_PRECISION)
    
    def decorator(func):
        def wrapper(*arg, **kwargs):
            result = func(*arg, **kwargs)
            end_time = time.monotonic()
            elapsed = end_time - start_time
            elapsed_as_str = format_elapsed(elapsed, prec)
            return result, elapsed, elapsed_as_str
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator


def printf(res, elapsed, formatted, func_name):
    print('*' * 30)
    print(f'running function: {func_name}!')
    print('result is: ', res)
    print(f'it lasted (raw): {elapsed} secs to finish')
    print(f'or lasted (formatted): {formatted} to finish')
    print('*' * 30)


@elapsed_time(precision=10)
def example_1(secs: float) -> str:
    time.sleep(secs)
    return 'success'


@elapsed_time(precision=3)
def example_2() -> str:
    for i in range(99999999):
        pass
    return 'success'  # or any type



