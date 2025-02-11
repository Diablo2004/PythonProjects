x, y = 5, 3  # Binary: x = 101, y = 011

print("Bitwise AND:", x & y)  # 001 -> 1
print("Bitwise OR:", x | y)   # 111 -> 7
print("Bitwise XOR:", x ^ y)  # 110 -> 6
print("Bitwise NOT:", ~x)     # -(x+1) -> -6
print("Left Shift:", x << 1)  # 1010 -> 10
print("Right Shift:", x >> 1) # 10 -> 2
