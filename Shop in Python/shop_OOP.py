import csv

class Product:

    def __init__(self, name, price=0):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f'Product: {self.name}\nCost: {self.price}\n'

class ProductStock:
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def name(self):
        return self.product.name;
    
    def unit_price(self):
        return self.product.price;
        
    def cost(self):
        return self.unit_price() * self.quantity
        
    def __repr__(self):
        return f"{self.product}Quantity: {self.quantity}\n"

class Customer:

    def __init__(self, path):
        self.shopping_list = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.name = first_row[0]
            self.budget = float(first_row[1])
            for row in csv_reader:
                name = row[0]
                quantity = float(row[1])
                p = Product(name)
                ps = ProductStock(p, quantity)
                self.shopping_list.append(ps) 
                
    def calculate_costs(self, shop_stock):
        for i in shop_stock:
            for j in self.shopping_list:
                if (j.name() == i.name()):
                    j.product.price = i.unit_price()
    
    def order_cost(self):
        cost = 0
        for i in self.shopping_list:
            cost += i.cost()
        return cost
    
    def __repr__(self):
        print('')
        str = f"{self.name} wants to buy the following:\n"
        for item in self.shopping_list:
            cost = item.cost()
            str += f"\n{item}"
            if (cost == 0):
                str += f"Apologies {self.name}, there's no price available for {item.product.name}\n"
            else:
                str += f"Total cost: {round(cost,2)}\n"
                
        str += f"\nThe cost would be: {round(self.order_cost(),2)}, you would have {round(self.budget - self.order_cost(),2)} left"
        return str 
        
class Shop:
    
    def __init__(self, path):
        self.stock = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.name = str(first_row[0])
            self.cash = float(first_row[1])
            for row in csv_reader:
                p = Product(row[0], float(row[1]))
                ps = ProductStock(p, float(row[2]))
                self.stock.append(ps)

    def check_shop(self, customer_shopping_list):
        stock = self.stock
        for i in stock:
            shop_item_name = i.product.name
            if shop_item_name == customer_shopping_list:
                return i

    def online_order(self, customer):
        total_cost = 0
        shop_balance = self.cash
        customer_balance = customer.budget
        print('')
        print('-'*30)    
        print(f'The shop has a balance of: {round(shop_balance,2)}')
        print(f'{customer.name} has a balance of: {round(customer_balance,2)}')
        print('-'*30)

        order = customer.shopping_list
        for customer_wants in order:
            customer_item_name = customer_wants.product.name

        # check if product on customers order is in the shop
            shop_has = Shop.check_shop(self, customer_item_name)
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
                print(f"Insufficient funds for {customer_item_name}, you're short by {balance} funds available is {round(customer.budget,2)}")
            else:
                customer.budget -= purchase_cost
                self.cash += purchase_cost
        print('')
        print('-'*30)
        print(f'New shop balance is {round(self.cash,2)}')
        print(f'New customer balance is {round(customer.budget,2)}')
        print('-'*30)
        print('')          

    def live_order_details():
        item = input(str("Choose an item: "))
        quantity = int(input("Choose a quantity: "))
        #budget = float(input("Enter budget: "))
        #c = Customer(name, float(budget))
        p = Product(item)
        ps = ProductStock(p, quantity)
        c = Customer(item, quantity)
        c.shopping_list.append(ps)
        return c

    def live_order(self, customer):
        total_cost = 0
        shop_balance = self.cash
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
            shop_has = Shop.check_shop(self, customer_item_name)
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
                self.cash += purchase_cost
        print('')
        print('-'*30)
        print(f'New shop balance is {round(self.cash,2)}')
        print(f'New customer balance is {round(customer_balance,2)}')
        print('-'*30)
        print('')

def display_menu():
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

selectCustomer = input("Select Customer: A, B, C, D or E: ")
#customer = Customer("../"+selectCustomer+".csv")
shop = Shop("../stock.csv")

def main():
    display_menu()
    while True:
        choice = input("Choice: ")
        if (choice == "1"):
            print('')
            print('-'*50)
            print(f'{shop.name} shop balance is {shop.cash}')
            print('-'*50)
            display_menu()
        elif (choice == "2"):
            print('')
            print('-'*50)
            print(f'The shop currently has the following stock:')
            print('-'*50)
            for i in shop.stock:
                print(i)
            print('-'*50)
            display_menu()
        elif (choice == "3"):
            customer = Customer("../"+selectCustomer+".csv")
            print(f"Hi {customer.name}, welcome to {shop.name} Shop")
            print(f'\nHi {customer.name}, welcome to {shop.name}')
            print(f'\n{customer.name}s budget is {customer.budget}')
            customer.calculate_costs(shop.stock)
            print(customer)
            display_menu()
        elif (choice == "4"):
            customer = Customer("../"+selectCustomer+".csv")
            print('')
            print('-'*50)
            print(f'{customer.name} wants to place the following order:')
            print('-'*50)
            customer.calculate_costs(shop.stock)
            Shop.check_shop(shop, customer.shopping_list)
            Shop.online_order(shop, customer)
            display_menu()
        elif (choice == "5"):
            live_customer = Shop.live_order_details()
            Shop.live_order(shop, live_customer)
            display_menu()
        elif (choice == "x"):
            break
        else:
            display_menu()

if __name__ == "__main__":
	main()