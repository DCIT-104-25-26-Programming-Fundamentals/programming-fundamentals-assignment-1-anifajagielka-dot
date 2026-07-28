def read_matrix(rows, cols, label=""):
    """Read a `rows` x `cols` matrix from the user, one row per line."""
    matrix = []
    for i in range(rows):
        prompt = f"Enter row {i + 1}{(' of ' + label) if label else ''}: "
        values = input(prompt).split()
        row = [int(v) for v in values]
        matrix.append(row)
    return matrix
 
 
def display_matrix(matrix):
    """Print `matrix` as a neatly aligned grid."""
    # Work out the widest value in each column so everything lines up.
    col_count = len(matrix[0])
    col_widths = []
    for c in range(col_count):
        widest = 0
        for r in range(len(matrix)):
            widest = max(widest, len(str(matrix[r][c])))
        col_widths.append(widest)
 
    for row in matrix:
        cells = []
        for c in range(len(row)):
            cells.append(str(row[c]).rjust(col_widths[c]))
        print("  ".join(cells))
 
 
def transpose(matrix):
    """Return the transpose of `matrix` (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
 
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
 
    return result
 
 
def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
 
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
 
    return result
 
 
def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product A x B."""
    m = len(matrix_a)          # rows of A
    n = len(matrix_a[0])       # cols of A == rows of B
    p = len(matrix_b[0])       # cols of B
 
    result = [[0 for _ in range(p)] for _ in range(m)]
 
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total
 
    return result
 
 
def run_transpose():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)
 
    print("\nOriginal Matrix:")
    display_matrix(matrix)
 
    print("\nTransposed Matrix:")
    display_matrix(transpose(matrix))
 
 
def run_addition():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
 
    print("Matrix A:")
    matrix_a = read_matrix(rows, cols, label="A")
    print("Matrix B:")
    matrix_b = read_matrix(rows, cols, label="B")
 
    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)
 
    print("\nSum (A + B):")
    display_matrix(add_matrices(matrix_a, matrix_b))
 
 
def run_multiplication():
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (must equal rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))
 
    print("Matrix A:")
    matrix_a = read_matrix(m, n, label="A")
    print("Matrix B:")
    matrix_b = read_matrix(n, p, label="B")
 
    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)
 
    print("\nProduct (A x B):")
    display_matrix(multiply_matrices(matrix_a, matrix_b))
 
 
def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
    choice = input("Choose an operation (1-3): ").strip()
 
    if choice == "1":
        run_transpose()
    elif choice == "2":
        run_addition()
    elif choice == "3":
        run_multiplication()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
 
 
if __name__ == "__main__":
    main()
 