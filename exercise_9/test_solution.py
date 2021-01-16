#!/Users/jeff/.pyenv/shims/python


def test_checks_for_ints():
    @mymypy([int, int])
    def mul(a, b):
        return a*b

    assert mul(3, 5) == 15

    with pytest.raises(TypeError) as e:
        value = mul([10, 20, 30], 5)
        assert e.message == '[10, 20, 30] must be of type int'


def test_two_errors_one_exception():
    @mymypy([int, int])
    def mul(a, b):
        return a*b

    with pytest.raises(TypeError) as e:
        value = mul([10, 20, 30], [10, 20, 30])
        assert e.message == '[10, 20, 30] must be of type int'


def test_checks_other_types():
    @mymypy([str, int])
    def mul(a, b):
        return a*b

    assert mul('a', 5) == 'aaaaa'

    with pytest.raises(TypeError) as e:
        value = mul(3, 5)
        assert e.message == '3 must be of type str'
