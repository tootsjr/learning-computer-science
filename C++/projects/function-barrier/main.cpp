#include <iostream>

void addFive(int *ptr);

int main() {

  int a{1};

  addFive(&a);

  std::cout << a;

  return 0;
}

void addFive(int *ptr) { *ptr += 5; }
