# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from logic.core import elapsed_time, printf


@elapsed_time(precision=10)
def example(secs: float):
    time.sleep(secs)
    return 'returned success'


@elapsed_time(precision=3)
def other_example():
    for i in range(99999999):
        pass
    return 'returned success'


@elapsed_time()
def other_other_example():
    for i in range(99999):
        pass
    return 'returned success'


if __name__ == '__main__':
    # example 1
    result, elapsed, formatted = example(2.56785)
    printf(result, elapsed, formatted, example.__name__)
    # example 2
    result, elapsed, formatted = other_example()
    printf(result, elapsed, formatted, other_example.__name__)
    
    # example 2
    result, elapsed, formatted = other_other_example()
    printf(result, elapsed, formatted, other_other_example.__name__)