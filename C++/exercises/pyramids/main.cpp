#include <iostream>

void buildPyramidLeft(int height, int row);
void buildPyramidRight(int row);

int main() {

  std::cout << "How tall would you like your pyramid to be ? ";
  int height{};
  std::cin >> height;

  if (height > 0) {
    for (int i{1}; i <= height; i++) {
      buildPyramidLeft(height, i);
      std::cout << "  ";
      buildPyramidRight(i);
    }
  } else {
    std::cout << "the value is not correct" << "\n";
  }

  return 0;
}

void buildPyramidLeft(int height, int row) {

  for (int j{height}; j > row; j--) {
    std::cout << " ";
  }
  for (int k{0}; k < row; k++) {
    std::cout << "#";
  }
}

void buildPyramidRight(int row) {

  for (int k{0}; k < row; k++) {
    std::cout << "#";
  }
  std::cout << '\n';
}
