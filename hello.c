#include "hello.h"

struct _PrLicenseInfo
{
    unsigned char LFVersion;
    char AC[32];
    //char LicenseEnforcementFlag[2];
    //char ApplicationName[3];
    //char ProductCode[3];
    //char LanguageVersion[2];
    //char VersionType[2];
    //char OSVersion[3];
    //char BUCode[3];
    //char GracePeriod[2];
    //char ExpirationDate[9];
    //char SequenceNumber[9];
    //char SeatsNumber[7];
};
 
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

int test_st(const PrLicenseInfo* info)
{
    printf("LFVersion: %d\n", info->LFVersion);
    printf("AC: %s\n", (info->AC));
    return 0;
}
