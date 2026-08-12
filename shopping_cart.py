products={101:{'name':'laptop','price':35000},102:{'name':'mobile','price':15000},103:{'name':'tablet','price':20000},104:{'name':'headphones','price':5000},105:{'name':'smartwatch','price':6000}}
cart={}
def display_products():
    print("\n"+"="*50)
    print("*^____^* PRODUCTS *^____^*")
    print("\n"+"="*50)
    print(f"{'ID':<8}{'Product':<20}{'Price':>10}")
    print("-"*50)
    for product_id, product in products.items():
     print(f"{product_id:<8}"f"{product['name']:<20}"f"{product['price']:>9}")\
     

        
        

