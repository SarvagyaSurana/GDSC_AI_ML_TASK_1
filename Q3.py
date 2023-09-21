def input_matrix(n):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Invalid input. Please enter exactly n elements in each row.")
            return None
        matrix.append(row)
    return matrix

def matrix_multiply(matrix1, matrix2):
    n = len(matrix1)
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def trace_of_matrix(matrix):
    n = len(matrix)
    trace = sum(matrix[i][i] for i in range(n))
    return trace

def main():
    try:
        n = int(input())
        
        matrix1 = input_matrix(n)
        matrix2 = input_matrix(n)
        
        if matrix1 is None or matrix2 is None:
            return
        
        result_matrix = matrix_multiply(matrix1, matrix2)
        
        trace = trace_of_matrix(result_matrix)
        print(trace)
    
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
