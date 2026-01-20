#include <iostream>
#include <string>

void validateInfo(double price, double quantity, std::string code);
double calculateValue (double price, double quantity, std::string code);

int main () {
  std::cout << "Enter the price : " << std::endl;
  double price {};
  std::cin >> price;

  std::cout << "Enter the quantity : " << std::endl;
  double quantity {};
  std::cin >> quantity;

  std::cout << "Enter your promo code (n if none): " << std::endl;
  std::string code;
  std::cin >> code;
  
  validateInfo(price, quantity, code);

  return 0;
}


void validateInfo(double price, double quantity, std::string code){
  if (price <= 0 || quantity <= 0){
    std::cout << "The price or quantity you have entered was not valid" << std::endl;
    return;
  }
    double result {calculateValue(price, quantity, code)};
    std::cout << result << std::endl;
}

double calculateValue (double price, double quantity, std::string code){
  double total {price * quantity};
  if (code == "n"){
    //no promo code
  }else if (code == "PROMO"){
    total *= 0.90;
    std::cout << "Code is correct" << std::endl;
  }else{
    std::cout << "The code you have entered is incorrect " << std::endl;
  }if (total < 50){
    total += 2;
  }
  return total;
}
