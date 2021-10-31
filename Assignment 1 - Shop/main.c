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
	double cash;
	struct ProductStock stock[20];
	int index;
};

struct Customer {
	char* name;
	double budget;
	struct ProductStock shoppingList[10];
	int index;
};

void printProduct(struct Product p)
{
	printf("PRODUCT NAME: %s \nPRODUCT PRICE: %.2f\n", p.name, p.price);
	printf("-------------\n");
}

void printCustomer(struct Customer c)
{
	printf("CUSTOMER NAME: %s \nCUSTOMER BUDGET: %.2f\n", c.name, c.budget);
	printf("-------------\n");
	for(int i = 0; i < c.index; i++)
	{
		printProduct(c.shoppingList[i].product);
		printf("%s ORDERS %d OF ABOVE PRODUCT\n", c.name, c.shoppingList[i].quantity);
		double cost = c.shoppingList[i].quantity * c.shoppingList[i].product.price;
		printf("The cost to %s will be €%.2f\n", c.name, cost);
	}
}

struct Shop createAndStockShop()
{
	struct Shop shop = { 500 };
    FILE *fp = fopen("stock.csv", "r");
    char * line = NULL;
    if(fp == NULL) {
    perror("Unable to open file!");
    exit(1);
    }

    char chunk[128];

    while(fgets(chunk, sizeof(chunk), fp) != NULL) {
    //fputs(chunk, stdout);
    char *n = strtok(chunk, ",");
    char *p = strtok(NULL, ",");
    char *q = strtok(NULL, ",");
    double price = atof(p);
    int quantity = atoi(q);
    char *name = malloc(sizeof(char) * 50);
    strcpy(name, n);

    struct Product product = {name, price};
    struct ProductStock stockItem = {product, quantity};
    shop.stock[shop.index++] = stockItem;
    printf("NAME OF PRODUCT %s PRICE IS %.2f QUANTITY IS %d\n", name, price, quantity);
    }

    return shop;
}


struct Customer customer(){
//--------------------- READ IN STOCK FILE ----------------------------
    FILE * customer;
    customer = fopen("customer.csv", "r");
    if (customer == NULL){
        perror("Unable to open the file.");
        exit(1);
    }
    char customer_line[200];
    printf("\nThe shop stock is as follows:\n\n");
    while(fgets(customer_line, sizeof(customer_line), customer)){
            char *name;
            char *budget;
            char *order_product;
            char *quantity;

            name = strtok(customer_line, ",");
            budget = strtok(NULL, ",");
            order_product = strtok(NULL, ",");
            quantity = strtok(NULL, ",");


            printf("NAME OF CUSTOMER IS %s, he has €%s available, he wants to order %s by %s\n", name, budget, order_product, quantity);
            //printf("AMOUNT AVAILABLE %s\n", budget);
            //printf("WANTS TO ORDER A TOTAL %s OF %s", quantity, order_product);

/*
            while(token != NULL){
                printf("%-20s", token);
                token = strtok(NULL, ",");
            }
*/
            printf("\n");
}
};

void printShop(struct Shop s)
{
	printf("Shop has %.2f in cash\n", s.cash);
	for (int i = 0; i < s.index; i++)
	{
		printProduct(s.stock[i].product);
		printf("The shop has %d of the above\n", s.stock[i].quantity);
	}
}

int main(void)
{
	// struct Customer dominic = { "Dominic", 100.0 };
	//
	// struct Product coke = { "Can Coke", 1.10 };
	// struct Product bread = { "Bread", 0.7 };
	// // printProduct(coke);
	//
	// struct ProductStock cokeStock = { coke, 20 };
	// struct ProductStock breadStock = { bread, 2 };
	//
	// dominic.shoppingList[dominic.index++] = cokeStock;
	// dominic.shoppingList[dominic.index++] = breadStock;
	//
	// printCustomer(dominic);

	//struct Shop shop = createAndStockShop();
	//printShop(shop);
    customer();
// printf("The shop has %d of the product %s\n", cokeStock.quantity, cokeStock.product.name);

    return 0;
}
