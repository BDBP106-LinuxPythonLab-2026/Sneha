import time


# Custom decorator to measure execution time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        print(f"Execution time: {end_time - start_time:.6f} seconds")

        return result

    return wrapper


class LinearAlgebra:

    def __init__(self, A, B):
        self._A = A
        self._B = B

    # Property getter for matrix A
    @property
    def A(self):
        return self._A

    # Property setter for matrix A
    @A.setter
    def A(self, new_A):
        self._A = new_A

    # Property getter for matrix B
    @property
    def B(self):
        return self._B

    # Property setter for matrix B
    @B.setter
    def B(self, new_B):
        self._B = new_B

    # Instance method for matrix multiplication
    @calculate_time
    def multiply(self):

        # Check for empty matrices
        if not self._A or not self._B:
            raise ValueError("Matrices cannot be empty.")

        # Check for consistent row lengths
        if any(len(row) != len(self._A[0]) for row in self._A):
            raise ValueError("Matrix A has inconsistent row lengths.")

        if any(len(row) != len(self._B[0]) for row in self._B):
            raise ValueError("Matrix B has inconsistent row lengths.")

        # Get dimensions
        rows_A = len(self._A)
        cols_A = len(self._A[0])

        rows_B = len(self._B)
        cols_B = len(self._B[0])

        # Check multiplication condition
        if cols_A != rows_B:
            raise ValueError(
                "Matrix multiplication is not possible: "
                "columns of A must equal rows of B."
            )

        # Initialize result matrix
        result = [
            [0 for _ in range(cols_B)]
            for _ in range(rows_A)
        ]

        # Perform multiplication
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += (
                        self._A[i][k] * self._B[k][j]
                    )

        return result


# Function to accept a matrix from the user
def input_matrix(name):

    rows = int(input(f"Enter the number of rows in {name}: "))
    cols = int(input(f"Enter the number of columns in {name}: "))

    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be positive.")

    matrix = []

    print(f"Enter the elements of matrix {name}, row by row:")

    for i in range(rows):
        while True:
            values = input(
                f"Enter {cols} elements for row {i + 1}: "
            ).split()

            if len(values) != cols:
                print(f"Please enter exactly {cols} values.")
                continue

            try:
                row = [float(value) for value in values]
                matrix.append(row)
                break
            except ValueError:
                print("Please enter valid numeric values.")

    return matrix


# Main program
try:
    A = input_matrix("A")
    B = input_matrix("B")

    algebra = LinearAlgebra(A, B)

    print("\nMatrix A:")
    for row in algebra.A:
        print(row)

    print("\nMatrix B:")
    for row in algebra.B:
        print(row)

    result = algebra.multiply()

    print("\nProduct of A and B:")
    for row in result:
        print(row)

except ValueError as error:
    print("Error:", error)
