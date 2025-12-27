#include <stdio.h>
#include <cs50.h>

void space(int height);
void brick(int height);

int main(void)
{
  int height;
  do
  {
    height = get_int("What height should the pyramids be? ");
  } while (height < 1 || height > 8);
  for (int i = 0; i < height; i++)
  {
    space(height - i);
    brick(i);
    printf("  ");
    brick(i);
    printf("\n");
  }
}

void space(int height)
{
  for (int j = height; j > 1; j--)
  {
    printf(" ");
  }
}

void brick(int i)
{
  for (int k = 0; k < i + 1; k++)
  {
    printf("#");
  }
}
