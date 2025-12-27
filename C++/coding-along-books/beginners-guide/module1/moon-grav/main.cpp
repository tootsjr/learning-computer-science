#include <iostream>

int main (){
  
  double moonPounds {};
  for (int i {1}; i<= 100; i++){
    moonPounds = i * 0.17;
    std::cout << i << "pounds on earth is " << moonPounds << " pounds on the moon" << "\n"; 
    if (i % 25 == 0){
      std::cout << '\n';
    }
  }
  return 0;
}


