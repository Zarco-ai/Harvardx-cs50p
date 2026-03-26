#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    char letters[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    char letters1[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                         'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    int k = 0; // key for encryption

    string p;
    if (argc == 2)
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (isdigit(argv[1][i]) && argv[1][i] > 0)
            {
            }
            else
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
        k = atoi(argv[1]);
        if (k >= 26)
        {
            k = k % 26;
        }
        else
        {
        }

        p = get_string("plaintext:  "); // Get user String
        // Encryption
        for (int i = 0, n = strlen(p); i < n; i++)
        {
            if (isalpha(p[i]) && isupper(p[i]))
            {
                p[i] = p[i] - letters1[0];
                p[i] = (p[i] + k) % 26;
                p[i] = p[i] + letters1[0];
            }
            if (isalpha(p[i]) && islower(p[i]))
            {
                p[i] = p[i] - letters[0];
                p[i] = (p[i] + k) % 26;
                p[i] = p[i] + letters[0];
            }
            else
            {
            }
        }

        printf("ciphertext: %s\n", p);
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

