#include <iostream>

void checkNum(int number);

int main() {

  std::cout << "what number would you like to check ? ";
  int input{};
  std::cin >> input;
  checkNum(input);
  return 0;
}

void checkNum(int number) {
  if (number < 2) {
    std::cout << "your number is a prime number" << '\n';
    return;
  }
  for (int i{2}; i < number; i++) {
    if (number % i == 0) {
      std::cout << "your number is not primal";
      return;
    }
  }
  std::cout << "your number is a prime number" << '\n';
}
