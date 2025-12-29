#include <iostream>

void calculator(double current, double income, double rate, int years);

int main() {

  std::cout << "What is the current amount in your savings ? ";
  double current{};
  std::cin >> current;

  std::cout << "How much do you earn each month ? ";
  double income{};
  std::cin >> income;

  std::cout << "What is your early interest rate ? ";
  double rate{};
  std::cin >> rate;

  std::cout << "How many years ? ";
  int years{};
  std::cin >> years;

  calculator(current, income, rate, years);
  return 0;
}

void calculator(double current, double income, double rate, int years) {

  int months{years * 12};
  double total{current};
  double monthlyRate = {rate / 12 / 100};

  for (int i{1}; i <= months; i++) {
    total = (total + income) * (1 + monthlyRate);
    if (i % 12 == 0) {
      std::cout << "year: " << i / 12 << " = " << total << '\n';
    }
  }
}
