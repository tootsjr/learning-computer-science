#include "converter.h"
#include <iostream>

int main() {

  displayMenu();

  int choice{0};
  std::cin >> choice;
  switch (choice) {
  case 1: {
    std::cout << "Celsius : ";
    double celsius{0};
    std::cin >> celsius;
    double fahrenheit{celsiusToFahrenheit(celsius)};
    std::cout << fahrenheit << "\n";
    break;
  }
  case 2: {
    std::cout << "Meters : ";
    double meters{0};
    std::cin >> meters;
    double feet{metersToFeet(meters)};
    std::cout << feet << "\n";
    break;
  }
  case 3: {
    std::cout << "Kilos : ";
    double kilograms{0};
    std::cin >> kilograms;
    double pounds{kilogramsToPounds(kilograms)};
    std::cout << pounds << "\n";
    break;
  }
  default:
    std::cout << "Invalid choice\n";
  }
  return 0;
}
