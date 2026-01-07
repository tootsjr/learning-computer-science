#include <iostream>

int main() {

  // here you assign two intergers

  int a{21};
  int b{17};

  // we then create two pointers with * assign them with the address of a and b
  // using & since these pointers point to the adress of a or b, if we change
  // the value of the pointer, we also change the value of the variable at that
  // address

  int *ptrA{&a};
  int *ptrB{&b};

  int temp = *ptrA;

  *ptrA = *ptrB;
  *ptrB = temp;

  std::cout << a << *ptrA;

  return 0;
}
