import sys
sys.path.append('../source')
from hashtable import HashTable

'''
Special note for scenario 1: Scenario 1 is In my commit history sicnce i did not think to dave it, but was implmented as a dictionary for the route costs
this current version weill hadnle scenario 2
'''
class CallRouting2nd(object):
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
        #same algorithm as last tome
        filename = number
        phone_numbers =[]
        with open(filename) as file_object:
            for line in file_object:
                line =line.strip()
                phone_numbers.append(line)

        self.telenum = phone_numbers

    def cost_to_route(self):
        'Based on the numbert thats passed in it loops through the dictionaries keys and maatches t the values, which is the cost'
        num_list =[]
        for num in self.telenum:
            if self.route_costs.get(num) == None:
                num_list.append(None)
            else:
                num_list.append(self.route_costs.get(num))
        return num_list
class CallRouting3rd(object):
    def __init__(self,number,route_list):
        '''Takes a list of txt files inerates through them and then puts them into a hashtable, Not going to lie, this is an EXPENSIVE operation (n^2) but its a nessecary eveil unlesss i wanted to sort them'''
        cost_hash_table =HashTable()
        for txt_file in route_list:
            with open(txt_file) as file_object:
                #for everyline in the file
                for line in file_object:
                    #strip it of whitespace
                    line =line.strip()
                    #split it into a string of two
                    line=line.split(',')
                    #set the ket to the firs in the list and the value to the second( turned into a float)
                    cost_hash_table.set(line[0],float(line[1]))

        self.route_costs = cost_hash_table
        #Now work with the numbers
        filename = number
        phone_numbers =[]
        with open(filename) as file_object:
            for line in file_object:
                line =line.strip()
                phone_numbers.append(line)

        self.telenum = phone_numbers

    def cost_to_route(self):
        'Based on the numbert thats passed in it loops through the dictionaries keys and maatches t the values, which is the cost'
        num_list =[]
        for num in self.telenum:
            if self.route_costs.get(num) == None:
                num_list.append(None)
            else:
                num_list.append(self.route_costs.get(num))
        return num_list

if __name__ == '__main__':
     call = CallRouting2nd('data/phone-numbers-3.txt','data/route-costs-10.txt')
     print(call.cost_to_route())
