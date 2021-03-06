#!/Users/jeff/.pyenv/shims/python

import pytest
from solution import tr

##############################################################################
# Usage: run "pytest" in the local directory after renaming one of the two
#        solutions to "solution.py".
# Note: Assumes you have pytest installed. If not, run "pip install pytest".
##############################################################################


def test_empty_source():
    with pytest.raises(TypeError):
        noop_tr = tr('', 'abcd')


def test_empty_result():
    with pytest.raises(TypeError):
        noop_tr = tr('abcd', '')


def test_simple():
    a_to_b_tr = tr('a', 'b')
    assert callable(a_to_b_tr)
    assert a_to_b_tr('abcdabcd') == 'bbcdbbcd'


def test_2_to_1():
    ab_to_c_tr = tr('ab', 'c')
    assert ab_to_c_tr('abcdabcd') == 'cccdcccd'


def test_remove():
    ab_to_c_tr = tr('ab', 'x')
    assert ab_to_c_tr('abcdabcd') == 'xxcdxxcd'

def test_swap():
    swap_ab_tr = tr('ab', 'ba')
    assert callable(swap_ab_tr)
    assert swap_ab_tr('abcdabcd') == 'bacdbacd'
