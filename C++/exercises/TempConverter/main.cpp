#include <iostream>

void printTable(int start, int end, int step);

int main() {

  std::cout << "What would you like to start at ? ";
  int start{};
  std::cin >> start;

  std::cout << "What would you like to end at ? ";
  int end{};
  std::cin >> end;

  std::cout << "How big would you like each step to be ? ";
  int step{};
  std::cin >> step;

  printTable(start, end, step);

  return 0;
}

void printTable(int start, int end, int step) {
  std::cout << "Celsius" << '\t' << "Fahrenheit" << '\n';
  for (int i{start}; i <= end; i += step) {
    double converted{(i * 1.8) + 32};
    std::cout << i << '\t' << converted << '\n';
  }
}
