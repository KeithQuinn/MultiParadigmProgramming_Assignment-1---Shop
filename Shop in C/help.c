#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Product1 {
	char* name;
	double price;
};

void printProduct1(struct Product1 p){
	printf("PRODUCT NAME: %s \nPRODUCT PRICE: %.2f\n", p.name, p.price);
	//printf("-------------\n");
}

int main(void){
	struct Product1 dominic = { "Dominic", 100.0 };
	printProduct1(dominic);
    return 0;
}
