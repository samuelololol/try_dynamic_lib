#include "hello.h"
void test_v()
{
    printf("im hello_v\n");
}

int test_i()
{
    return 42;
}

int test_cp(const char* char_string)
{
    char* new_cp = (char*) malloc(sizeof(char)*4);
    new_cp[0] = char_string[0];
    new_cp[1] = char_string[1];
    new_cp[2] = char_string[2];
    new_cp[3] = '\0';
    printf("this is first 3 chars in char string: %s\n", new_cp);
    free(new_cp);
    return 0;
}

