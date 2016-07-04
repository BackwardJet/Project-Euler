#include<stdio.h>

int sumOfMultiples(int largest) {
    int sum = 0;
    int i;
    for (i = 0; i < largest; i++) {
        if (i % 3 == 0) {
            sum += i;
        }
        else if (i % 5 == 0) {
            sum += i;
        }
    }
    return sum;
}
        

int main() {
    int sum10 = sumOfMultiples(10); // = 23
    int sum1000 = sumOfMultiples(1000); // = 233168
    printf("%i\n",sum10);
    printf("%i\n",sum1000);
}
