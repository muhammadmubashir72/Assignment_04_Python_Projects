# ## Problem Statement 16

# # Write a program that doubles each element in a list of numbers. 
# # For example, if you start with this list:

# # numbers = [1, 2, 3, 4]
# # You should end with this list:
# # numbers = [2, 4, 6, 8]

# def main():
#     numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers

#     for i in range(len(numbers)):  # Loop through the indices of the list
#         elem_at_index = numbers[i]  # Get the element at index i in the numbers list
#         numbers[i] = elem_at_index * 2  # Set the element at index i to be equal to the previous element times 2
#     print(numbers)  # This should print the doubled list

# if __name__ == '__main__':
#     main()
def main():
    numbers = list(map(int, input("➡️ Enter numbers: ").split()))

    for i in range(len(numbers)):  
        numbers[i] *= 2 

    print(f"\n✅ Your doubled numbers are: {numbers} 🎉")

if __name__ == '__main__':
    main()
