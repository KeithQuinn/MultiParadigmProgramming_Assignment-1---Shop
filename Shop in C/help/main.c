#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Product {
	char* name;
	double price;
};

void printProduct(struct Product p){
	printf("PRODUCT NAME: %s \nPRODUCT PRICE: %.2f\n", p.name, p.price);
	//printf("-------------\n");
}

struct ProductStock {
	struct Product product;
	int quantity;
};

void printProductStock(struct ProductStock ps){
	printf("PRODUCT NAME: %s \nPRODUCT PRICE: %.2f\nPRODUCT QUANTITY: %d\n", ps.product.name, ps.product.price, ps.quantity);
	//printf("-------------\n");
}




int main(void){

	struct Product productA = { "Runners", 100.0 };
	struct ProductStock stockA = { productA, 10 };
	printProductStock(stockA);


    return 0;
}
