#include <stdio.h>
#include <cs50.h>

int main(void)
{
  int x = get_int("what would you like x to be?\n");
  int y = get_int("What would you like y to be?\n");

  if (x < y)
  {
    printf("x is smaller than y\n");
  }
  else if (x > y)
  {
    printf("x is bigger than y\n");
  }
  else
  {
    printf("x and y are equal\n");
  }
}
