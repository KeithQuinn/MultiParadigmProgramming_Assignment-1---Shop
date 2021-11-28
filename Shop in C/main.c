#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Product {
	char* name;
	double price;
};

struct ProductStock {
	struct Product product;
	int quantity;
};

struct Shop {
	char* shopName;
	double cash;
	struct ProductStock stock[20];
	int index;
};

struct Customer {
	char* customerName;
	double budget;
	struct ProductStock shoppingList[10];
	//struct CustomerOrder order[20];
	int index;
};

struct Shop createAndStockShop(){
    FILE *fp = fopen("../stock.csv", "r");
    //char * line = NULL;
    if(fp == NULL) {
    perror("Unable to open file!");
    exit(1);
    }

    char chunk[128];

    fgets(chunk, sizeof(chunk), fp);
    char *sn = strtok(chunk, ",");
    char * shopName= malloc(sizeof(char) * 50);
    strcpy(shopName, sn);
    char *c = strtok(NULL, ",");
    double cash = atof(c);
    //printf("Cash in shop is %.2f\n", cash);
    struct Shop shop = {shopName, cash};

    while(fgets(chunk, sizeof(chunk), fp) != NULL) {
    //fputs(chunk, stdout);
    char *n = strtok(chunk, ",");
    char *p = strtok(NULL, ",");
    char *q = strtok(NULL, ",");

    char *name = malloc(sizeof(char) * 50);
    strcpy(name, n);
    double price = atof(p);
    int quantity = atoi(q);

    struct Product product = {name, price};
    struct ProductStock stockItem = {product, quantity};
    shop.stock[shop.index++] = stockItem;
    //printf("NAME OF PRODUCT %s PRICE IS %.2f QUANTITY IS %d\n", name, price, quantity);
    }

    return shop;
}

struct Customer createCustomer(){
    FILE *fp = fopen("../customer.csv", "r");
    //char * line = NULL;
    if(fp == NULL) {
    perror("Unable to open file!");
    exit(1);
    }

    char chunk[128];

    fgets(chunk, sizeof(chunk), fp);
    char *cn = strtok(chunk, ",");
    char * customerName= malloc(sizeof(char) * 50);
    strcpy(customerName, cn);
    char *c = strtok(NULL, ",");
    double cash = atof(c);
    //printf("Cash in shop is %.2f\n", cash);
    struct Customer customer = {customerName, cash};

    while(fgets(chunk, sizeof(chunk), fp) != NULL) {
    //fputs(chunk, stdout);
    char *n = strtok(chunk, ",");
    //char *p = strtok(NULL, ",");
    char *q = strtok(NULL, ",");

    char *name = malloc(sizeof(char) * 50);
    strcpy(name, n);
    //double price = atof(p);
    int quantity = atoi(q);

    //struct Customer customer = {product, quantity};
    //struct CustomerOrder orderItem = {product, quantity};
    //customer.order[customer.index++] = orderItem;

    struct Product product = {name};
    struct ProductStock stockItem = {product, quantity};
    customer.shoppingList[customer.index++] = stockItem;
    //printf("NAME OF PRODUCT %s QUANTITY IS %d\n", product, quantity);
    }

    return customer;
}

void printProduct(struct Product p){
	printf("PRODUCT NAME:%s\nPRODUCT PRICE: %.2f\n", p.name, p.price);
}

void printCustomer(struct Customer c){
	printf("The customer %s has a balance of %.2f in cash and wants to order the following:\n\n", c.customerName, c.budget);
	for (int i = 0; i < c.index; i++)
	{
		printProduct(c.shoppingList[i].product);
		printf("%s ORDERS %d OF THE ABOVE PRODUCT\n", c.customerName, c.shoppingList[i].quantity);
		double cost = c.shoppingList[i].quantity * c.shoppingList[i].product.price;
		printf("The cost to %s will be %.2f\n\n", c.customerName, cost);

		//printOrder(c.order[i].order);
		//printf("%s wants %d of the above\n", c.customerName, c.order[i].quantity);
		//double value;
        //value = c.order[i].quantity;
		//printf("At a total cost of %.2f\n\n", value);
	}
}

void printShop(struct Shop s){
	printf("%s shop has a total of %.2f in cash and has the following stock:\n\n", s.shopName, s.cash);
	//printf("|------------------------------------------|\n");
	for (int i = 0; i < s.index; i++)
	{
		printProduct(s.stock[i].product);
		printf("The shop has %d of the above\n", s.stock[i].quantity);
		double value;
        value = s.stock[i].quantity * s.stock[i].product.price;
		printf("With a total value of %.2f\n\n", value);
	}
}

struct checkShop {
    struct Shop createAndStockShop;
    struct Customer createCustomer;
};


int main(void){

    //struct Shop checkStock = checkShop(struct Shop createAndStockShop(), struct Customer createCustomer())

    struct Shop shop = createAndStockShop();
	printShop(shop);

    struct Customer customer = createCustomer();
    printCustomer(customer);

    //struct Product p1 = { "Stock1", 100 };
    //struct ProductStock p1Stock = { p1, 20 };
	//struct Shop shop2 = { "The new", 25 };
	//printf("%s shop has a total of %.2f in cash and has the following stock:\n%s, QTY: %d", shop2.shopName, shop2.cash, p1Stock.product.name, p1Stock.quantity);
	//double value;
	//value = p1Stock.quantity * p1Stock.product.price;
	//printf("\nWith a price of of %.2f\n\n", p1Stock.product.price);
	//printf("\nWith a total value of %.2f\n\n", value);
    //printShop(shop2);
}





















//struct Order {
//	char* name;
//};

//struct CustomerOrder {
//	struct Order order;
//	int quantity;
//};

//void printProduct(struct Product o){
//	printf("PRODUCT NAME: %s\n", o.name);
//}
