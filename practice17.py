# Multiplication table with conditions
for i in range(1, 6):  # Outer loop for rows
    for j in range(1, 6):  # Inner loop for columns
        if i * j > 15:
            break  # Exit inner loop if product > 15
        if j == 2:
            continue  # Skip the rest of this iteration for j == 2
        print(f"{i} x {j} = {i * j}")
