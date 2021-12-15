import csv

class Product: # setting product as a class with name and price set to 0

    def __init__(self, name, price=0):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f'Product: {self.name}\nCost: {self.price}\n'

class ProductStock: # setting ProductStock as a class product name, product quantity and product price
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def name(self):
        return self.product.name;
    
    def unit_price(self):
        return self.product.price;
        
    def cost(self):
        return self.unit_price() * self.quantity # in object oriented programming the function is within the class
        
    def __repr__(self):
        return f"{self.product}Quantity: {self.quantity}\n"

class Customer: # read in the customer details from a CSV file

    def __init__(self, path):
        self.shopping_list = [] # define an empty shopping list (will append to later)
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.name = first_row[0] # treating the first row outside the for loop, defines the customer name
            self.budget = float(first_row[1]) # treating the first row outside the for loop, defines the customers budget
            for row in csv_reader: # for loop that loops through the CSV file and appends the product name and quantity to the shopping list
                name = row[0]
                quantity = float(row[1])
                p = Product(name)
                ps = ProductStock(p, quantity)
                self.shopping_list.append(ps) 
                
    def calculate_costs(self, shop_stock): # function to define the cost of the products in the customer shopping list
        for i in shop_stock: # loops through the shop stock
            for j in self.shopping_list: # loops through the customer shopping list
                if (j.name() == i.name()): # checks for a match
                    j.product.price = i.unit_price() # where theres a match, set the price
    
    def order_cost(self): # function to calculate the cost of the order
        cost = 0 # defining cost = 0
        for i in self.shopping_list: # loop through the shopping list
            cost += i.cost() # add each items cost to cost
        return cost # return the total cost
    
    def __repr__(self): # returns a string with customer order cost and remaining budget
        print('')
        str = f"\nHi {self.name}, welcome to {shop.name} Shop\n\n"
        str += f"{self.name} wants to buy the following:\n"
        for item in self.shopping_list:
            cost = item.cost()
            str += f"\n{item}"
            if (cost == 0):
                str += f"Apologies {self.name}, there's no price available for {item.product.name}\n"
            else:
                str += f"Total cost: {round(cost,2)}\n"
                
        str += f"\n{self.name}s budget is {self.budget}\n"
        str += f"\nThe cost would be {round(self.order_cost(),2)}, {self.name} would have {round(self.budget - self.order_cost(),2)} left"
        return str 

class Live(Customer): # Takes in details when shop operates in live mode
        def __init__(self):
            self.shopping_list = []
            self.name = input("Enter Product: ")
            self.quantity = input("Enter Quantity: ")
            self.budget = float(input("Enter Budget: "))
            p = Product(self.name)
            ps = ProductStock(p, self.quantity)
            self.shopping_list.append(ps)
 
class Shop: # Shop class reads in the Shop stock from CSV
    
    def __init__(self, path): # reads in the Shop stock from CSV
        self.stock = [] # define empty list as self.stock
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.name = str(first_row[0]) # shop name
            self.cash = float(first_row[1]) # shop cash value
            for row in csv_reader: # loops through the shop stock CSV file and sets the product details
                p = Product(row[0], float(row[1])) # product name and quantity
                ps = ProductStock(p, float(row[2])) # product price
                self.stock.append(ps) # appends the name, price and quantity details to self.stock list

    def shop_balance(self):
        print(f'Initial cash value for {shop.name} shop is {shop.cash}')

    def stock_levels_pricing(self):
            print(f'{self.name} shop currently has the following stock:\n')
            for i in self.stock:
                print(i)

    def check_shop(self, customer_shopping_list): # check to see if item on customer shopping list is in stock
        stock = self.stock
        for i in stock: # loops through the stock
            shop_item_name = i.product.name
            if shop_item_name == customer_shopping_list: 
                return i # if theres a match between the shopping list and stock then return that item

    def order_processing(self, customer): # process the order, arguments are self and customer
        total_cost = 0 # define cost at start = 0
        shop_balance = self.cash
        customer_balance = customer.budget
        print('')
        print('-'*30)    
        print(f'The shop has a balance of: {round(shop_balance,2)}') # shop balance from CSV file
        print(f'{customer.name} has a balance of: {round(customer_balance,2)}\n') # customer name and budget from CSV file
        print('-'*30)
        print(f'{customer.name} wants to place the following order:')
        print('-'*30)     

        order = customer.shopping_list
        for customer_wants in order: # loops through the customer shopping list
            customer_item_name = customer_wants.product.name # setting the customer item name

        # check if product on customers order is in the shop
            shop_has = Shop.check_shop(self, customer_item_name) # using Shop.check_shop function to see if product in stock
            if shop_has == None:
                print(f"\n*** WARNING *** No {customer_item_name} in stock\n")
                continue
            wanted = int(customer_wants.quantity)
            available = int(shop_has.quantity)

        # insufficient stock levels
            if available < wanted:
                print(f"\n*** WARNING *** Order can't be complete, there's insufficient stock levels for {customer_item_name} we have {available} in stock but you require {wanted}.")
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
                print(f"\n*** WARNING *** Insufficient funds for {customer_item_name}, you're short by {balance} funds available is {round(customer.budget,2)}")
            else:
                customer.budget -= purchase_cost
                self.cash += purchase_cost
        print('')
        print('-'*30)
        print(f'New shop balance is {round(self.cash,2)}')
        print(f'New customer balance is {round(customer.budget,2)}')
        print('-'*30)
        print('')

def display_menu(): # creating a menu to navigate the shop app
    print("")
    print("-" * 30)
    print(f"Welcome to {shop.name} Shop")
    print("-" * 30)
    print("Menu")
    print("=" * 10)
    print("1 - Shop Balance")
    print("2 - Product Stock Levels and Pricing")
    print("3 - Read in Customer Order")
    print("4 - Process Order")
    print("5 - Live Mode")
    print("x - Exit application")

shop = Shop("../stock.csv")

def main():
    display_menu()
    while True:
        choice = input("Choice: ")
        if (choice == "1"):
            print('')
            print('-'*50)
            shop.shop_balance()
            print('-'*50)
            display_menu()
        elif (choice == "2"):
            print('')
            print('-'*50)
            shop.stock_levels_pricing()
            print('-'*50)
            display_menu()
        elif (choice == "3"):
            selectCustomer = input("\nSelect Customer: A, B or C\n\n(A - shop not enough stock)\n\n(B - customer not enough money)\n\n(C - order can be fully processed): ")
            customer = Customer("../"+selectCustomer+".csv")
            #print(f"\nHi {customer.name}, welcome to {shop.name} Shop, {customer.name}s budget is {customer.budget}")
            #customer.welcome()
            customer.calculate_costs(shop.stock)
            print(customer)
            display_menu()
        elif (choice == "4"):
            selectCustomer = input("\nSelect Customer: A, B or C\n\n(A - shop not enough stock)\n\n(B - customer not enough money)\n\n(C - order can be fully processed): ")
            customer = Customer("../"+selectCustomer+".csv")
            print('')
            customer.calculate_costs(shop.stock)
            shop.check_shop(customer.shopping_list)
            shop.order_processing(customer)
            display_menu()
        elif (choice == "5"):
            print('-'*50)
            print('')
            live_customer = Live()
            live_customer.calculate_costs(shop.stock)
            shop.check_shop(live_customer.shopping_list)
            shop.order_processing(live_customer)
            display_menu()
            print('-'*50)
        elif (choice == "x"):
            break
        else:
            display_menu()

if __name__ == "__main__":
	main()