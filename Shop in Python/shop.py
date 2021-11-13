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

#def print_customer(c):
    print(f'\nCUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: {c.budget}')

    for item in c.shopping_list:
        print_product(item.product)

        print(f'{c.name} ORDERS {item.quantity} OF ABOVE PRODUCT')
        cost = item.quantity * item.product.price
        print(f'The cost to {c.name} will be €{cost}')

#def print_product(p):
    print(f'\nPRODUCT NAME: {p.name} \nPRODUCT PRICE: {p.price}')

#def print_shop(s):
    print(f'Shop has {s.cash} in cash')
    for item in s.stock:
        print_product(item.product)
        print(f'The Shop has {item.quantity} of the above')

def check_shop(in_shop, looking_for):
    stock = in_shop.stock
    for i in stock:
        shop_item_name = i.product.name
        if shop_item_name == looking_for:
            return i

def process_order(in_shop, customer):
    total_cost = 0
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
            print(f"\nThere's {available} of {customer_item_name} in stock, your order of {wanted} can be satisied leaving {remaining} remaining in stock.")
            shop_has.quantity -= wanted
            purchase_cost = wanted * shop_has.product.price
            balance = round(customer.budget - purchase_cost,2)
            print(f"The unit cost of {customer_item_name} is {round(shop_has.product.price,2)} so the total cost for {wanted} is {round(purchase_cost,2)}.")
            print(f"Your budget is {round(customer.budget,2)} leaving a balance of {balance}")

# insufficient funds
        
        total_cost += purchase_cost
        total_cost = round(total_cost,2)
        #print(f'total cost is {total_cost}')
        if total_cost > customer.budget :
            print(f"Insufficient funds, total cost is {total_cost}, funds available is {customer.budget}")
        else:
            customer.budget -= purchase_cost
            in_shop.cash += purchase_cost

customer = read_customer("../customer.csv")          
in_shop = create_and_stock_shop()

process_order(in_shop, customer)