#include <iostream>

int main() {

  for (int i{1}; i <= 100; i++) {
    double moonPounds{i * 0.17};
    std::cout << i << " pounds on earth is " << moonPounds
              << " pounds on the moon" << "\n";
    if (i % 25 == 0) {
      std::cout << '\n';
    }
  }
  return 0;
}
