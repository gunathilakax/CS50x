#include <cs50.h>
#include <stdio.h>

int get_height(void);
void print_row(int height, int bricks);

int main(void)
{
    // Call the get_height function
    int n = get_height();

    // Print a pyramid of that height
    for (int i = 0; i < n; i++)
    {
        // Call the Print_row function
        print_row(n, i + 1);
    }
}

int get_height(void)
{
    // Get user input as the pyramid's height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    return n;
}

void print_row(int height, int bricks)
{
    // Print the spaces
    for (int j = height; j > bricks; j--)
    {
        printf(" ");
    }
    // Print the bricks
    for (int k = 0; k < bricks; k++)
    {
        printf("#");
    }
    printf("\n");
}
