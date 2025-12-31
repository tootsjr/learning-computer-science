#include <iostream>
#include <vector>

std::vector<int> updatePrices(const std::vector<int> &oldPrices);

int main() {

  std::vector<int> prices{5, 30, 75, 90, 99, 100, 120, 200};
  std::vector<int> newPrices{updatePrices(prices)};

  for (int i : newPrices) {
    std::cout << "$" << i << "\n";
  }
  return 0;
}

std::vector<int> updatePrices(const std::vector<int> &oldPrices) {

  int current{};
  std::vector<int> updated{};

  for (int i : oldPrices) {
    current = i;
    if (current < 100) {

      current += 5;
    }
    updated.push_back(current);
  }
  return updated;
}
