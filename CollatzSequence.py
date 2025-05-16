def collatz_sequence(n):
   
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:  # If n is even
            n = n // 2
        else:  # If n is odd
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence

def main():
    print("Welcome to the Collatz Sequence Generator!")
    
    try:
        
        number = int(input("Enter a positive integer: "))
        
        if number <= 0:
            print("Please enter a positive integer.")
        else:
            
            sequence = collatz_sequence(number)
            print("The Collatz sequence for", number, "is:")
            print(sequence)
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


main()
