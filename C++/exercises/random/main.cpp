#include <cstdlib>
#include <ctime>
#include <iostream>

void play(int high);

int main() {
  srand(time(0));
  char playAgain{};
  do {

    int choice{};
    std::cout << "Select difficulty : 1. Easy, 2. Medium, 3. Hard ";
    if (!(std::cin >> choice)) {
      std::cin.clear();
      std::cin.ignore(10000, '\n');
      std::cout << "Invalid choice, defaulting to Medium";
      choice = 2;
    }

    int high{};

    switch (choice) {
    case 1:
      high = 100;
      break;
    case 2:
      high = 500;
      break;
    case 3:
      high = 1000;
      break;
    default:
      std::cout << "Your selection was invalid, defaulting to Medium";
      high = 500;
    }

    play(high);

    std::cout << "Would you like to play again ? If so press y : ";
    std::cin >> playAgain;

  } while (playAgain == 'y' || playAgain == 'Y');

  std::cout << "Thank you for playing !" << std::endl;

  return 0;
}

void play(int high) {
  int secret = rand() % high + 1;

  std::cout << "Number has been picked !" << std::endl;
  int guess{0};
  int low{1};

  std::cout << "Guess the Number between 1 and " << high << "! ";

  do {

    if (!(std::cin >> guess)) {
      std::cin.clear();
      std::cin.ignore(10000, '\n');
      std::cout << "Invalid input. Please enter a number: ";
      continue;
    }

    if (guess > secret) {
      high = guess;
      std::cout << "Too high guess again ! It's between " << low << " and "
                << high << "! ";

    } else if (guess < secret) {
      low = guess;
      std::cout << "Too low guess again ! It's between " << low << " and "
                << high << "! ";
    }

  } while (guess != secret);

  std::cout << "You have guess correctly ! It was " << secret << '\n';
}
