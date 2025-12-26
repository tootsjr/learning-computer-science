#include <iostream>
#include <fstream>
#include <string>

void addToList(std::fstream &myFile);
void printList(std::fstream &myFile);

int main()
{

  std::fstream myFile;

  std::cout << "What would you like to do :" << '\n'
            << "list everything(1)," << '\n'
            << "add something (2)," << '\n'
            << "update status (3) or " << '\n'
            << "delete something (4)" << '\n'
            << "Enter the number here: ";

  int choice{};
  std::cin >> choice;

  if (choice == 1)
  {
    printList(myFile);
  }
  else if (choice == 2)
  {
    addToList(myFile);
  }

  return 0;
}

void addToList(std::fstream &myFile)
{
  myFile.open("sample.txt", std::ios::app);

  if (myFile.is_open())
  {
    std::cout << "Enter next thing todo: ";
    std::string list_item{};
    std::cin.ignore();
    getline(std::cin, list_item);

    myFile << list_item << std::endl;
  }
  else
  {
    std::cout << "the file failed to open";
  }
  myFile.clear();
  myFile.close();
}

void printList(std::fstream &myFile)
{
  myFile.open("sample.txt", std::ios::in);
  if (myFile.is_open())
  {
    std::string list_item{};
    int lineNumber{1};
    while (getline(myFile, list_item))
    {
      std::cout << lineNumber++ << ". " << list_item << std::endl;
    }
  }
  else
  {
    std::cout << "the file failed to open";
  }
  myFile.clear();
  myFile.close();
}
