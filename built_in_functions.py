from handson import groceryItem
x = groceryItem("Almonds",800,750,4.9,12)
#x.get_item_details()

# map function
def mul(n):
    return n**2
x = [1,2,3,4,5]
y = map(mul,x)
print(list(y))

# filter function
def is_positive(num):
    return num>0
a = [1,-2,-9,5]
pos_num = filter(is_positive,a)
print(list(pos_num))

st = ["apple","beetroot","carrot"]
st = list(map(str.upper,st))
print(st)

# reduce function
from functools import reduce
def sum_of_num(n1,n2):
    return n1+n2
seq = [1,2,3,4]
red = reduce(sum_of_num,seq)
print(red)