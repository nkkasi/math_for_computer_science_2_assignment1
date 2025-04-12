'''
# Question2
A 6-sided die is rolled n times. What is the probability all faces have appeared?
(Hint: Use Principle of Inclusion and Exclusion)
'''
from math import comb

def prob_all_faces_appear(n, sides=6):
    # Using inclusion-exclusion principle
    total_prob = 0
    for k in range(sides + 1):
        term = (-1)**k * comb(sides, k) * ((1 - k / sides) ** n)
        total_prob += term
    return total_prob

# Example: Compute for n = 10 rolls
probability_n10 = prob_all_faces_appear(n=10)
print(probability_n10)


