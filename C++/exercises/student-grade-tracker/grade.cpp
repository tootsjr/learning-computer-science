#include "grade.h"
#include <iostream>
#include <vector>

std::vector<double> inputGrades(void) {

  std::vector<double> grades{};

  std::cout << "Enter Math grade : ";
  double math{0};
  std::cin >> math;

  std::cout << "Enter an English grade : ";
  double english{0};
  std::cin >> english;

  std::cout << "Enter a Science grade : ";
  double science{0};
  std::cin >> science;

  grades.push_back(math);
  grades.push_back(english);
  grades.push_back(science);

  return grades;
}

double average(const std::vector<double> &grades) {

  double sum{};

  for (double i : grades) {
    sum += i;
  }

  return sum / grades.size();
}

char gradeConverter(double average) {

  char letterAverage{};

  if (average >= 90) {
    letterAverage = 'A';
  } else if (average >= 80) {
    letterAverage = 'B';
  } else if (average >= 70) {
    letterAverage = 'C';
  } else if (average >= 60) {
    letterAverage = 'D';
  } else if (average < 60) {
    letterAverage = 'F';
  }

  return letterAverage;
}

void displayResults(double average, char letterAverage) {

  std::cout << "average : " << average << '\n'
            << "letter average : " << letterAverage << std::endl;
}
