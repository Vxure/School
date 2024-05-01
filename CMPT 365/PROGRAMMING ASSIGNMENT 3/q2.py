# Question 2

import numpy as np
import math

def read_N_from_file(file_path):
    with open(file_path, 'r') as file:
        N = int(file.readline().strip())
    return N

# Given colab
def a(i, N):
    if i == 0:
        return math.sqrt(1/N)
    else:
        return math.sqrt(2/N)

def get_DCT_matrix(N):
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            matrix[i, j] = a(i, N) * math.cos(((2*j+1)*i*math.pi)/(2*N))
    return matrix

def read_vector_from_file(file_path):
    with open(file_path, 'r') as file:
        line = file.readline().strip()
        vector_elements = line[ 1:-1 ].split(',')
        vector = np.array([float(element.strip()) for element in vector_elements])
    return vector

# Print Results.
# Define file paths
size_file_paths = ["PA3_sample_inputs/q2_(1)_input_0.txt",
                    "PA3_sample_inputs/q2_(1)_input_1.txt",
                    "PA3_sample_inputs/q2_(1)_input_2.txt"
                    ]
vector_file_paths = ["PA3_sample_inputs/q2_(2)_input_0.txt",
                     "PA3_sample_inputs/q2_(2)_input_1.txt",
                     "PA3_sample_inputs/q2_(2)_input_2.txt"
                    ]

# Print transformation matrices with filenames
print("\n----------Question 1 - Transformation Matrices----------")
for size_file_path in size_file_paths:
    filename = size_file_path
    N = read_N_from_file(size_file_path)
    print(f"\n{filename}: Size = {N}")
    print(f"\nTransformation Matrix: \n{get_DCT_matrix(N)}")

# Compute and print DCT transformations
print("\n----------Question 2 - DCT Transformations----------\n")
for size_file_path, vector_file_path in zip(size_file_paths, vector_file_paths):
    filename = vector_file_path
    N = read_N_from_file(size_file_path)

    # Read vector from file
    x = read_vector_from_file(vector_file_path)
    N = len(x)

    # Compute DCT transformation
    dct_matrix = get_DCT_matrix(N)
    transformed = dct_matrix @ x.T
    print(f"{filename} \nOriginal Vector = {x}\n")
    print(f"Transformed Vector:\n{np.round(transformed, 8)}\n")

# Question 3
# Create a high frequency vector
print("----------Question 3 - Designing Input Vector----------")
highfreq_vector = read_vector_from_file("PA3_sample_inputs/q3.txt")
formatted_vector = ' '.join(map(str, highfreq_vector))
print(f"High frequency Vector: [ {formatted_vector} ]\n")

# Calculate Discrete Cosine Transform
highfreq_N = len(highfreq_vector)
highfreq_dctMatrix = get_DCT_matrix(highfreq_N)
highfreq_transformed = highfreq_dctMatrix @ highfreq_vector.T
print(f"Transformed Vector:\n{np.round(highfreq_transformed, 5)}\n")

