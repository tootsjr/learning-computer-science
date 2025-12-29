#include <iostream>

int broken_refill(int a) {
  a = 100; // Changes a local COPY
  return a;
}

void real_refill(int *p) {
  *p = 100; // Goes to the address and changes the ORIGINAL
}

int main() {
  int ammo = 10;

  broken_refill(ammo);
  std::cout << "After broken: " << ammo << "\n"; // Still 10

  real_refill(&ammo);
  std::cout << "After real:   " << ammo << "\n"; // Now 100!

  return 0;
}
