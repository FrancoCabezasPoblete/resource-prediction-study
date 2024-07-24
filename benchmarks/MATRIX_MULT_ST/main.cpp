#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

void generateRandomMatrix(std::vector<std::vector<int>>& matrix, int size) {
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            matrix[i][j] = rand() % 180; // Genera números aleatorios entre 0 y 179
        }
    }
}

void multiplyMatrices(
    const std::vector<std::vector<int>>& matrixA, 
    const std::vector<std::vector<int>>& matrixB, 
    std::vector<std::vector<int>>& result, 
    int size
) {
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            result[i][j] = 0;
            for (int k = 0; k < size; ++k) {
                result[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }
}

// void printMatrix(const std::vector<std::vector<int>>& matrix, int size) {
//     for (int i = 0; i < size; ++i) {
//         for (int j = 0; j < size; ++j) {
//             std::cout << matrix[i][j] << " ";
//         }
//         std::cout << std::endl;
//     }
// }

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <matrix size>" << std::endl;
        return 1;
    }

    int size = std::atoi(argv[1]);
    if (size <= 0) {
        std::cerr << "Matrix size should be a positive integer." << std::endl;
        return 1;
    }

    std::srand(42); // Inicializa la semilla para los números aleatorios

    std::vector<std::vector<int>> matrixA(size, std::vector<int>(size));
    std::vector<std::vector<int>> matrixB(size, std::vector<int>(size));
    std::vector<std::vector<int>> result(size, std::vector<int>(size));

    generateRandomMatrix(matrixA, size);
    generateRandomMatrix(matrixB, size);

    // std::cout << "Matrix A:" << std::endl;
    // printMatrix(matrixA, size);
    // std::cout << "Matrix B:" << std::endl;
    // printMatrix(matrixB, size);

    multiplyMatrices(matrixA, matrixB, result, size);

    // std::cout << "Result:" << std::endl;
    // printMatrix(result, size);

    return 0;
}
