import os
from os import path
import json

class DatabaseError(Exception):
    pass

class DataError(Exception):
    pass

def new(db):
    if path.exists(f'{db}.json'):
        raise DatabaseError(f"Database name {db} already exist\nTry different name instead")
    else:
        with open(f'{db}.json','w') as f:
            f.write("{}")
        return None
        
class data:
    
    def new(self, db, key, value):
        if not path.exists(f'{db}.json'):
            raise DatabaseError(f"Database name {db} not exist")
        else:
            with open(f'{db}.json','r') as f:
                inside = json.load(f)
            if str(key) in inside:
                raise DataError(f'Database already have "{key}" data\ndid you mean "rewrite"?')
            else:
                inside[str(key)] = str(value)
                with open(f'{db}.json','w') as f:
                    json.dump(inside,f)
                return key
                    
    def rewrite(self, db, key, newValue):
        if not path.exists(f'{db}.json'):
            raise DatabaseError(f"Database name {db} not exist")
        else:
            with open(f'{db}.json','r') as f:
                inside = json.load(f)
            if str(key) not in inside:
                raise DataError(f'Database not have "{key}" data\ndid you mean "new"?')
            else:
                inside[str(key)] = str(newValue)
                with open(f'{db}.json','w') as f:
                    json.dump(inside,f)
                return inside[str(key)]
                    
    def getData(self, db, key):
        if not path.exists(f'{db}.json'):
            raise DatabaseError(f"Database name {db} not exist")
        else:
            with open(f'{db}.json','r') as f:
                inside = json.load(f)
            if str(key) not in inside:
                raise DataError(f'Database not have "{key}" data\ntry "new"?')
            else:
                return {str(key): inside[str(key)]}
            
    def dataAll(self, db):
        if not path.exists(f'{db}.json'):
            raise DatabaseError(f"Database name {db} not exist")
        else:
            with open(f'{db}.json','r') as f:
                inside = json.load(f)
            return inside
        
    def end(self, db):
        if not path.exists(f'{db}.json'):
            raise DatabaseError(f"Database name {db} not exist")
        else:
            with open(f'{db}.json','r') as f:
                inside = json.load(f)
            inside = {}
            with open(f'{db}.json','w') as f:
                json.dump(inside,f)
            return None
        
    def remove(self, db, key):
        if not path.exists(f'{db}.json'):
            raise DatabaseError(f"Database name {db} not exist")
        else:
            with open(f'{db}.json','r') as f:
                inside = json.load(f)
            if str(key) not in inside:
                raise DataError(f'Database not have "{key}" data\ntry "new"?')
            else:
                inside.pop(str(key))
                with open(f'{db}.json','w') as f:
                    json.dump(inside,f)
                return inside[str(key)]
                
class category:
    
    def convert(self, db, key):
        if not path.exists(f'{db}.json'):
            raise DatabaseError(f"Database name {db} not exist")
        else:
            with open(f'{db}.json','r') as f:
                inside = json.load(f)
            if str(key) not in inside:
                raise DataError(f'Database not have "{key}" data\ntry "new"?')
            else:
                inside[str(key)] = {}
                with open(f'{db}.json','w') as f:
                    json.dump(inside,f)
                return inside[str(key)]
                    
    def new(self, db, key):
        if not path.exists(f'{db}.json'):
            raise DatabaseError(f"Database name {db} not exist")
        else:
            with open(f'{db}.json','r') as f:
                inside = json.load(f)
            if str(key) in inside:
                raise DataError(f'Database already have "{key}" data\ndid you mean "oldNew"?')
            else:
                inside[str(key)] = {}
                with open(f'{db}.json','w') as f:
                    json.dump(inside,f)
                return inside[str(key)]
                
                    
    def add(self, db, oldkey, key, value):
        if not path.exists(f'{db}.json'):
            raise DatabaseError(f"Database name {db} not exist")
        else:
            with open(f'{db}.json','r') as f:
                inside = json.load(f)
            if oldkey not in inside:
                raise DataError(f'Database not have "{key}" data\ntry "new"?')
            else:
                ctgry = inside[str(oldkey)]
                if str(key) in ctgry:
                    raise DataError(f'Data Class already have "{key}" data\ntry different name')
                else:
                    ctgry[str(key)] = str(value)
                    with open(f'{db}.json','w') as f:
                        json.dump(inside,f)
                    return ctgry
                        
    def rewrite(self, db, oldkey, key, newValue):
        if not path.exists(f'{db}.json'):
            raise DatabaseError(f"Database name {db} not exist")
        else:
            with open(f'{db}.json','r') as f:
                inside = json.load(f)
            if oldkey not in inside:
                raise DataError(f'Database not have "{key}" data\ntry "new"?')
            else:
                ctgry = inside[str(oldkey)]
                if str(key) not in ctgry:
                    raise DataError(f'Data Class not have "{key}" data\ntry "add"?')
                else:
                    ctgry[str(key)] = str(newValue)
                    with open(f'{db}.json','w') as f:
                        json.dump(inside,f)
                    return ctgry
                
    def remove(self, db, oldkey, key):
        if not path.exists(f'{db}.json'):
            raise DatabaseError(f"Database name {db} not exist")
        else:
            with open(f'{db}.json','r') as f:
                inside = json.load(f)
            if oldkey not in inside:
                raise DataError(f'Database not have "{key}" data\ntry "new"?')
            else:
                ctgry = inside[str(oldkey)]
                if str(key) not in ctgry:
                    raise DataError(f'Data Class not have "{key}" data\ntry "add"?')
                else:
                    ctgry.pop(str(key))
                    with open(f'{db}.json','w') as f:
                        json.dump(inside,f)
                    return ctgry
                

    