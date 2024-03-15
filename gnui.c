#include <stdio.h>

void printRouthArray(float routhArray[][3], int rows) {
    printf("Routh Array:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%.4f\t", routhArray[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int main() {
    int n = 4; // Degree of the polynomial is n
    float coefficients[] = {1, 2, 5, 80}; // Coefficients of the polynomial, starting from the highest degree

    // Initialize the Routh array
    float routhArray[n][3];

    // Fill in the first row of the Routh array
    for (int i = 0; i < n; i++) {
        routhArray[i][0] = coefficients[i];
    }

    // Fill in the remaining columns of the Routh array
    for (int j = 1; j < 3; j++) {
        for (int i = 0; i < n - j; i++) {
            routhArray[i][j] = (routhArray[i][0] * routhArray[i + 1][j - 1] - routhArray[i + 1][0] * routhArray[i][j - 1])
                               / routhArray[i + 1][0];
        }
    }

    // Print the Routh array
    printRouthArray(routhArray, n);

    // Check for sign changes in the first column
    int signChanges = 0;
    for (int i = 0; i < n - 1; i++) {
        if (routhArray[i][0] * routhArray[i + 1][0] < 0) {
            signChanges++;
        }
    }

    // Determine stability
    if (signChanges == 0) {
        printf("The system is stable (no sign changes in the first column).\n");
    } else {
        printf("The system is unstable (there are %d sign changes in the first column).\n", signChanges);
    }

    return 0;
}

