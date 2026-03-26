#include "helpers.h"
#include <stdlib.h> // For calloc and free

// Helper function to round a float to the nearest int
int round_f(float num)
{
    return (int)(num + 0.5);
}

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all rows
    for (int i = 0; i < height; i++)
    {
        // Loop over all columns
        for (int j = 0; j < width; j++)
        {
            // Get original RGB values as floats to ensure accurate division
            float originalRed = image[i][j].rgbtRed;
            float originalGreen = image[i][j].rgbtGreen;
            float originalBlue = image[i][j].rgbtBlue;

            // Calculate the average of the RGB values, rounding to the nearest integer
            int average = round_f((originalRed + originalGreen + originalBlue) / 3.0);

            // Set all three color values to the calculated average
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all rows
    for (int i = 0; i < height; i++)
    {
        // Loop over all columns
        for (int j = 0; j < width; j++)
        {
            // Get original RGB values as floating-point numbers
            float originalRed = image[i][j].rgbtRed;
            float originalGreen = image[i][j].rgbtGreen;
            float originalBlue = image[i][j].rgbtBlue;

            // Calculate new sepia values using the provided formula
            int sepiaRed = round_f(originalRed * .393 + originalGreen * .769 + originalBlue * .189);
            int sepiaGreen = round_f(originalRed * .349 + originalGreen * .686 + originalBlue * .168);
            int sepiaBlue = round_f(originalRed * .272 + originalGreen * .534 + originalBlue * .131);

            // Cap the values at 255 if they exceed the maximum
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            // Update the pixel with the new sepia values
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate over each row of the image
    for (int i = 0; i < height; i++)
    {
        // Iterate over the first half of the columns
        for (int j = 0; j < width / 2; j++)
        {
            // Create a temporary variable to hold the pixel
            RGBTRIPLE temp = image[i][j];

            // Swap the pixel from the left side with the corresponding pixel on the right side
            image[i][j] = image[i][width - 1 - j];

            // Place the temporary pixel on the right side
            image[i][width - 1 - j] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a temporary copy of the image to read from
    RGBTRIPLE *temp_image = calloc(height * width, sizeof(RGBTRIPLE));
    if (temp_image == NULL)
    {
        return; // Handle memory allocation failure
    }

    // Copy the original image to the temporary array
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp_image[i * width + j] = image[i][j];
        }
    }

    // Loop over all rows
    for (int i = 0; i < height; i++)
    {
        // Loop over all columns
        for (int j = 0; j < width; j++)
        {
            float totalRed = 0.0;
            float totalGreen = 0.0;
            float totalBlue = 0.0;
            int count = 0;

            // Iterate over the 3x3 box of neighboring pixels
            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    // Check if the neighbor pixel is within the image boundaries
                    int row = i + k;
                    int col = j + l;
                    if (row >= 0 && row < height && col >= 0 && col < width)
                    {
                        // Add the color values to the total
                        totalRed += temp_image[row * width + col].rgbtRed;
                        totalGreen += temp_image[row * width + col].rgbtGreen;
                        totalBlue += temp_image[row * width + col].rgbtBlue;
                        count++;
                    }
                }
            }

            // Calculate the average for each color channel and update the pixel
            image[i][j].rgbtRed = round_f(totalRed / count);
            image[i][j].rgbtGreen = round_f(totalGreen / count);
            image[i][j].rgbtBlue = round_f(totalBlue / count);
        }
    }

    // Free the temporary image copy
    free(temp_image);
}
