#ifndef GRADE_H
#define GRADE_H
#include <vector>

std::vector<double> inputGrades(void);
double average(const std::vector<double> &grades);
char gradeConverter(double average);
void displayResults(double average, char letterAverage);

#endif // !GRADE_H
