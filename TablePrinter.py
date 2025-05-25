def printTable(table):

    colWidths = [0] * len(table)
    
    for i in range(len(table)):
        colWidths[i] = max(len(item) for item in table[i])


    for row in range(len(table[0])):
        for col in range(len(table)):
            print(table[col][row].rjust(colWidths[col]), end=' ')
        print()  # Newline after each row


tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

printTable(tableData)
