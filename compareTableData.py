import csv

class ModifiedDict:
    modified_dict = {}
    pk = "";
    def __init__(self,pk):
        self.pk = pk
    
    def add_to_dict(self,pk,modified_list):
        self.modified_dict.update({pk : modified_list})
    
    def get_modified_list(self,pk):
        if(self.modified_dict.get(pk) is None) : 
            return []
        else :
            return self.modified_dict.get(pk)

class compareTableData(object) :
    
    def is_same_columns_exist(self, keys1 , keys2, t):
        #{"pk" : {ModifiedCol : colName, oldValue : old value, newValue : new value}}
            for x in keys1:
                if(x in keys2):
                   
                    if(keys1.get(x) != keys2.get(x)) : 
                        y = t.get_modified_list(keys2.get(t.pk))
                        y.append({"ModifiedCol" : x , "oldValue" : keys1.get(x) , "newValue" : keys2.get(x)})
                        t.add_to_dict(keys2.get(t.pk)+ "--> Modified " ,y)
                        
    def __init__(self):
        pk = "account_number"
        t =  ModifiedDict(pk)
        newItemDict = {}
        oldItemDict = {}
        with open('sample-address-new.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                newItemDict[row['account_number']] = row
        
        
        with open('sample-address-old.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                oldItemDict[row['account_number']] = row
        
        if(len(oldItemDict) != len(newItemDict)) :
            oldItemBakupDict = oldItemDict.copy()
            newItemBakupDict = newItemDict.copy()
            
            for x in newItemDict.keys():
                if x in oldItemDict:
                    oldItemBakupDict.pop(x)
            
            if(len(oldItemBakupDict)> 0) :
                for x in oldItemBakupDict:
                    itemKey = x +"--> DELETED"
                    t.add_to_dict(itemKey ,oldItemBakupDict[x])
            
            
            for x in oldItemDict.keys():
                if x in newItemDict:
                    newItemBakupDict.pop(x)
                  
            if(len(newItemBakupDict)> 0) :
                for x in newItemBakupDict:
                    itemKey = x + "--> New "
                    t.add_to_dict(itemKey,newItemBakupDict[x])
              
            for x in newItemBakupDict.keys():
                if x in newItemDict:
                    newItemDict.pop(x)
            for x in oldItemBakupDict.keys():
                if x in oldItemDict:
                    oldItemDict.pop(x)
                
                
        print("After removing deleted and new records. Proceed with element diff")
        if(len(oldItemDict) == len(newItemDict)) :
            for x in newItemDict.keys():
                self.is_same_columns_exist(newItemDict[x] , oldItemDict[x],t)        
                
        
        print("printing all") 
        print(t.modified_dict)
        with open('diff.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in t.modified_dict.items():
                writer.writerow([key, value])  
        csvfile.close()
 
compareTableData()
        
       
                
            
        




    