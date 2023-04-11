import math

# ABC is a right triangle, 90o at B. Therefore, angle ABC = 90o. Point M is the midpoint of hypotenuse AC.

# You are given the lengths AB and BC.
# Your task is to find angle MBC in degrees.

# Input Format
# The first line contains the length of side AB.
# The second line contains the length of side BC.
#
# Constraints
# 0 < AB <= 100
# 0 < BC <= 100
# Lengths AB and BC are natural numbers.
# Output Format
# Output angle MBC in degrees.

# Note: Round the angle to the nearest integer.
# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.


AB = int(input("Enter the length of AB between 0 and <=100 ", ))
BC = int(input("Enter the length of BC between 0 and <=100 ", ))


def calculate_hypotenuse_AC(side_1, side_2):
    side_CA = math.hypot(side_1, side_2)
    return side_CA


def calc_midpoint_of_hypotenuse():
    side_CA = calculate_hypotenuse_AC(AB, BC)
    Midpoint = side_CA / 2
    return Midpoint


CA = calculate_hypotenuse_AC(AB, BC)
print(f'Hypotenuse side is = {CA}')
MC = calc_midpoint_of_hypotenuse()
print(f'midpoint of Hypotenuse side = {MC}')

BCA = math.asin(1 * AB / CA)
print(f'Angle C is {BCA}')

length_BM = math.sqrt((BC ** 2 + MC ** 2) - (2 * BC * MC * math.cos(BCA)))
print(f'Length of MB is {length_BM}')

angle_MBC = math.asin(math.sin(BCA) * MC / length_BM)
print(f'So the Angle is {round(math.degrees(angle_MBC))}\u00B0') # This one is \u00B0 is to print the degree symbol
