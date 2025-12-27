#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_LENGTH 75

void vote(char *candidates[]);

int main(int argc, char *argv[])
{
  char *candidates[argc - 1];
  int n = 0;
  int i;
  int length;
  for (i = 0; i < (argc - 1); i++)
  {
    length = strlen(candidates[i]);
    strcpy(candidates[i], argv[i]);

    for (int j = 0; j < length; j++)
      if (isalpha(candidates[i][j]) || candidates[i][j] == ' ')
      {
        n++;
      }
  }
  if (n == length)
  {
    vote(candidates);
  }
  else
  {
    printf("one or more of the characters is not a letter");
  }
}

void vote(char *candidates[])
{
  int voters;
  printf("How many voters : ");
  scanf("%i", &voters);

  char votes[voters][MAX_LENGTH];

  for (int i = 0; i < voters; i++)
  {
    printf("Vote : ");
    scanf("%s", votes[i]);
  }
}
