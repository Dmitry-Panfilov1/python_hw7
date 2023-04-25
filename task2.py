def print_operation_table(operation, num_rows, num_coloums):
    for i in range(1, num_rows + 1):
        row = list()
        for j in range(1, num_coloums + 1):
            row.append(operation(i, j))
        print(*row)
    
print_operation_table(lambda x, y: x * y, 6, 6) 