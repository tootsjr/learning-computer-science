#include <iostream>

void checkNum(int num);

int main() {

  for (int i{0}; i <= 20; i++) {
    checkNum(i);
  }

  return 0;
}

void checkNum(int num) {

  if (num % 3 == 0 && num % 5 == 0) {
    std::cout << "FizzBuzz" << '\n';
  }

  else if (num % 3 == 0) {
    std::cout << "Fizz" << '\n';
  }

  else if (num % 5 == 0) {
    std::cout << "Buzz" << '\n';
  } else {
    std::cout << num << '\n';
  }
}
