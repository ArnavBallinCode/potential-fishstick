gfdef print_pyramid(height):
    for i in range(1, height + 1):
        print(' ' * (height - i) + '#' * i)

def main():
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                break
            else:
                print("Height must be between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 8.")

    print_pyramid(height)

if __name__ == "__main__":
    main()