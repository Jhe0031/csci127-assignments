#include <iostream>
#include <cstdlib>
#include <math.h>

int discriminant(int d, int e, int f) {
	int sum;
	sum = (e*e)-(4*d*f);
	return sum;
}

int quadsolve(int a, int b, int c) {
	int dis;
	dis = discriminant(a, b, c);
	double total;
	if (dis >= 0) {
		total = (-b + (sqrt(dis)))/(2*a);
		std::cout << "Quadtratic Formula: " << total << "\n";
	} else if (dis < 0) {
		total = 0;
		std::cout << "Quadtratic Formula: " << 0 << "\n";
	}
}

int main() {
	srand(time(NULL));
	int x = rand()%25;
	int y = rand()%50;
	int z = rand()%30;
	std::cout << "a=" << x << ", b=" << y << ", c=" << z << "\n";
	int disc = discriminant(x, y, z);
	std::cout << "Discriminant: " << disc << "\n";
	int solve = quadsolve(x, y, z);
	// std::cout << "Quadtratic Formula: " << solve << "\n";
	return 0;
}

