#include <iostream>
#include <string>
using namespace std;

//const int INT_MAX = 2147485647;
//const int INT_MIN = -2147485647;

int atoi(string str) {
  int len = str.length();
  //cout << len << endl;
  int *digit = new int[len];
  string max  = "2147483647"; 
  int offset = -1;
  bool sign = true;
  int out=0;
  int i;
  int digit_len;
  for (i=0; i<len; i++){
    if (offset < 0) {
      if (str[i]==' ' || str[i] == '0') 
          continue;
      else if (str[i]=='+')
          offset = i+1;
      else if (str[i]=='-') {
          sign = false;
          offset = i+1;
      } else if (str[i] <= '9' && str[i] >= '1') {
        offset = i;
        i--;
      }
      else
        return 0;
      continue;
    }
    if (i==offset && str[i] == '0') {
      offset = i+1;
      continue;
    }  else if (str[i] <= '9' && str[i] >= '0') {
      digit[i-offset] = str[i]-'0';
    } else
      break;
  }
  digit_len = i - offset;
  if (digit_len > 10 || digit_len==10 && str.substr(offset, digit_len) > max) {
    if (sign)
      return 2147483647;
    else
      return -147483648;
  }
  for (i=0;i<digit_len;i++) {
    out = out * 10 + digit[i];
  }
  if (!sign) {
    out = -out;
  }
  return out;
}

int main() {
  string str;
  cin >> str;
  cout << atoi(str) <<endl;
}
