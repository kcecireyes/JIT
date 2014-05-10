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

    def getRecordType(self, i):
        record_type = self.table[i]['type']
        return record_type

    def getRecordExpType(self, i):
        record_exp_type = self.table[i]['exp_type']
        return record_exp_type

    def copyRecords(self, to_ST):
        for i in range(0,len(self.table)):
            to_ST.addRecord(self.table[i])
            # TODO: error handling (what if the table to copy from has no records, etc)   
        print "old \n" + str(self.table)
        print "new\n" + str(to_ST.table)
        return 1 # all records copied

