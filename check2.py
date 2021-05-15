#Mahmud Cole, Hamzah Karachiwalla
from argparse import ArgumentParser
import sys 
import re
import pandas as pd 
import csv 

class Vinylrecord: 
    """Listing 20 available record types at our Store.
    Attributes: 20 records available for purchase, pending availability 
    """   
    def __init__(self, vinylfile):
        self.df = pd.read_csv(vinylfile)
        self.cart = []
        
    def metadata(self):
        """This method lists different factors of the vinyl class, characteristics are used to categorize the vinyls

        Return: 
            Series element: requested piece of metadata could 
            be a string
        """ 
        print("""
        1. vinyl_id
        2. album_name
        3. artist_name
        4. genre
        5. track_amount
        6. runtime
        7. first_available
        8. weight
        9. is_explicit
        10. billboard
        11. occ
        12. aria
        13. gfk 
        14. oricon
        15. gold
        16. platinum
        17. multi_platinum
        18. diamond
        19. discogs_rating
        20. rollingstone_rating
        21. amazon_rating
        22. label_name
        23. label_city
        24. label_country
        25. price in $
        26. quantity 
        """)
        n = int(input("pick a number to view your selected metadata "))
        return self.df.iloc[:,n - 1]




        def purchase(self, vinylid):
        self.cart.append(vinylid)
    """Place a function in a cart without a user
    """

    def make_purchase(self):
        """Called the user input, call the purchase function
        
        """
        choice = int(input('Enter the vinyl ID of what Vinyl you want to buy'))
        self.purchase(choice)

        def get_price(self,vinylid):
        row = self.df[self.df["vinyl_id"] == vinylid].iloc[0]
        return row['price in $'] 
        

    def total(self):
        total = 0.0 
        for vinylid in self.cart:
            total += self.get_price(vinylid)
        return total 

def main(vinylfile):
    chance = Vinylrecord(vinylfile)
    print(chance.metadata()) 
    while True:
        chance.make_purchase()
        question = (input('Would you like to make another purchase?'))
        if question == 'no':
            break
    total = chance.total()
    print("Your total is " +str(total)+"dollars today.")   
    
if __name__ == "__main__":
    main("vinyldata1.csv")
