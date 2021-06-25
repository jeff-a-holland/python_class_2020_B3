def test_zero_loan():
    myloan = Loan(0, 0.1)

    d = arrow.get(2100, 1, 1)
    assert myloan.total_on(d) == 0


def test_1k_loan_1pct():
    myloan = Loan(1000, 0.1, arrow.get(2020, 1, 1))
    d = arrow.get(2021, 1, 1)
    amount_due = myloan.total_on(d)
    assert int(amount_due * 100) / 100 == 1100.28

    d = arrow.get(2025, 1, 1)
    amount_due = myloan.total_on(d)
    assert int(amount_due * 100) / 100 == 1611.35


def test_1k_loan_2pct():
    myloan = Loan(1000, 0.2, arrow.get(2020, 1, 1))

    d = arrow.get(2021, 1, 1)
    amount_due = myloan.total_on(d)
    assert int(amount_due * 100) / 100 == 1200.59

    d = arrow.get(2025, 1, 1)
    amount_due = myloan.total_on(d)
    assert int(amount_due * 100) / 100 == 2490.80


def test_1k_loan_2pct_specific_date():
    initial_date = arrow.get(2021, 1, 1)
    myloan = Loan(1000, 0.2, initial_date)

    d = arrow.get(2025, 1, 1)
    amount_due = myloan.total_on(d)
    assert int(amount_due * 100) / 100 == 2074.63

    d = arrow.get(2026, 1, 1)
    amount_due = myloan.total_on(d)
    assert int(amount_due * 100) / 100 == 2489.56


def test_1k_loan_2pct_date_range():
    initial_date = arrow.get(2021, 1, 1)
    myloan = Loan(1000, 0.2, initial_date)

    range_start = arrow.get(2022, 1, 1)
    range_end = arrow.get(2022, 2, 1)

    daily_amounts = myloan.total_on_each(range_start, range_end)
    assert iter(daily_amounts) == daily_amounts

    daily_amounts_list = list(daily_amounts)
    assert isinstance(daily_amounts_list[0], tuple)
    assert isinstance(daily_amounts_list[0][0], arrow.Arrow)
    assert isinstance(daily_amounts_list[0][1], float)
