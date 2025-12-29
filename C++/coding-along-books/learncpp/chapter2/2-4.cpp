#include <iostream>

int add(int a, int b);
int userInput();

int main() {

  int sum{add(userInput(), userInput())};

  std::cout << sum << '\n';

  return 0;
}

int userInput() {
  std::cout << "enter a value ";
  int num{};
  std::cin >> num;
  return num;
}
// this is a test
int add(int a, int b) { return a + b; }
