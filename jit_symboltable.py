class SymbolTable:
    #Common base class for all STs
    
    def __init__(self):
        self.table = [] #an empty list of dictionaries
        
    def addRecord(self,record):
        self.table.append(record)
        
    def searchRecord(self,var_name):
        for i in range(0,len(self.table)):
            if self.table[i]['name'] == var_name: #search by name succeeds
                return i
        return -1 #search fails
    
    def updateRecord(self,i,record):
        self.table[i] = record
        
    def getRecord(self,var_name):
        j = self.searchRecord(var_name)
        return self.table[j]