'''
concept  of numbers bases as lists

will need alans help on this for debugging since i cant get the binary to display like i did the number systems
'''
base10Nums= [1,2,3,4,5,6,7,8,9]
tickOverAmount_base10= len(base10Nums)
print(tickOverAmount_base10)

base2Nums=[1,0]
tickOverAmount_base2= len(base2Nums)

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

base2Nums_next = [num for num in map((lambda x: x + tickOverAmount_base2),base2Nums)]

print(base2Nums_next)
