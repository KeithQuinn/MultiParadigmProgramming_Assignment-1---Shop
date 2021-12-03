from dataclasses import dataclass, field
from typing import List
import csv

@dataclass
class Product:
    name: str
    price: float = 0.0

@dataclass
class ProductStock:
    product: Product
    quantity: int

@dataclass
class Shop:
    cash: float = 0.0
    stock: List[ProductStock] = field(default_factory=list)

@dataclass
class Customer:
    name: str = ""
    budget: float = 0
    shopping_list: List[ProductStock] = field(default_factory=list)

# Display menu	
def display_menu():
    print("")
    print("Welcome to the Shop")
    print("-" * 9)
    print("Menu")
    print("=" * 4)
    print("1 - Shop Balance")
    print("2 - Product Stock Levels and Pricing")
    print("3 - Read in Customer Order")
    print("4 - Process Order")
    print("5 - Live Mode")
    print("x - Exit application")

def create_and_stock_shop():
    s = Shop()
    with open('../stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        s.cash = float(first_row[1])
        for row in csv_reader:
            p = Product(row[0], float(row[1]))
            ps = ProductStock(p, float(row[2]))
            s.stock.append(ps)
            #print(ps)
    return s

def read_customer(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        c = Customer(first_row[0], float(first_row[1]))
        for row in csv_reader:
            name = row[0]
            quantity = float(row[1])
            p = Product(name)
            ps = ProductStock(p, quantity)
            c.shopping_list.append(ps)
    return c

def print_customer(c):
    print(f'\nCUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: {c.budget}')

    for item in c.shopping_list:
        print_product(item.product)

        print(f'{c.name} ORDERS {item.quantity} OF ABOVE PRODUCT')
        cost = item.quantity * item.product.price
        print(f'The cost to {c.name} will be €{cost}')

def print_product(p):
    print(f'\nPRODUCT NAME: {p.name} \nPRODUCT PRICE: {p.price}')

def print_shop(s):
    #print(f'Shop has {s.cash} in cash')
    print('')
    print('-'*30)
    for item in s.stock:
        print_product(item.product)
        print(f'The Shop has {item.quantity} of the above')
    print('')
    print('-'*30)
    print('')

def print_shop_balance(s):
    print('')
    print('-'*30)
    print('')
    print(f'Shop has {s.cash} in cash')
    print('')
    print('-'*30)
    print('')

def check_shop(in_shop, looking_for):
    stock = in_shop.stock
    for i in stock:
        shop_item_name = i.product.name
        if shop_item_name == looking_for:
            return i

def online_order(in_shop, customer):
    total_cost = 0
    shop_balance = in_shop.cash
    customer_balance = customer.budget
    print('')
    print('-'*30)    
    print(f'The shop has a balance of: {shop_balance}')
    print(f'{customer.name} has a balance of: {customer_balance}')
    print('-'*30)
    
    order = customer.shopping_list
    for customer_wants in order:
        customer_item_name = customer_wants.product.name

    # check if product on customers order is in the shop
        shop_has = check_shop(in_shop, customer_item_name)
        if shop_has == None:
            print(f"\nNo {customer_item_name} in stock\n")
            continue
        wanted = int(customer_wants.quantity)
        available = int(shop_has.quantity)

    # insufficient stock levels
        if available < wanted:
            print(f"\nOrder can't be complete, there's insufficient stock levels for {customer_item_name} we have {available} in stock but you require {wanted}.")
            continue

    # sufficient stock levels
        if available >= wanted :
            remaining = available - wanted
            print(f"\nThere's {available} {customer_item_name} in stock, your order of {wanted} can be satisied leaving {remaining} remaining in stock.")
            shop_has.quantity -= wanted
            purchase_cost = wanted * shop_has.product.price
            balance = round(customer.budget - purchase_cost,2)
            print(f"The unit cost of {customer_item_name} is {round(shop_has.product.price,2)} so the total cost for {wanted} is {round(purchase_cost,2)}.")
            print(f"Your budget is {round(customer.budget,2)} leaving a balance of {balance}")

    # insufficient funds
        
        total_cost += purchase_cost
        total_cost = round(total_cost,2)
        #print(f'total cost is {total_cost}')
        if purchase_cost > customer.budget :
            print('')
            print(f"Insufficient funds for {customer_item_name}, you're short by {balance} funds available is {round(customer.budget,2)}")
        else:
            customer.budget -= purchase_cost
            in_shop.cash += purchase_cost

    print('')
    print('-'*30)
    print(f'New shop balance is {in_shop.cash}')
    print(f'New customer balance is {round(customer.budget,2)}')
    print('-'*30)
    print('')
    

def live_order_details():
    #name = input(str("Enter Name: "))
    item = input(str("Choose an item: "))
    quantity = int(input("Choose a quantity: "))
    #budget = float(input("Enter budget: "))
    
    #c = Customer(name, float(budget))
    p = Product(item)
    ps = ProductStock(p, quantity)
    c = Customer(item, quantity)
    c.shopping_list.append(ps)
    return c

def live_order(in_shop, customer):
    total_cost = 0
    shop_balance = in_shop.cash
    customer_balance = float(input("Enter Budget: "))
    print('')
    print('-'*30)    
    print(f'The shop has a balance of: {shop_balance}')
    #print(f'{customer.name} has a balance of: {customer_balance}')
    print('-'*30)
    
    order = customer.shopping_list
    for customer_wants in order:
        customer_item_name = customer_wants.product.name

    # check if product on customers order is in the shop
        shop_has = check_shop(in_shop, customer_item_name)
        if shop_has == None:
            print(f"\nNo {customer_item_name} in stock\n")
            continue
        wanted = int(customer_wants.quantity)
        available = int(shop_has.quantity)

    # insufficient stock levels
        if available < wanted:
            print(f"\nOrder can't be complete, there's insufficient stock levels for {customer_item_name} we have {available} in stock but you require {wanted}.")
            continue

    # sufficient stock levels
        if available >= wanted :
            remaining = available - wanted
            print(f"\nThere's {available} {customer_item_name} in stock, your order of {wanted} can be satisied leaving {remaining} remaining in stock.")
            shop_has.quantity -= wanted
            purchase_cost = wanted * shop_has.product.price
            balance = round(customer_balance - purchase_cost,2)
            print(f"The unit cost of {customer_item_name} is {round(shop_has.product.price,2)} so the total cost for {wanted} is {round(purchase_cost,2)}.")
            print(f"Your budget is {round(customer_balance,2)} leaving a balance of {balance}")

    # insufficient funds
        
        total_cost += purchase_cost
        total_cost = round(total_cost,2)
        #print(f'total cost is {total_cost}')
        if purchase_cost > customer_balance :
            print('')
            print(f"Insufficient funds for {customer_item_name}, you're short by {balance} funds available is {round(customer.budget,2)}")
        else:
            #customer_balance -= purchase_cost
            in_shop.cash += purchase_cost
    print('')
    print('-'*30)
    print(f'New shop balance is {round(in_shop.cash,2)}')
    print(f'New customer balance is {round(customer_balance,2)}')
    print('-'*30)
    print('')

selectCustomer = input("Select Customer: A, B, C, D or E: ")
#customer = read_customer("../"+selectCustomer+".csv")

def main():
    display_menu()
    while True:
        choice = input("Choice: ")
        if (choice == "1"):
            in_shop = create_and_stock_shop()
            print_shop_balance(in_shop)
            display_menu()
        elif (choice == "2"):
            print_shop(in_shop)
            display_menu()
        elif (choice == "3"):
            #selectCustomer = input("Select Customer: A, B, C, D or E: ")
            customer = read_customer("../"+selectCustomer+".csv")
            print_customer(customer)
            display_menu()
        elif (choice == "4"):
            in_shop = create_and_stock_shop()
            #selectCustomer = input("Select Customer: A, B, C, D or E: ")
            customer = read_customer("../"+selectCustomer+".csv")
            online_order(in_shop, customer)
            display_menu()
        elif (choice == "5"):
            customer = live_order_details()
            in_shop = create_and_stock_shop()
            live_order(in_shop, customer)
            display_menu()
        elif (choice == "x"):
            break
        else:
            display_menu()

if __name__ == "__main__":
	main()