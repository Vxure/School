# CMPT 365 - Programming Assignment 2 Queston 2
# Regan Li - 301426946

import numpy as np

def read_image(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        # Convert the image to a numpy array after reading
        return np.array([[int(pixel) for pixel in line.strip().split(',')] for line in lines])

def halftone_printing(image):
    dither_matrix = np.array([ [0, 3], [2, 1] ])
    length = len(image)
    # Ensure dithered is initialized as a numpy array
    dithered = np.zeros((length * 2, length * 2))
    
    for i in range(0, length * 2, 2):
        for j in range(0, length * 2, 2):
            pixel_value = image[i//2, j//2]
            # Apply dithering based on matrix & pixel value
            dithered[i, j] = int(dither_matrix[0,0] < pixel_value / 64) 
            dithered[i, j + 1] = int(dither_matrix[0,1] < pixel_value / 64)
            dithered[i + 1, j] = int(dither_matrix[1,0] < pixel_value / 64)
            dithered[i + 1, j + 1] = int(dither_matrix[1,1] < pixel_value / 64)

    dithered = dithered.astype(int)

    return dithered

def ordered_dithering(image, dither_matrix):
    result = []
    n = len(image)
    for i in range(n):
        result_row = []
        for j in range(n):
            threshold = dither_matrix[i % 2][j % 2] * 64    # Apply threshold to decide pixel value
            result_row.append(1 if image[i][j] >= threshold else 0)
        result.append(result_row)
    return result

def print_image(image):
    for row in image:
        print(''.join(map(str, row)))

def main():
    image_file = input("Enter path of input text file: ")
    dither_matrix = [ [0, 3], [2, 1] ]

    image = read_image(image_file)  # Returns numpy array

    print("\nOriginal Image:")
    print_image(image)

    print("\nHalftone Printing Result:")
    halftone_result = halftone_printing(image)
    print_image(halftone_result)

    # Convert the numpy array result back to a list for the ordered dithering function
    ordered_dither_result = ordered_dithering(image.tolist(), dither_matrix)
    print("\nOrdered Dithering Result:")
    print_image(ordered_dither_result)

if __name__ == "__main__":
    main()