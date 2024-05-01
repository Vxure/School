# CMPT 365 - Programming Assignment 2 Queston 1
# Regan Li - 301426946
def ycocg_to_rgb(y, co, cg):
    r = y + co - cg
    g = y + cg
    b = y - co - cg
    return r, g, b

def rgb_to_yuv(r, g, b):
    y = round(0.299 * r + 0.587 * g + 0.114 * b)
    u = round(-0.299 * r - 0.587 * g + 0.886 * b)
    v = round(0.701 * r - 0.587 * g - 0.114 * b)
    return y, u, v

def main():
    filename = input("Enter path of input text file: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                values = line.strip().split(',')
                y, co, cg = map(int, values)        # Maps split values to Y Co Cg
                r, g, b = ycocg_to_rgb(y, co, cg)
                yuv = rgb_to_yuv(r, g, b)
                print("\nYUV:", yuv, "\n")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()