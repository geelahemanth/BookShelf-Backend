from flask import Flask
import requests
from config import api_key




app=Flask(__name__)

@app.route('/')
def home():
    
    book_name=input("Search of your favorite book :")
    url=f'https://www.googleapis.com/books/v1/volumes?q={book_name}&key={api_key}'
    
    response=requests.get(url)
    if response.status_code ==200:
        result=response.json()
        #print(result)
        for values in result.get('items',[]):
            title=values['volumeInfo'].get('title','no title found')
            author=values['volumeInfo'].get('authors','no author found')[0]
            retail_price=values['saleInfo'].get('retailPrice',{}).get('amount','Price Not Mentioned')
            buy_link=values['saleInfo'].get('buyLink','Link not mentioned')
            if retail_price != 'Price Not Mentioned':
                output=f'{retail_price} INR'
            else:
                output=retail_price
                
    
            final_output=(f'Title : {title}\nAuthor : {author}\nRetail_Price : {output}\nBuy_Link : {buy_link}\n')
            print(final_output)
        
    else:
        print("Failed to retrive books")
    
    return 'hii'

if __name__=="__main__":
    app.run(debug=True)
    
