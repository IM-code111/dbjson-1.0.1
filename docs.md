# ![dbjson logo](https://media.discordapp.net/attachments/796223053440483328/799125635367698452/dbjson.png?width=100&height=100)
# **Documentation**

## Adding new database
## `dbjson.add(name)`
### Example code:
```py
import dbjson as db

db.new('database')
```
### **Raise:**
- **DatabaseError**
    - Database already exist in directory
### **Return**
- **None**
****
## Adding Data
## `dbjson.data().new(db, data, value)`
### Example code:
```py
db.data().new('database', 'Mark', '23')
```
### **Raise**
- **DatabaseError**
    - Database not found in directory
- **DataError**
    - Data already exist
### **Return**
- **Data Value**
****
## Edit Specific Data
## `dbjson.data().rewrite(db, data, newValue)`
### Example code:
```py
db.data().rewrite('database', 'Mark', '30')
```
### **Raise**
- **DatabaseError**
    - Database not found in directory
- **DataError**
    - Data not exist
### **Return**
- **Data new value**
****
## Get Specific Data
## `dbjson.data().getData(db, data)`
### Example Code:
```py
db.data().getData('database', 'Mark')
```
### **Raise**
- **DatabaseError**
    - Database not found in directory
- **DataError**
    - Data not exist
### **Return**
- **Data name and the value in dict**
****
## Get all data in database
## `dbjson.data().dataAll(db)`
### Example Code
```py
db.data().dataAll('database')
```
### **Raise**
- **DatabaseError**
    - Database not found in directory
### **Return**
- **All data inside database in dict**
****
## Remove Specific Data
## `dbjson.data().remove(db, data)`
### Example Code:
```py
db.data().remove('database', 'Mark')
```
### **Raise**
- **DatabaseError**
    - Database not found in directory
- **DataError**
    - Data not exist
### **Return**
- **Data value**
****
## Remove all data
## `dbjson.data().end(db)`
### Example Code:
```py
db.data().end('database')
```
### **Raise**
- **DatabaseError**
    - Database not found in directory
### **Return**
- **None**
****
## Category
### Category is data class
### Let me give you example
### `{"key": {"key2": "Value"}}`
### So, data class is just basically dict inside dict
****
## Convert non-data class to data class
## `dbjson.category().convert(db, data)`
_Note: this will make the data lost it value_
```py
 db.category().convert('database', 'Mark')
 ```
### **Raise**
- **DatabaseError**
    - Database not found in directory
- **DataError**
    - Data not exist
### **Return**
- **Data value**
****
## **Add Data Class**
## `dbjson.category().new(db, data)`
### Example Code:
```py
db.category().new('database', 'Dave')
```
### **Raise**
- **DatabaseError**
    - Database not found in directory
- **DataError**
    - Data already exist
### **Return**
- **Data Class Value**
****
## **Add Data Inside Data Class**
## `dbjson.category().add(db, dataClass, data, value)`
### Example Code:
```py
db.category().add('database', 'Dave', 'age', '32')
```
### **Raise**
- **DatabaseError**
    - Database not found in directory
- **DataError**
    - Data already exist
### **Return**
- **Data Class and The Data inside it in dict**
****
## **Edit Specific Data Inside Data Class**
## `dbjson.category().rewrite(db, dataClass, data, newValue)`
### Example Code:
```py
db.category().rewrite('database', 'Dave', 'age', '22')
```
### **Raise**
- **DatabaseError**
    - Database not found in directory
- **DataError**
    - Data not exist
### **Return**
- **Data Class and The Data inside it in dict**
****
## **Remove Specific Data Inside Data Class**
## `dbjson.category().rewrite(db, dataClass, data, newValue)`
### Example Code:
```py
db.category().rewrite('database', 'Dave', 'age')
```
### **Raise**
- **DatabaseError**
    - Database not found in directory
- **DataError**
    - Data not exist
### **Return**
- **Data Class and The Data inside it in dict**