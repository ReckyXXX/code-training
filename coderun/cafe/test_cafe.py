import pytest
from coderun.cafe.cafe import *


# task tests:

def test1():
    result = CouponesStrategy(min_sum=235, unused_coupones_count=0, used_coupones_count=1, coupone_days=[5])
    assert calculate_coupones_strategy(5, [35, 40, 101, 59, 63]) == result

