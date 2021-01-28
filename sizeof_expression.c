#include <stdio.h>

int main()
{
    double f = 3.14;
    // if Sizeof-expression: sizeof Cast-expression
    // then the following statement is valid
    size_t s = sizeof (int)f;
    // otherwise if you have to do
    size_t t = sizeof ((int)f);
    // then sizeof-expression: sizeof unary-expression
    // this might be useful only to people who needs to write a C compiler/intepreter
    printf("%zd\n", s);
}
