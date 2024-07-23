import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the job portal page
url = 'https://books.toscrape.com/'

# Send a GET request
response = requests.get(url)

soup = BeautifulSoup(response.text)

listings = soup.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

books = []
for listing in listings:
     product_name = listing.find("article").find("h3").a.attrs.get("title")
     product_price = listing.find("div",class_="product_price").p.text

     books.append(
           {
                "Book Name": product_name,
                "Book Price": product_price
           }
          
     ) 
df = pd.DataFrame(books)
df.to_csv("Book Store.csv", index=False)