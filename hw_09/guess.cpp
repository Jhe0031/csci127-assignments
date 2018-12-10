#include <iostream>
#include <stdlib.h>
#include <cstdlib>

int main()
{
	int i;
	int g;
	int rand();
	int num;
	srand (time(NULL));
	g = rand()%100;
	std::cout << "Please enter an integer from 0 to 99, inclusive: ";
	std::cin >> i;
	std::cout << "Is this your number: " << g << "?\n";
	std::cout << "Please enter '-1' if your number is lower\n";
	std::cout << "Please enter '1' if your number is higher\n";
	std::cout << "Please enter '0' if this is your number\n";
	std::cin >> num;
	while (g != i)
	{
		if (num == 0) {
			std::cout << "Your number is " << g << "! Yay!\n";
			break;
		} else if (num == -1) {
			std::cout << "Is this your number: " << g-1 << "?\n";
			g = g-1;
			std::cin >> num;
		} else if (num == 1) {
			std::cout << "Is this your number: " << g+1 << "?\n";
			g = g+1;
			std::cin >> num;
		} else {
			std::cout << "So you want to stop using 1's I see.\n";
			g = g+num;
			std::cout << "Is this your number: " << g << "?\n";
			std::cin >> num;
		}
	}
	if (g == i)
	{
		std::cout << "Your number is " << g << ". Yay!\n";
	}
	return 0;
}