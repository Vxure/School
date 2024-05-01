# CMPT 365 - Programming Assignment 2 Queston 3
# Regan Li - 301426946

import math
from collections import Counter
import heapq

# Reading input from a file
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        string = file.readline().strip()
    return string

# Calculating entropy
def calculate_entropy(string, order = 1):
    length = len(string)
    if order == 1:
        frequencies = Counter(string)
    else: # for second order, consider pairs
        pairs = [string[i:i + 2] for i in range(0, length, 2)]
        frequencies = Counter(pairs)
    
    entropy = -sum((freq/length) * math.log2(freq/length) for freq in frequencies.values())
    if order == 2:
        entropy /= 2  # Adjusting for per symbol entropy in pairs
    return entropy

# Huffman coding function
def huffman_coding(frequencies):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key = lambda p: (len(p[-1]), p))

# Calculating average codeword length
def calculate_average_codeword_length(frequencies, order=1):
    coded = huffman_coding(frequencies)
    total_length = sum(len(code) * frequency for _, [symbol, code] in enumerate(coded) for frequency in [frequencies[symbol]])
    total_symbols = sum(frequencies.values())
    average_length = total_length / total_symbols
    if order == 2:
        average_length /= 2  # Adjusting for per-symbol in the case of 2-symbol coding
    return average_length

# Main execution
def main():
    file_path = input("Please enter the file path: ")  # User inputs file path
    string = read_input_file(file_path)
    
    # Entropy calculations
    print(f"\nFirst order entropy: {calculate_entropy(string, 1)} bits/symbol")
    print(f"Second order entropy: {calculate_entropy(string, 2)} bits/symbol\n")
    
    # Huffman coding
    frequencies_1 = Counter(string)
    frequencies_2 = Counter([string[i:i + 2] for i in range(0, len(string), 2)])
    
    print(f"Average codeword length (Huffman Coding): {calculate_average_codeword_length(frequencies_1, 1)} per Symbol")
    print(f"Average codeword length (2-Symbol Joint Huffman Coding): {calculate_average_codeword_length(frequencies_2, 2)} per Symbol\n")

if __name__ == "__main__":
    main()
