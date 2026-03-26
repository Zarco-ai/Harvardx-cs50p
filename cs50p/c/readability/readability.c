

#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    // Get text input from the user
    string text = get_string("Text: ");

    // Initialize counters for letters, words, and sentences
    int letters = 0;
    int words = 1; // Start at 1 because the first word isn't preceded by a space
    int sentences = 0;

    // Iterate through each character of the text to count letters, words, and sentences
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // Count letters using isalpha() from the <ctype.h> library
        if (isalpha(text[i]))
        {
            letters++;
        }
        // Count words by finding spaces
        else if (isspace(text[i]))
        {
            words++;
        }
        // Count sentences by finding '.', '!', or '?'
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
    }

    // Calculate L and S for the Coleman-Liau index
    // L = average number of letters per 100 words
    // S = average number of sentences per 100 words
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;

    // Apply the Coleman-Liau formula to calculate the index
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // Round the index to the nearest integer
    int grade_level = round(index);

    // Print the appropriate grade level based on the rules
    if (grade_level >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade_level < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade_level);
    }
}
