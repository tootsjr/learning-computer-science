#include <iostream>

int main() {

  int a{21};
  int b{17};

  int *ptrA{&a};
  int *ptrB{&b};

  int temp = *ptrA;

  *ptrB = temp;

  std::cout << a << *ptrA;

  return 0;
}
