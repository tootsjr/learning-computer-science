#include <iostream>

double toFeet(double n);
double toMeters(double n);

int main() {

  std::cout << "What would you like to convert ?" << '\n'
            << "Feet(f) to meters or meters(m) to feet ? ";
  char answer{};
  std::cin >> answer;

  if (answer == 'm') {

    std::cout << "Your value in meters: ";
    double meters{};
    std::cin >> meters;
    double feet = toFeet(meters);
    std::cout << feet << " feet";

  } else if (answer == 'f') {

    std::cout << "Your value in feet: ";
    double feet{};
    std::cin >> feet;
    double meters = toMeters(feet);
    std::cout << meters << " meters";

  } else {

    std::cout << "invalid input";
  }
}

double toFeet(double n) {
  n *= 3.28;
  return n;
}

double toMeters(double n) {
  n /= 3.28;
  return n;
}
