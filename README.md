# Python Matrix Calculator
Command line program written to make tedious matrix operations almost instant. Begin by selecting an operation 1-8 (briefly outlined below), and then following instructions on screen.

In order to input a matrix, simply begin by specifying the number of rows and columns. The program will verify that dimension of the matrix is valid for the selected operation (i.e. only square matrices for inverse operation). Next, to input the actual rows of the array, input values in the format "X X X X X". For example, if you specified a 3x3 matrix, you will be prompted to input 3 rows in the form "1 2 3".

If an operation selected requires two matrices, you will then be prompted to input a second one, and calculation will begin.

## List of operations
### 1. Addition
### 2. Subtraction
### 3. Multiplication
### 4. Row Echelon Form
### 5. Reduced Row Echelon Form
### 6. Transpose
### 7. Inverse
### 8. Determinant

Hoping to add in the near future: column space, row space, rank, eigenvalues, eigenvectors, and diagonalization.

Also on the to-do list: add further comments to explain process, refactor code for inverse at it is essentially the same as RREF code.

This program was originally written to help with my linear algebra course last semester, and has been refactored and released to GitHub :)!