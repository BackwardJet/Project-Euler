#include <iostream>

int sumOfMultiples(int number) {
    int sum = 0;
    for (int i = 1; i < number; i++) {
        if ((i % 3 == 0) || (i % 5 == 0)) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    
    std::cout << sumOfMultiples(10) << std::endl; // 23

    std::cout << sumOfMultiples(1000) << std::endl; // 233168   

    return 0;
}
