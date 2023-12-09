
import unittest
import PriceAllert 

class TestFetchPrice(unittest.TestCase):
    def test_fetch_price(self):
        target = PriceAllert.Target(
            "Python Course", "https://www.udemy.com/course/automate-your-life-with-python/?referralCode=7FA8B361D7A92B03A8C3", "udemy_com:price")
        price = PriceAllert.fetch_price(target)
        print(price)

if __name__ == '__main__':
    unittest.main()
