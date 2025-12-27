#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

void cypher(char *argv, char plaintext[1000], int size);

int main(int argc, char *argv[])
{
  char plaintext[1000];
  if (argc > 2)
  {
    printf("Usage: ./caesar key\n");
    return 1;
  }
  for (int i = 0; i < strlen(argv[1]); i++) // this for loop iterates through the 2nd argument put into the terminal the one that comes after ./cesar, a command line argument is always stored in a array of strings in C.
  {
    if (!isdigit(argv[1][i]) || argv[1][i] < 1) // This loop checks if each character is a digit. If it finds a non-digit, it prints an error message and exits the program with return 1.
    {
      printf("Usage: ./caesar key\n");
      return 1;
    }
  }
  cypher(argv[1], plaintext, sizeof(plaintext));
}

void cypher(char *argv, char plaintext[1000], int size) // in this function we are going to cypher the text that we are going to get with fgets using the key we obtained using the commnand line args.
{
  printf("Text :\n");
  fgets(plaintext, size, stdin);              // fgets instead of scanf for spaces
  plaintext[strcspn(plaintext, "\n")] = '\0'; // takes the \n and puts it at position \0 so it is not taken into account

  char cyphertext[1000];

  int key = atoi(argv); // atoi converts the current string into an int so we can use that number as the key
  int i;
  for (i = 0; i < strlen(plaintext); i++)
  {
    if (isalpha(plaintext[i])) // we will be checking if the current string is infact text and not any other chracter, so we avoid changing punctiation or something else
    {
      cyphertext[i] = plaintext[i] + key; // this defines cyphertext as the plain text with the key
      if (isupper(plaintext[i]))          // we will check if the character that we have added our key to has gone over Z for both upper and lowercase
      {
        cyphertext[i] = (plaintext[i] - 'A' + key) % 26 + 'A'; // if so we take our current character, take away A or 65 to get the position of the chracter in the normal alphabet, we will then see the rest of the devision by 26, if it is 27 it will return 1 if it is 3 it will be 3. And then add A back to get to the right position.
      }
      else if (islower(plaintext[i]))
      {
        cyphertext[i] = (plaintext[i] - 'a' + key) % 26 + 'a';
      }
    }
    else
    {
      cyphertext[i] = plaintext[i];
    }
  }
  cyphertext[i] = '\0';
  printf("ciphertext: %s\n", cyphertext);
}
