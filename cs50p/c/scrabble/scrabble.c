#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // create an array called letters
    char letters[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    // create an array called letter-values
    int values[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                      1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    // get input and validate answer
    string answer1;
    bool has_invalid_char = false;
    int final_score1 = 0;
    int d = 0;
    do
    {
        has_invalid_char = false; // Reset the flag for each new input
        answer1 = get_string("Player 1: ");
        for (int i = 0, n = strlen(answer1); i < n; i++)
        {
            // Check if the current character is a space or a digit
            if (isspace(answer1[i]) || isdigit(answer1[i]))
            {
                has_invalid_char = true;
                break; // Exit the for loop as soon as an invalid character is found
            }
        }
        if (has_invalid_char == true)
        {
            printf("Invalid input. Please try again.\n");
        }
        if (has_invalid_char == false)
        {
            for (int i = 0, n = strlen(answer1); i < n; i++) // loop through user string
            {
                answer1[i] = tolower(answer1[i]); // This converts user input into lowercase, making
                                                  // it easier to identify characters in the array
                d = answer1[i] - letters[0];
                final_score1 += values[d];
            }
        }
    }
    while (has_invalid_char == true);
    printf("%d\n", final_score1);

    // second user input

    string answer2;
    bool has_invalid_char1 = false;
    int final_score2 = 0;
    int d2 = 0;
    do
    {
        has_invalid_char1 = false; // Reset the flag for each new input
        answer2 = get_string("Player 2: ");
        for (int i = 0, n = strlen(answer2); i < n; i++)
        {
            // Check if the current character is a space or a digit
            if (isspace(answer2[i]) || isdigit(answer2[i]))
            {
                has_invalid_char1 = true;
                break; // Exit the for loop as soon as an invalid character is found
            }
        }
        if (has_invalid_char1)
        {
            printf("Invalid input. Please try again.\n");
        }
        if (has_invalid_char1 == false)
        {
            for (int i = 0, n1 = strlen(answer2); i < n1; i++) // loop through user string
            {
                answer2[i] = tolower(answer2[i]); // This converts user input into lowercase, making
                                                  // it easier to identify characters in the array
                d2 = answer2[i] - letters[0];
                final_score2 += values[d2];
            }
        }
    }
    while (has_invalid_char1 == true);
    printf("%d\n", final_score1);

    if (final_score1 == final_score2)
    {
        printf("tie!\n");
    }
    else if (final_score1 > final_score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (final_score2 > final_score1)
    {
        printf("Player 2 wins!\n");
    }
}
