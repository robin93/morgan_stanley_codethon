# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

list_of_lists = []

for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    list_of_lists.append(new_list)
    
number_of_inputs = list_of_lists[0][0]

for iteration in range(number_of_inputs):
    case = iteration*2
    number_of_stocks = list_of_lists[case+1][0]
    stock_prices = list_of_lists[case+2]
    s = 0
    if number_of_stocks%2==0:
        pivot = (number_of_stocks/2)
    else:
        pivot = ((number_of_stocks-1)/2)
    for i in range(pivot):
        s = s + abs(stock_prices[i]-stock_prices[number_of_stocks-i-1])
    print s