// veirifica si los numeros son pares o impares
#include <stdio.h>

void countNumbers(int[], int);

int main(void){
	int numbers[5] = {2,88,92,15,13};

	countNumbers(numbers, 5);
}

void countNumbers(int numbers[], int size){
	int count = 0;

	for (int i = 0; i < size; i++){
		if (numbers[i] % 2 != 0) 
			count++;
	}

	printf(" hay %d numeros impares \n", count);
}

/* guardado 