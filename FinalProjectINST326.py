#Mahmud Cole
from argparse import ArgumentParser
import sys 
import re
import pandas as pd 
import csv 
import tkinter as tk
from tk import *
import PyPDF2
from PIL import Image, ImageTk


class Vinylrecord: 
    """This class lists 20 of the records we created in a CSV file.
    Attributes: 20 records available for purchase, pending availability.
    """ 
    def __init__(self, vinylfile):
        """This init method creates an empty shopping cart by allowing users to pass through a vinyl file from the CSV file-vinylfile.
        
        Attribute:
            vinylfile: A CSV database of 20 different vinyl records from 1980-2020. 
       
        """
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

    def record_info(record):
      """
      Args: 
          record (str): name of the record  
      Returns:
          Series: the metadata of the record 
      Side effects:
          printing a message: if the record doesnt exist
      """
      df = pd.read_csv("vinyldata.csv")
      for i in range(len(df)):
        for each in df.loc[i]:
          if each == record:
            return df.loc[i]   
      print("record doesnt exist")
    
    def purchase(self, vinylid):
        self.cart.append(vinylid)
        """Place a function in a cart without a user. This function allows users to add an item associated with vinyl ID to their cart
        Args:
        User appends vinylID to previously empty shopping cart.
        """

    def make_purchase(self):
        """After calling the user input Users are able to finalize a purchase through the input statement.
        When users enter the vinyl ID value of their choice, the item will exist as a string in their shopping cart.
        Args:
            User must input vinyl ID to recieve the option to make a purchase.    
        """
        choice = int(input('Enter the vinyl ID of what Vinyl you want to buy'))
        self.cart.append(choice)
    
    def get_price(self,vinylid):
        """User is able to recieve the price of the item in their shopping cart. 
        Any choice selected from the list of metadata will be passed through the function. 
        
        Args: 
            User is able to recieve the price in vinyl 
        
        Attributes: 
            vinylid: piece of metadata selected by the user in the Vinylrecord class.
            
        Return:
            "price is $"
        """
        row = self.df[self.df["vinyl_id"] == vinylid].iloc[0]
        return row['price in $'] 
        

    def total(self):
        """The total is a function that starts at 0, and ads the price from the get_price method 
        to the empty shopping cart, that was formerly 0.0. This new value is from the vinylid. 
        
        Args: 
            Creates an equation to add the get_price to the current 0.0 value of the empty shopping cart.  
      
        return: 
            total of price 
        """
        total = 0.0 
        for vinylid in self.cart:
            total += self.get_price(vinylid) 
        return total 
    
def main(vinylfile):
    """This  function will allow users to continue to purchase items in the vinylfile metadata until they say no, 
    no will end the round of purchases for this user. This is done through a while loop; only when the function is 
    True, will users be allowed to continue to purchase. 
        Args: 
            Takes in chance.make_purchase, the option to make a purchase if a total was returned in def total method. 
            While loop to continue purchase until 'no' is entered by user. 
        
        Attributes:
            The vinylfile: contains the shopping cart  
            
        break: 
            End the function as user only has the option to purchase.
    """
    chance = Vinylrecord(vinylfile)
    print(chance.metadata()) 
    while True:
        chance.make_purchase()
        question = (input('Would you like to make another purchase?'))
        if question == 'no':
            break
    total = chance.total()

    
    root = tk.Tk()
    canvas = tk.Canvas(root, width=200, height=50)
    canvas.grid(columnspan=3)

    """Creating a png image of logo which opens an image of the vinyl record chosen.
    GUI is intended to print out the list of vinyls selected from purchase in the user's cart.
    """
    logo = Image.open('logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=1)

    totalamount = tk.Label(root, text = f"Your total is " +str(total) + " dollars today.", font = "Silom")
    totalamount.grid(columnspan=3, column=0, row=2)
    """Instructions for the GUI:
    Return a string of the total price of vinyl_id from chance.total in main function.
    
    Args:
        User is able to recieve total price in dollars of vinylID.

        Return: The total section in the image.
    """
    instructions = tk.Label(root, text = "Thank you for shopping at our Record Store!", font = "Silom")
    instructions.grid(columnspan=3, column=0, row=3)
    
    def buttonfunction():
        """This buttonfunction is the interactive part of this graphic design. When the button is chosen it will:
        Args:
            Takes in vinylId in chance.cart
        
        Returns:
            Name of album corresponding to the chosen vinyl IDs. 
        """
        for vinylid in chance.cart:
            print("You've selected", (chance.df["album_name"][vinylid]), "today.")
    
    b = tk.Button(root, text = "See the records you chose!", font = "Silom", command = buttonfunction)
    b.grid()

    root.mainloop()


if __name__ == "__main__":
    """After the final purchase is recieved, this method allows the program to end with the final 
    purchase price for all metadata selected in the previous method. The purchase was based on the
    additions from all pieces of metadata from the vinylid section (1) of 'vinyldata1.csv', the dataframe used
    for this code.        
    """
    main("vinyldata.csv")