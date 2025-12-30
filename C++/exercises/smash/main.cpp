#include <iostream>
#include <string>
#include <vector>

void smash(const std::vector<std::string> &words);

int main() {

  std::vector<std::string> words{"hello", "world"};

  smash(words);

  return 0;
}

void smash(const std::vector<std::string> &words) {
  std::string sentence{};

  for (unsigned long i{0}; i < words.size(); i++) {
    sentence += words[i];

    if (i < words.size() - 1) {
      sentence += " ";
    }
  }
  std::cout << sentence;
}
