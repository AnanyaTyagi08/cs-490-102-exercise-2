def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if (a == 0):
        return b

    return abs(gcd(b%a, a))


def gcd2(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    Returns None if a or b is zero or negative.
    """
    # Reject zero or negative inputs
    if a <= 0 or b <= 0:
        return None

    if (a == 0):
        return b

    return abs(gcd(b%a, a))


print("Test cases for regular gcd function:")
# Test cases from Prof.:
print(gcd(54, 24))  # 6
print(gcd(48, 18))  # 6
print(gcd(101, 10))  # 1

# Own test cases:
print(gcd(10, 15)) # 5

# Prime #s
print(gcd(7, 11)) # 1  TWO DIFF PRIME #s
print(gcd(51, 11)) # 1  TWO DIFF PRIME #s
print(gcd(17, 13)) # 1   # coprime numbers
print(gcd(11, 11)) # 11  SAME PRIME #s 
print(gcd(7, 20)) # 1  ONE PRIME ONE REG

# Negative #s GCDS should always be non-negative
print(gcd(-10, 15)) # 5  one -(ve)
print(gcd(10, -15)) # 5  one -(ve)
print(gcd(-10, -15)) # 5  two -(ve)

# One # devides the other
print(gcd(8, 4)) # 4
print(gcd(100, 25)) # 25
print(gcd(9, 3)) # 3

# Zero divide
print(gcd(0, 5)) # 5
print(gcd(0, 10)) # 10
print(gcd(0, 0)) 

# Large #s
print(gcd(123456, 789012)) # 12
print(gcd(1000000, 500000)) # 500000




print("\n\nTest cases for Reject Zero & -(ve)s gcd function:")
# Test cases from Prof.:
print(gcd2(54, 24))  # 6
print(gcd2(48, 18))  # 6
print(gcd2(101, 10))  # 1

# Own test cases:
print(gcd2(10, 15)) # 5

# Prime #s
print(gcd2(7, 11)) # 1  TWO DIFF PRIME #s
print(gcd2(51, 11)) # 1  TWO DIFF PRIME #s
print(gcd2(17, 13)) # 1   # coprime numbers
print(gcd2(11, 11)) # 11  SAME PRIME #s 
print(gcd2(7, 20)) # 1  ONE PRIME ONE REG

# Negative #s, shd return None bcs Prof. specified we don't divide by -(ve)s
print(gcd2(-10, 15)) # None
print(gcd2(10, -15)) # None
print(gcd2(-10, -15)) # None

# One # devides the other
print(gcd2(8, 4)) # 4
print(gcd2(100, 25)) # 25
print(gcd2(9, 3)) # 3

# Zero divide, shd return None bcs Prof. specified we don't divide by 0s
print(gcd2(0, 5)) # None 
print(gcd2(0, 10)) # None
print(gcd2(0, 0)) # None

# Large #s
print(gcd2(123456, 789012)) # 12
print(gcd2(1000000, 500000)) # 500000