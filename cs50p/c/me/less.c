#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        printf("Number between 1 and 8: ");
        scanf("%d", &n);
    }
    while (n < 1 || n > 8);

    for (int i = 1; i <= n; i++)
    {
        // These loops signifies what happens to each row during each iteration
        // This one prints the spaces in each row by 'n' (height) - 'i' (current row)
        for (int j = 0; j < n - i; j++)
        {
            printf(" ");
        }
        // This row prints a '#' for each non-space (" ")
        // EX: n=7 , i= 5 -> 7-5=2 , the 2 means 2 spaces, and the other 5 integers are represented
        // as '#' because there are 7 rows; first the spaces are created, and then the '#' are
        // created
        for (int k = 0; k < i; k++) //
        {
            printf("#");
        }
        // Creates a double-space between the last '#' of the row...
        printf("  ");
        // before adding on more '#'
        for (int k = 0; k < i; k++) // i=1 and k=0, therefore, as long as the loop runs, the argument 'k<1' will
                  // always be true and it will always add 1-'#' until it's = to 'i' because the
                  // argument 'k++' tells it to. If i=1 -> k=0 , print one hash because k is < i
                  // ('0' is k's starting value). If i=3 -> k= 0,1,2, print 3 hashes. I didn't add a
                  // 'space'-loop before this side of the pyramid because the '#'s start on the left
                  // side of this side of the pyramid, and there are already 2 spaces separating the
                  // two sides of the pyramid (left side of pyramid is right-leaning, while right
                  // side of pyramid is left-leaning).
        {
            printf("#");
        }
        printf("\n"); // this is so after every row, a new row following the same instructions can
                      // be created.
    }
}
