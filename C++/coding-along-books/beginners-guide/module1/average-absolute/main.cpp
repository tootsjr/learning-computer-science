#include <cmath>
#include <iostream>

// int main (){
//
//   std::cout << "Enter 5 values each seperated by a space or a return ";
//   float v1{}, v2{}, v3{}, v4{}, v5{};
//   std::cin >> v1 >> v2 >> v3 >> v4 >> v5;
//
//   double sum {std::abs(v1) + std::abs(v2) + std::abs(v3) + std::abs(v4) +
//   std::abs(v5)}; double average {sum / 5};
//
//   std::cout << average << std::endl;
//
//   return 0;
// }

int main() {
  std::cout << "How many numbers would you like to enter ? ";
  int numbers;
  std::cin >> numbers;

  if (numbers == 0) {
    return 1;
  }

  int total{};

  for (int i{0}; i < numbers; i++)

  {
    std::cout << "Enter a number : ";
    int input{};
    std::cin >> input;
    total += std::abs(input);
  }

  double average = static_cast<double>(total) / numbers;
  std::cout << average;
}
