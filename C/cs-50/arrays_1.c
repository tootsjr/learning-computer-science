#include <stdio.h>

#define size 5

int main(void)
{
  int arr[size];
  arr[0] = 1;

  printf("%i\n", arr[0]);

  for (int i = 1; i < size; i++)
  {
    arr[i] = arr[i - 1] * 2;
    printf("%i\n", arr[i]);
  }
}
