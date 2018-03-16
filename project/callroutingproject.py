class CallRouting(object):
    def __init__(self,telenum):
        '''takes in a phone number and spits out the cost to run it'''
        # the dictionary of comparisions for the first scenario
        self.route_costs = {'+86153':0.84, '+449275049':0.49, '+8130':0.68,'+4928843955':0.40 ,'+449187847':0.48,'8197753':0.75, '+449916707':0.58, '+64655676':0.40,'+34924199':0.39,'+1941613':0.05}
        #telephin number to be checked
        self.telenum = telenum

    def cost_to_route(self):
        'Based on the numbert thats passed in it loops through the dictionaries keys and maatches t the values, which is the cost'
        for prefix,cost in enumerate(self.route_costs):
            if str(self.telenums)==prefix
            print(self.telenums+','+ cost)
