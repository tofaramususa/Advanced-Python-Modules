from array2D import slice_me


# def main():
# 	family = [[1.80, 78.4],
# 				[2.15, 102.7],
# 				[2.10, 98.5], 
# 				[1.88, 75.2]]

# 	print(slice_me(family, 0, 2))
# 	print(slice_me(family, 1, -2))



# if __name__ == "__main__":
# 	main()

from array2D import slice_me

def run_tests():
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    
    # Test case 1: Valid slice
    print("Test Case 1: Valid slice")
    print(slice_me(family, 0, 2))  # [[1.8, 78.4], [2.15, 102.7]]
    print()

    # Test case 2: Valid slice with negative end index
    print("Test Case 2: Valid slice with negative end index")
    print(slice_me(family, 1, -2))  # [[2.15, 102.7]]
    print()

    # Test case 3: Empty slice
    print("Test Case 3: Empty slice")
    try:
        print(slice_me(family, 3, 3))  # []
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Test case 4: Non-2D list input
    print("Test Case 4: Non-2D list input")
    try:
        print(slice_me("not a list", 0, 2))
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Test case 5: Rows with inconsistent lengths
    print("Test Case 5: Rows with inconsistent lengths")
    invalid_family = [[1.80, 78.4], [2.15], [2.10, 98.5]]
    try:
        print(slice_me(invalid_family, 0, 2))
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Test case 6: Start and end indices out of range
    print("Test Case 6: Start and end indices out of range")
    try:
        print(slice_me(family, -10, 10))
    except ValueError as e:
        print(f"Error: {e}")
    print()

if __name__ == "__main__":
    run_tests()

