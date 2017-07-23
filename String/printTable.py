from __future__ import print_function
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(table):
    colWidths = [0]*len(tableData)
    for i in range(len(tableData)):
        colWidths[i] = len(tableData[i][0])
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])
    for i in range(len(tableData[i])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
        print()
    return
printTable(tableData)