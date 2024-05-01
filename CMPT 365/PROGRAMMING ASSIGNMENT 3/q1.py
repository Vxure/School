# Question 1

def read_file_content(filePath):
    with open(filePath, 'r') as file:
        content = file.read().strip()


    return content

def arithmetic_coding_without_e1e2(symbols):

    # Probability model based on frequency
    total_symbols = len(symbols)
    prob_a = symbols.count('A') / total_symbols
    prob_b = symbols.count('B') / total_symbols
    
    # Initial range
    low, high = 0.0, 1.0
    
    # Encoding each symbol
    for symbol in symbols:
        range_ = high - low

        if symbol == 'A':
            high = low + range_ * prob_a

        else:  # symbol == 'B'
            low = low + range_ * prob_a
    
    return low, high

# Section 2
def arithmetic_coding_with_e1e2(symbols):

    # Probability model based on frequency
    total_symbols = len(symbols)
    prob_a = symbols.count('A') / total_symbols
    prob_b = symbols.count('B') / total_symbols
    
    # Initial range & operation
    low, high = 0.0, 1.0
    operations = []
    
    # Encoding each symbol
    for symbol in symbols:
        range_ = high - low
        if symbol == 'A':
            high = low + range_ * prob_a
        else:  # symbol == 'B'
            low = low + range_ * prob_a   

        # Check for E1/E2 conditions and apply operations
        while True:
            if high < 0.5:  # E1 condition
                # Scale up (double) the interval without changing its relative position
                low *= 2
                high *= 2
                operations += ['E1']
            elif low >= 0.5:  # E2 condition
                # Scale up (double) the interval after shifting it to the left
                low = 2 * (low - 0.5)
                high = 2 * (high - 0.5)
                operations += ['E2']

            else:
                break  
            
    return operations


# Results.
# Define an array of file paths
file_paths = ["PA3_sample_inputs/q1_(1)_(2)_input_0.txt", 
              "PA3_sample_inputs/q1_(1)_(2)_input_1.txt",
              "PA3_sample_inputs/q1_(1)_(2)_input_2.txt",
              "PA3_sample_inputs/q1_(1)_(2)_input_3.txt"
              ]

# Initialize lists to store the results
e1e2_operations_list = []

# Loop through each file path
for file_path in file_paths:

    # Read the content of the file
    content = read_file_content(file_path)
    
    # Calculate bounds without E1/E2
    lower_bound, upper_bound = arithmetic_coding_without_e1e2(content)

    # Calculate E1/E2 operations
    e1e2_operations = arithmetic_coding_with_e1e2(content)
    e1e2_operations_list.append((content, lower_bound, upper_bound, e1e2_operations))

# Print Results.
for idx, (file_content, lower_bound, upper_bound, operations) in enumerate(e1e2_operations_list, 1):
    print(f"\nString: '{file_content}'")
    print(f"Lower Bound (without E1/E2): {lower_bound} \nUpper Bound (without E1/E2): {upper_bound}")
    print(f"Interval (without E1/E2): [{lower_bound}, {upper_bound})")
    print(f"E1/E2 Operations: {operations}\n")