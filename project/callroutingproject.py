import sys
sys.path.append('../source')
from hashtable import HashTable
class CallRouting(object):
    def __init__(self,number,route):
        '''takes in a phone number and spits out the cost to run it'''
        #route costs from file to be read
        filename= route
        #declar empty hast table to store values
        cost_hash_table =HashTable()
        with open(filename) as file_object:
            #for everyline in the file
            for line in file_object:
                #strip it of whitespace
                line =line.strip()
                #split it into a string of two
                line=line.split(',')
                #set the ket to the firs in the list and the value to the second( turned into a float)
                cost_hash_table.set(line[0],float(line[1]))

        self.route_costs = cost_hash_table
        #telephone numbers from file to be read
        filename = number
        phone_numbers =[]
        with open(filename) as file_object:
            for line in file_object:
                line =line.strip()
                phone_numbers.append(line)

        self.telenum = phone_numbers

    def cost_to_route(self):
        'Based on the numbert thats passed in it loops through the dictionaries keys and maatches t the values, which is the cost'
        for prefix,cost in self.route_costs.items():
            if self.telenum==prefix:
                return(str(self.telenum) +','+ str(cost))
            else:
                return("Not found")
if __name__ == '__main__':
    # call = CallRouting('+86153')
    # print(call.cost_to_route())
    
