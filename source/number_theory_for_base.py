'''
concept  of numbers bases as lists
'''
base10Nums= [1,2,3,4,5,6,7,8,9]
tickOverAmount_base10= len(base10Nums)
print(tickOverAmount_base10)

base2Nums=[0,1]
tickOverAmount_base2= len(base2Nums)-1

hex_nums =[1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
tickOverAmount_hex = len(hex_nums)
'''
figure out the next row in each

'''
'''
test function with labdas

for ch in map((lambda x: x + tickOverAmount_base10),base10Nums):
    print(ch)

'''
base10Nums_next=[num for num in map((lambda x: x + tickOverAmount_base10),base10Nums)]

print(base10Nums_next)
#####

base2Nums_next = [num for num in map((lambda x: (x + tickOverAmount_base2)%2),base2Nums)]

print(base2Nums_next)

base2Nums_next2 = [num for num in map((lambda x: (x + tickOverAmount_base2)%2),base2Nums_next)]

print(base2Nums_next2)
