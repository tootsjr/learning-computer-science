#include <iostream>

int main() {
  double m{};

  for (int i{1}; i <= 100; i++) {
    m = i / 3.28;
    std::cout << i << "feet is " << m << " meters" << '\n';

    if (i % 10 == 0) {
      std::cout << '\n';
    }
  }

  return 0;
}
