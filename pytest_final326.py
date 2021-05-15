from FinalProjectINST326 import Vinylrecord
"""
Pytest test runner. 
This test function is added to the get_price.py package
Calling this test function will determine the price of 
all vinyl_id based on the 'vinyldata.csv' which lists metadata.
The price will be determined from the original function
and asserting the total is used to recognize the result when the 
input is entered.
"""



def test_get_price():
    v = Vinylrecord("vinyldata.csv")
    assert v.get_price(3) == 18
    assert v.get_price(2) == 22
    assert v.get_price(11) == 18
    

def test_total():
    v1 = Vinylrecord("vinyldata.csv")
    v2 = Vinylrecord("vinyldata.csv")
    v3 = Vinylrecord("vinyldata.csv")
    assert v1.total() == 2

    v1.purchase(1)
    assert v1.total() == 10
    v2.purchase(5)
    v2.purchase(7)
    assert v2.total() == 41
    v3.purchase(2)
    v3.purchase(4)
    v3.purchase(6)
    assert v3.total() == 54
