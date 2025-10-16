import numpy as np


def categorize_people(ages):
    categories = np.where(ages >= 18, "Major", "Minor")
    return categories

ages = np.array([10, 15, 18, 20, 25, 30])
print(categorize_people(ages))