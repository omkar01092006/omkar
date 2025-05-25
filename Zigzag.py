print("Name:Omkar")
print("USN:1AY24AI079")
print("Section:O")
def print_zigzag(rows, columns):
    
    for i in range(rows):
        for j in range(columns):
            
            if (i + j) % 2 == 0:
                print('*', end='')
            else:
                print(' ', end='')
        print() 

def main():
    print("Zigzag Pattern Generator")
    
   
    try:
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))
        
       
        print_zigzag(rows, columns)
    
    except ValueError:
        print("Please enter valid integer values for rows and columns.")


main()
