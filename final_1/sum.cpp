#include <iostream>
#include <cstdlib>

int sumofsquares(int a, int b){
	int sum;
	for (int i = a; i <= b; ++i) {
		sum = sum + (i*i);
	}
	return sum;
}

int main() {
	int sum = sumofsquares(5, 10);
	std::cout << "5 -> 10: " << sum << "\n";
	int sum2 = sumofsquares(10, 15);
	std::cout << "10 -> 15: " << sum2 << "\n";
	int sum3 = sumofsquares(1, 10);
	std::cout << "1 -> 10: " << sum3 << "\n";
	return 0;
}