# shopping_cart.py

# Google Sheets Import














import datetime
import os
from dotenv import load_dotenv

load_dotenv()

import gspread

from oauth2client.service_account import ServiceAccountCredentials



DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")
SHEET_NAME = os.environ.get("SHEET_NAME", "products")

#
# AUTHORIZATION
#

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth",
                                    "google_api_credentials.json")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)


client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>

doc = client.open_by_key(DOCUMENT_ID) #> <class 'gspread.models.Spreadsheet'>

print("-----------------")
print("SPREADSHEET:", doc.title)
print("-----------------")

sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>

rows = sheet.get_all_records() #> <class 'list'>

#for row in rows:
#    print(row) #> <class 'dict'>





#products = [
#    {
#        "id": 1,
#        "name": "Chocolate Sandwich Cookies",
#        "department": "snacks",
#        "aisle": "cookies cakes",
#        "price": 3.50
#    }, {
#        "id": 2,
#        "name": "All-Seasons Salt",
#        "department": "pantry",
#        "aisle": "spices seasonings",
#        "price": 4.99
#    }, {
#        "id": 3,
#        "name": "Robust Golden Unsweetened Oolong Tea",
#        "department": "beverages",
#        "aisle": "tea",
#        "price": 2.49
#    }, {
#        "id": 4,
#        "name":
#        "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce",
#        "department": "frozen",
#        "aisle": "frozen meals",
#        "price": 6.99
#    }, {
#        "id": 5,
#        "name": "Green Chile Anytime Sauce",
#        "department": "pantry",
#        "aisle": "marinades meat preparation",
#        "price": 7.99
#    }, {
#        "id": 6,
#        "name": "Dry Nose Oil",
#        "department": "personal care",
#        "aisle": "cold flu allergy",
#        "price": 21.99
#    }, {
#        "id": 7,
#        "name": "Pure Coconut Water With Orange",
#        "department": "beverages",
#        "aisle": "juice nectars",
#        "price": 3.50
#    }, {
#        "id": 8,
#        "name": "Cut Russet Potatoes Steam N' Mash",
#        "department": "frozen",
#        "aisle": "frozen produce",
#        "price": 4.25
#    }, {
#        "id": 9,
#        "name": "Light Strawberry Blueberry Yogurt",
#        "department": "dairy eggs",
#        "aisle": "yogurt",
#        "price": 6.50
#    }, {
#        "id": 10,
#        "name": "Sparkling Orange Juice & Prickly Pear Beverage",
#        "department": "beverages",
#        "aisle": "water seltzer sparkling water",
#        "price": 2.99
#    }, {
#        "id": 11,
#        "name": "Peach Mango Juice",
#        "department": "beverages",
#        "aisle": "refrigerated",
#        "price": 1.99
#    }, {
#        "id": 12,
#        "name": "Chocolate Fudge Layer Cake",
#        "department": "frozen",
#        "aisle": "frozen dessert",
#        "price": 18.50
#    }, {
#        "id": 13,
#        "name":
#        "Saline Nasal Mist",
#        "department": "personal care",
#        "aisle": "cold flu allergy",
#        "price": 16.00
#    }, {
#        "id": 14,
#        "name":
#        "Fresh Scent Dishwasher Cleaner",
#        "department": "household",
#        "aisle": "dish detergents",
#        "price": 4.99
#    }, {
#        "id": 15,
#        "name":
#        "Overnight Diapers Size 6",
#        "department": "babies",
#        "aisle": "diapers wipes",
#        "price": 25.50
#    }, {
#        "id": 16,
#        "name":
#        "Mint Chocolate Flavored Syrup",
#        "department": "snacks",
#        "aisle": "ice cream toppings",
#        "price": 4.50
#    }, {
#        "id": 17,
#        "name":
#        "Rendered Duck Fat",
#        "department": "meat seafood",
#        "aisle": "poultry counter",
#        "price": 9.99
#    }, {
#        "id": 18,
#        "name":
#        "Pizza for One Suprema Frozen Pizza",
#        "department": "frozen",
#        "aisle": "frozen pizza",
#        "price": 12.50
#    }, {
#        "id": 19,
#        "name":
#        "Gluten Free Quinoa Three Cheese & Mushroom Blend",
#        "department": "dry goods pasta",
#        "aisle": "grains rice dried goods",
#        "price": 3.99
#    }, {
#        "id": 20,
#        "name":
#        "Pomegranate Cranberry & Aloe Vera Enrich Drink",
#        "department": "beverages",
#        "aisle": "juice nectars",
#        "price": 4.25
#    }
#] 
# 
#  # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"  #> $12,000.71


# TODO: write some Python code here to produce the desired output

#print(products)

pricelist = []
orderlist = []
product_list = [str(p["id"]) for p in rows]


#doneclass MyCustomError:
#done    print()
#doneraise MyCustomError("Product Not Found")

#def pid(products):
# return [d for d in products if str(d["id"] == d]


#while True:
#matching_products = [p for p in products if str(p["id"]) == x]
#print(matching_products)
#matching_product = matching_products[0]
#print("Selected Product: " + matching_product["name"] + " " + str(matching_product["price"]))
#
total_price = 0

while True:
    x = input(
           'Please Scan or Enter The Product Code; Enter done if complete: ')
    if x == "done":
        break
    else:
        try:
            matching_products = [p for p in rows if str(p["id"]) == x]
            matching_product = matching_products[0]
            total_price = total_price + (matching_product["price"])
            y = int(matching_product["price"])
<<<<<<< HEAD
            i = "... " + matching_product["name"] + "  " + to_usd(
=======
            i = matching_product["name"] + "     " + to_usd(
>>>>>>> parent of 76727c0... Complete Raw code 
                matching_product["price"])
            #print("Selected Product: " + matching_product["name"] + " " + str(matching_product["price"]))
            pricelist.append(y)
            orderlist.append(i)
#print(x)
        except:
            print("Product Not Found")

#print(*pricelist, sep="\n")

#for id in orderlist:
    pass
#total_price =


#> ---------------------------------
#> GREEN FOODS GROCERY
#> WWW.GREEN-FOODS-GROCERY.COM
#> ---------------------------------
#> CHECKOUT AT: 2020-02-07 03:54 PM
#> ---------------------------------
#> SELECTED PRODUCTS:
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... All-Seasons Salt ($4.99)
#>  ... Robust Golden Unsweetened Oolong Tea ($2.49)
#>  ... All-Seasons Salt ($4.99)
#>  ... Chocolate Sandwich Cookies ($3.50)
#> ---------------------------------
#> SUBTOTAL: $19.47
#> TAX: $1.70
#> TOTAL: $21.17
#> ---------------------------------
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------




print('---------------------------------')
print('Not Your Parents Bodega')
print('WWW.NOTYOURPARENTSBODEGA>COM')
print('---------------------------------')
import datetime
y = datetime.datetime.now()

print(" Checkout At " + (y.strftime("%Y-%m-%d %I:%M %p")))
print('---------------------------------')
print('---------------------------------')
print('---------------------------------')
print('---------------------------------')

print(matching_product["name"] + "           " +
      str(matching_product["price"]))

print(*orderlist, sep="\n")

print("Total Product Price: " + str(total_price))
#for y in orderlist

tax = (total_price * .08875)
costplustax = (total_price + tax)

t = to_usd(tax)
c = to_usd(costplustax)
print("Total Tax: " + t)
print("Order Total: " + c)
