#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int kadanes_On3(const std::vector<int> &list) {
  int result = 0;
  for (int i = 0; i < list.size(); i++) {
    for (int j = i; j < list.size(); j++) {
      int sum = 0;
      for (int z = i; z <= j; z++) {
        sum += list[z];
      }
      result = std::max(sum, result);
    }
  }
  return result;
}

int kadanes_On2(const std::vector<int> &list) {
  int result = 0;
  for (int i = 0; i < list.size(); i++) {
    int sum = 0;
    for (int j = i; j < list.size(); j++) {
      sum += list[j];
      result = std::max(result, sum);
    }
  }
  return result;
}

int kadanes_On1(const std::vector<int> &list) {
  int result = 0;
  int sum = 0;
  for (int i = 0; i < list.size(); i++) {
    sum = std::max(sum + list[i], list[i]);
    result = std::max(result, sum);
  }
  return result;
}

int main() {
  std::vector<int> l;
  int temp;
  std::cout << "Enter some series of integers ending with 0." << std::endl;
  while (true) {
    std::cin >> temp;
    if (temp == 0) {
      break;
    }
    l.push_back(temp);
  }
  if (l.size() > 0) {
    int r1 = kadanes_On1(l);
    /* int r2 = kadanes_On2(l); */
    /* int r3 = kadanes_On3(l); */

    std::cout << "kadane's O(1) result: " << r1 << std::endl;
    /* std::cout << "kadane's O(2) result: " << r2 << std::endl; */
    /* std::cout << "kadane's O(3) result: " << r3 << std::endl; */
  } else {
    std::cout << "No arguments passed." << std::endl;
  }
  return 0;
}
