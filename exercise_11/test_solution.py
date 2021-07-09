from solution import Card, CardSuit, CardValue


def test_all_suits():
    assert len(list(CardSuit)) == 4


def test_a_value():
    assert len(list(CardValue)) == 13


def test_one_card():
    new_card = Card(CardSuit.SPADES, CardValue.TWO)
    assert str(new_card) == 'TWO of SPADES'


def test_two_cards():
    low_card = Card(CardSuit.SPADES, CardValue.TWO)
    high_card = Card(CardSuit.SPADES, CardValue.THREE)
    assert low_card < high_card
    assert high_card > low_card


def test_two_suits():
    low_card = Card(CardSuit.HEARTS, CardValue.TWO)
    high_card = Card(CardSuit.SPADES, CardValue.TWO)
    assert low_card < high_card
    assert high_card > low_card
