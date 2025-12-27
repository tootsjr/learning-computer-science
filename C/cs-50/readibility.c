#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_words(char text[]);
int count_letters(char text[]);
int count_sentences(char text[]);
double coleman_liau(int letters, int words, int sentences);

int main(void)
{
  char text[1000];
  printf("Enter you text:\n");
  fgets(text, 1000, stdin);
  text[strcspn(text, "\n")] = '\0';

  int words = count_words(text);
  int letters = count_letters(text);
  int sentences = count_sentences(text);

  coleman_liau(letters, words, sentences);
}

int count_words(char text[])
{
  int words = 1;
  for (int i = 0; text[i] != '\0'; i++)
  {
    if (text[i] == ' ')
    {

      words++;
    }
  }
  return words;
}

int count_letters(char text[])
{
  int letters = 0;
  for (int i = 0; text[i] != '\0'; i++)
  {
    if (isalpha(text[i]))
    {
      letters++;
    }
  }
  return letters;
}

int count_sentences(char text[])
{
  int sentence = 0;
  for (int i = 0; text[i] != '\0'; i++)
  {
    if (text[i] == '.' || text[i] == '?' || text[i] == '!')
    {

      sentence++;
    }
  }
  return sentence;
}

double coleman_liau(int letters, int words, int sentences)
{
  double average_letters = ((double)letters / words) * 100;
  double average_sentences = ((double)sentences / words) * 100;

  double index = 0.0588 * average_letters - 0.296 * average_sentences - 15.8;

  int grade = round(index);

  if (grade < 1)
    printf("Before Grade 1\n");
  else if (grade >= 16)
    printf("Grade 16+\n");
  else
    printf("Grade %d\n", grade);

  return index;
}
