#include <stdio.h>

int sum_of_two_digits(int first_digit, int second_digit) {
    printf("%d",first_digit + second_digit);
}

int main() {
    int a = 0;
    int b = 0;
    scanf("%d%d",&a,&b);
    sum_of_two_digits(a,b);
}
