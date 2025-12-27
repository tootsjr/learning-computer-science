#include <stdio.h>
#include <string.h>
#include <ctype.h>

int score_counter(char players[2][100], int scores[2]);
void compare(int scores[2]);

char const score1[10] = {'a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u'};
char const score2[2] = {'d', 'g'};
char const score3[4] = {'b', 'c', 'm', 'p'};
char const score4[5] = {'f', 'h', 'v', 'w', 'y'};
char const score5[1] = {'k'};
char const score8[2] = {'j', 'x'};
char const score10[2] = {'q', 'z'};

int main(void)
{
  char player1[100];
  printf("Player 1: ");
  scanf("%s", player1);

  char player2[100];
  printf("Player 2: ");
  scanf("%s", player2);

  char players[2][100];
  strcpy(players[0], player1);
  strcpy(players[1], player2);

  int scores[2];

  score_counter(players, scores);
  compare(scores);
}

int score_counter(char players[2][100], int scores[2])
{
  int score;
  for (int i = 0; i < 2; i++)
  {
    score = 0;
    int length = strlen(players[i]);

    for (int j = 0; j < length; j++)
    {
      players[i][j] = tolower(players[i][j]);

      if (players[i][j] == 'a' || players[i][j] == 'e' || players[i][j] == 'i' || players[i][j] == 'l' || players[i][j] == 'n' || players[i][j] == 'o' || players[i][j] == 'r' || players[i][j] == 's' || players[i][j] == 't' || players[i][j] == 'u')
      {
        score += 1;
      }
      else if (players[i][j] == 'd' || players[i][j] == 'g')
      {
        score += 2;
      }
      else if (players[i][j] == 'b' || players[i][j] == 'c' || players[i][j] == 'm' || players[i][j] == 'p')
      {
        score += 3;
      }
      else if (players[i][j] == 'f' || players[i][j] == 'h' || players[i][j] == 'v' || players[i][j] == 'w' || players[i][j] == 'y')
      {
        score += 4;
      }
      else if (players[i][j] == 'k')
      {
        score += 5;
      }
      else if (players[i][j] == 'j' || players[i][j] == 'x')
      {
        score += 8;
      }
      else if (players[i][j] == 'q' || players[i][j] == 'z')
      {
        score += 10;
      }
      else
      {
        score += 0;
      }
    }
    scores[i] = score;

  }
  printf("%i %i\n", scores[0], scores[1]);
  return 0;
}

void compare(int scores[2])
{
  if(scores[0] > scores[1]){
    printf("player 1 wins\n");
  }
  else if(scores[1] < scores[0])
  {
    printf("player 2 wins\n");
  }
  else{
    printf("tie\n");
  }
}

// 1 point : A E I L N O R S T U
// 2 points : D G
// 3 points : B C M P
// 4 points : F H V W Y
// 5 points : K
// 8 points : J X
// 10 points : Q Z
