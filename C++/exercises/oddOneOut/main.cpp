#include <iostream>
#include <vector>

std::vector<int> getEvenNumbers(const std::vector<int> &numberList);

int main() {

  std::vector<int> numbers{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

  std::vector<int> evenNumbers{getEvenNumbers(numbers)};

  for (int i{}; i < evenNumbers.size(); i++) {
    std::cout << evenNumbers[i];
    if (i < evenNumbers.size() - 1) {
      std::cout << " ";
    }
  }

  return 0;
}

std::vector<int> getEvenNumbers(const std::vector<int> &numberList) {

  std::vector<int> evenNumbers{};

  for (int currentNumber : numberList) {
    if (currentNumber % 2 == 0) {
      evenNumbers.push_back(currentNumber);
    }
  }
  return evenNumbers;
}
