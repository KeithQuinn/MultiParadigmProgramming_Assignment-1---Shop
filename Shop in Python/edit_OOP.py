import csv

from shop_procedural import check_shop

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

    def quantity(self):
        return self.product.quantity;
    
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
                
        str += f"\nThe cost would be: {self.order_cost()}, you would have {round(self.budget - self.order_cost(),2)} left"
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

    def check_stock(self, customer_shopping_list):
        self.product_available = []
        for i in customer_shopping_list:
            for j in self.stock:
                if (j.name() == i.name()):
                    j.product.price = i.unit_price()
                    self.product_available.append(i)

    def order_cost(self):
        cost = 0
        for i in self.product_available:
            cost += i.cost()
        return cost

    def __repr__(self):
        str = ""
        #str += f'\nShop has {self.cash} in cash\n\n'
        for i in self.product_available:
            #print(item)
            cost = i.cost()
            str += f"{i}"
            if (cost == 0):
                str += f"{customer.name} doesn't know how much that costs :("
            else:
                str += f"COST: {round(cost,2)}\n\n"
        
        if customer.order_cost() < customer.budget:
            str += f"The cost would be: {round(customer.order_cost(),2)}, you had {customer.budget}, you have {round(customer.budget - self.order_cost(),2)} left\n"
            str += f"\n\nThe cost would be: {round(customer.order_cost(),2)}, shop balance was {self.cash}, updated to {round(self.cash + self.order_cost(),2)}\n"
            customer.budget = round(customer.budget - self.order_cost(),2)
            self.cash = round(self.cash + self.order_cost(),2)
        else:
            str += f"Insufficient funds"
        
        return str

def display_menu():
    print("")
    print("-" * 30)
    print(f"Hi {customer.name}, welcome to {shop.name} Shop")
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
customer = Customer("../"+selectCustomer+".csv")
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
            print(f'\nHi {customer.name}, welcome to {shop.name}')
            customer.calculate_costs(shop.stock)
            print(customer)
            display_menu()
        elif (choice == "4"):
            print('')
            print('-'*50)
            print(f'{customer.name} wants to place the following order:')
            print('-'*50)
            customer.calculate_costs(shop.stock)
            shop.check_stock(customer.shopping_list)
            shop.quantity_available(customer.shopping_list)
            print(shop)
            print(f'the b is {customer.budget}')
            display_menu()
        elif (choice == "5"):

            display_menu()
        elif (choice == "x"):
            break
        else:
            display_menu()

if __name__ == "__main__":
	main()


#customer = Customer("../A.csv")
#customer.calculate_costs(shop.stock)
#shop.check_stock(customer.shopping_list)
#print(customer)
#print(shop)