/*
 * Bubble sort is of order n2
 * every time inner loop finished one iteration, one element comes to its
 * correct position starting from largest to smallest meaning 1st iteration
 * largest number comes to its position i.e the end and the next largest and the
 * next until all elemnts move to their positions which is why there is outer
 * loop.
 */

#include <iostream>
#include <utility>
#include <vector>

std::vector<int> &bubble_On2(std::vector<int> &list) {
  for (int i = 0; i < list.size(); i++) {
    for (int j = 0; j < list.size() - 1; j++) {
      if (list[j] > list[j + 1]) {
        std::swap(list[j], list[j + 1]);
      }
    }
  }
  return list;
}

int main() {
  std::vector<int> l = {9, 3, 8, 2};
  l = bubble_On2(l);
  for (int i : l) {
    std::cout << i << " ";
  }
  std::cout << std::endl;
}
