# ECC BASIC IMPLEMENTATION (Toy Example)
# Prime field (all operations happen mod p)
p = 17
# Curve equation: y^2 = x^3 + ax + b
a = 2
b = 2
# FUNCTION: Modular Inverse
# Used because division is not directly possible in mod arithmetic
def mod_inverse(k, p):
    return pow(k, p - 2, p)  # Fermat's little theorem
# FUNCTION: POINT ADDITION
# Adds two points on elliptic curve
def point_add(P, Q):
    # If one point is None (identity), return the other
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    # If points are inverse → result is point at infinity
    if x1 == x2 and y1 != y2:
        return None
    # CASE 1: Point Doubling (P == Q)
    if P == Q:
        m = (3 * x1 * x1 + a) * mod_inverse(2 * y1, p)
    # CASE 2: Normal Addition (P != Q)
    else:
        m = (y2 - y1) * mod_inverse(x2 - x1, p)
    # Take slope mod p
    m = m % p
    # Compute new point coordinates
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)
# FUNCTION: POINT DOUBLING
# Special case of point addition (P + P)
def point_double(P):
    return point_add(P, P)
# FUNCTION: SCALAR MULTIPLICATION (kP)
# Repeated addition of a point k times
def scalar_mult(k, P):
    R = None  # start with identity point
    for _ in range(k):
        R = point_add(R, P)
    return R
# BASE POINT (Generator Point)
G = (5, 1)
print("Base Point G:", G)
# KEY GENERATION
# Private key = random number
# Public key = PrivateKey * G
private_key = 7
public_key = scalar_mult(private_key, G)
print("\nPrivate Key:", private_key)
print("Public Key:", public_key)
# ENCRYPTION (Simplified EC-ElGamal)
message = 9  # small numeric message to encrypt
k = 3  # random number used for encryption
# C1 = kG (first part of ciphertext)
C1 = scalar_mult(k, G)
# C2 = message + (k * PublicKey_x)
C2 = message + scalar_mult(k, public_key)[0]
print("\n ENCRYPTION")
print("Cipher C1:", C1)
print("Cipher C2:", C2)
# DECRYPTION
# Shared secret = PrivateKey * C1
shared_secret = scalar_mult(private_key, C1)[0]
# Recover original message
decrypted_message = C2 - shared_secret
print("\n DECRYPTION")
print("Decrypted Message:", decrypted_message)