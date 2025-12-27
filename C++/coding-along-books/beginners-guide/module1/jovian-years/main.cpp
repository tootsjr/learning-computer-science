#include <iostream>

int main (){
  std::cout << "How many earth years ? ";
  double earthYears{};
  std::cin >> earthYears;

  double jovianYears { earthYears * 12 };

  std::cout << jovianYears; 

  return 0;
}
