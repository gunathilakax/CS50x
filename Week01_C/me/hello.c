#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Get the user name as an input
    string name = get_string("What is Your name? ");

    //Print a greeting message
    printf("Hello, %s\n", name);
}
