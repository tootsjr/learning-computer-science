#include <stdio.h>

int main(void)
{
  int n_scores;
  printf("How many scores would you like to enter? ");
  scanf("%d", &n_scores);

  int scores[n_scores];
  float average = 0;

  for (int i = 0; i < n_scores; i++)
  {
    printf("Score %d: ", i + 1);
    scanf("%d", &scores[i]);
  }

  for (int i = 0; i < n_scores; i++)
  {
    average += scores[i];
  }

  printf("Your avg is %f\n", average / n_scores);
}

// #include <stdio.h>
// #include <cs50.h>

// int main (void){
//   int n_scores = get_int("how many scores would you like to enter? ");
//   int scores [n_scores];
//   float average = 0;
//   for (int i = 0; i < n_scores; i++)
//   {
//     scores[i] = get_int("score ");
//   }
//   for (int i = 0; i < n_scores; i++)
//   {
//     average += scores[i];
//   }
//   printf("your avg is %f\n", average / n_scores);
// }
