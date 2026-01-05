from backend import database_helper

def test_fetch_expenses_for_date_valid():
    expenses = database_helper.fetch_expenses_for_date("2024-08-15")

    assert len(expenses) == 1
    assert expenses[0]["amount"] == 10
    assert expenses[0]["category"] == "Shopping"
    assert expenses[0]["notes"] == "Bought potatoes"




def test_fetch_expenses_for_date_invalid():
    expenses = database_helper.fetch_expenses_for_date("2027-08-15")

    assert len(expenses) == 0