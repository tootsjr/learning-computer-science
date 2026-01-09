#include "grade.h"
#include <vector>

int main() {

  std::vector<double> grades{inputGrades()};
  double gradeAverage{average(grades)};
  char letterGrade{gradeConverter(gradeAverage)};
  displayResults(gradeAverage, letterGrade);

  return 0;
}
