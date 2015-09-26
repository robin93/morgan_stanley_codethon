list_of_lists = [[2],[4],[2,4,3,2],[4],[2,4,4,8]]#,[7],[2,4,6,8,10,12,14]]
#list_of_lists = [[3],[4],[2,4,3,2],[4],[2,4,3,8],[7],[2,4,6,8,10,12,14]]

number_of_inputs = list_of_lists[0][0]

def cases_gen(stock_prices,index):
    if index==(number_of_stocks-1):
        s1=0
        for i in range(pivot):
                        s1 = s1 + abs(stock_prices[i]-stock_prices[number_of_stocks-i-1])
        list_of_sums.append(s1)
        print list_of_sums
    else:
        for i in range(index,number_of_stocks-1):
            if stock_prices[i-1]%2==0 and stock_prices[i+1]%2==0:
                copy = stock_prices
                copy[i] = 0.5*(copy[i+1] + copy[i-1])
                print copy
                cases_gen(copy,i+1)
                #stock_prices[i] = 0.5*(stock_prices[i+1] + stock_prices[i-1])
                # print stock_prices
                cases_gen(stock_prices,i+1)

#print number_of_inputs
for iteration in range(number_of_inputs):
    case = iteration*2
    number_of_stocks = list_of_lists[case+1][0]
    stock_prices = list_of_lists[case+2]
    if number_of_stocks%2==0:
        pivot = (number_of_stocks/2)
    else:
        pivot = ((number_of_stocks-1)/2)
    s1=0
    for i in range(pivot):
                    s1 = s1 + abs(stock_prices[i]-stock_prices[number_of_stocks-i-1])
    list_of_sums=[s1]
    cases_gen(stock_prices,1)
    print int(max(list_of_sums))
    print len(list_of_sums)


# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

list_of_lists = []

for line in sys.stdin:
    new_list = [elem for elem in line.split()]
    list_of_lists.append(new_list)

number_of_inputs = int(list_of_lists[0][0])

def dist_mat(string):
    vector = [0 for i in range(26)]
    for letter in string:
        if letter=='a':vector[0]+=1
        elif letter=='b':vector[1]+=1
        elif letter=='c':vector[2]+=1
        elif letter=='d':vector[3]+=1
        elif letter=='e':vector[4]+=1
        elif letter=='f':vector[5]+=1
        elif letter=='g':vector[6]+=1
        elif letter=='h':vector[7]+=1
        elif letter=='i':vector[8]+=1
        elif letter=='j':vector[9]+=1
        elif letter=='k':vector[10]+=1
        elif letter=='l':vector[11]+=1
        elif letter=='m':vector[12]+=1
        elif letter=='n':vector[13]+=1
        elif letter=='o':vector[14]+=1
        elif letter=='p':vector[15]+=1
        elif letter=='q':vector[16]+=1
        elif letter=='r':vector[17]+=1
        elif letter=='s':vector[18]+=1
        elif letter=='t':vector[19]+=1
        elif letter=='u':vector[20]+=1
        elif letter=='v':vector[21]+=1
        elif letter=='w':vector[22]+=1
        elif letter=='x':vector[23]+=1
        elif letter=='y':vector[24]+=1
        elif letter=='z':vector[25]+=1
    return vector

def vector_diff(vector1,vector2):
    return [(vector1[i]-vector2[i]) for i in range(len(vector1))]

def net_vector_element_sum(vector):
    sum = 0
    for i in vector:sum = sum + i
    return sum

def vector_positive_element_sum(vector):
    sum = 0
    for i in vector:
        if i>0:
            sum = sum + i
    return sum

for iterations in range(number_of_inputs):
    case = 3*iterations
    init_string = list_of_lists[case+1][0]
    obj_string = list_of_lists[case+2][0]
    cost_mat = [int(element) for element in (list_of_lists[case+3])]
    del_cost,ins_cost,rep_cost = cost_mat[0],cost_mat[1],cost_mat[2]
    init_vector = dist_mat(init_string)
    obj_vector = dist_mat(obj_string)
    diff_vector = vector_diff(init_vector,obj_vector)
    net_sum =net_vector_element_sum(diff_vector)
    pos_sum = vector_positive_element_sum(diff_vector)
    neg_sum = net_sum - pos_sum
    cost = 0
    if net_sum>0:
        cost = cost + net_sum*del_cost
        if (del_cost+ins_cost)>rep_cost:
            cost = cost + (pos_sum-net_sum)*rep_cost
        else:
            cost = cost + (pos_sum-net_sum)*(del_cost+ins_cost)
    elif net_sum==0:
        if (del_cost+ins_cost)>rep_cost:
            cost = cost + (pos_sum)*rep_cost
        else:
            cost = cost + (pos_sum)*(del_cost+ins_cost)
    else:
        cost = cost + abs(net_sum)*ins_cost
        if (del_cost+ins_cost)>rep_cost:
            cost = cost + (pos_sum)*rep_cost
        else:
            cost = cost + (pos_sum)*(del_cost+ins_cost)
    print cost 