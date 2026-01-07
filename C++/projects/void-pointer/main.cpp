#include <iostream>

struct Box {
  int id{};
};

void changeId(Box *ptr) { ptr->id = 500; }

int main() {

  Box myBox;
  myBox.id = 5;

  std::cout << "before " << myBox.id << std::endl;

  changeId(&myBox);

  std::cout << "after " << myBox.id << std::endl;

  return 0;
}
