def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    Returns:
        int GCD for valid inputs, or None if undefined (e.g., gcd(0, 0)).
    """
    if not isinstance(a, int):
        print("Error: Expected integer inputs. Input with inccorect type is (", a,").")
        return None
    
    if not isinstance(b, int):
        print("Error: Expected integer inputs. Input with inccorect type is (", b,").")
        return None

    if a == 0 and b == 0:
        print("Error: gcd(0, 0) behavior undefined.")
        return None
    
    a = abs(a)
    b = abs(b)

    if a == 0:
        return b
    
    return gcd(b%a, a)


print("Test cases for gcd function:")
# Test cases from Prof.:
print(gcd(54, 24))  # 6
print(gcd(48, 18))  # 6
print(gcd(101, 10))  # 1

# Own test cases:
print(gcd(10, 15)) # 5

# Prime #s
print(gcd(7, 11)) # 1  TWO DIFF PRIME #s
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

# Zero divide, 
print(gcd(0, 5)) # 5
print(gcd(0, 10)) # 10
print(gcd(0, 0)) # Return Error message + None

# Large #s
print(gcd(123456, 789012)) # 12
print(gcd(1000000, 500000)) # 500000

print(gcd("5", 10)) # 500000