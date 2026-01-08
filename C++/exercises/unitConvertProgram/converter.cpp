#include "converter.h"
#include <iostream>

double celsiusToFahrenheit(double celsius) {

  double fahrenheit{(celsius * 9 / 5) + 32};

  return fahrenheit;
}

double metersToFeet(double meters) {

  double feet{meters * 3.281};

  return feet;
}

double kilogramsToPounds(double kilograms) {

  double pounds{kilograms * 2.2};

  return pounds;
}

void displayMenu() {

  std::cout << "1. celsius to fahrenheit";
  std::cout << "2. meters to feet";
  std::cout << "3. kilograms to pounds";
}
