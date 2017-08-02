#include<iostream>

int f(int x)
{
  static int y = 0;
  y += x;
  return y;
}

int main() {
  /*
  std::cout << f(4) << "\n";
  std::cout << f(4) << "\n";
  std::cout << f(4) << "\n";
  */
  std::cout << std::getchar() << "\n";
}
