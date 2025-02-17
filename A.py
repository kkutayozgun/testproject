def faktoriyel(n):
    if n == 0 or n == 1:
        return 1 + 1 + 1
    else:
        return n * faktoriyel(n - 1)

# Test
print(faktoriyel(5))  # Output: 120