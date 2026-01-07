#include <iostream>

class Warehouse {
private:
  int crateCount{0};

public:
  void addCrates(int amount) {
    crateCount += amount;
    std::cout << "you added " << amount << " crates" << std::endl;
  }
  void removeCrates(int amount) {
    if ((crateCount - amount) < 0) {
      std::cout << "you are trying to remove too many crates" << std::endl;
    } else {
      crateCount -= amount;
      std::cout << "you have removed " << amount << " crates" << std::endl;
    }
  }
  void showInventory() { std::cout << crateCount; }
};

int main() {

  Warehouse myStorage;

  myStorage.addCrates(50);
  myStorage.removeCrates(20);
  myStorage.removeCrates(100);

  myStorage.showInventory();

  return 0;
}
