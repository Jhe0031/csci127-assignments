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
		double sqr = sqrt(dis);
		// std::cout << "sqrt(dis): " << sqr << "\n";
		double bottom = 2*a;
		// std::cout << "2*a: " << bottom << "\n";
		b = b*(-1);
		// std::cout << "-b: " << b << "\n";
		double top = (b+sqr);
		// std::cout << "top: " << top << "\n";
		total = top / bottom;
		std::cout << "Quadtratic Formula: " << total << "\n";
	} else if (dis < 0) {
		total = 0;
		std::cout << "Quadtratic Formula: " << 0 << "\n";
	}
}

int main() {
	srand(time(NULL));
	int x = rand()%10;
	int y = rand()%30;
	int z = rand()%20;
	std::cout << "a=" << x << ", b=" << y << ", c=" << z << "\n";
	int disc = discriminant(x, y, z);
	std::cout << "Discriminant: " << disc << "\n";
	int solve = quadsolve(x, y, z);
	// std::cout << "Quadtratic Formula: " << solve << "\n";
	return 0;
}

