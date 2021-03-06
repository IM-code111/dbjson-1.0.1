# **dbjson**
## **Get started**
### **things that you need:**
****
* **Python**

  - of course you need it

## **Installation**
****
```
$- pip install DBJSONS==1.0.2
```

## **What is dbjson?**
****
### `dbjson` is [Python](https://www.python.org/) module

Everyone say `JSON` can't be used as database but I don't think `JSON` can't be used as database

With this module you can use `JSON` as database since `JSON` is just [Python](https://www.python.org/) dictionary

## **Example Code**
****
**Creating json file**
```py
import dbjson as db

db.new('database')
```
**Add a data inside our database**
```py
db.data().new('database','data1','value1')
```
### If you open the `JSON` file you can see that `JSON` file will automatically update
```json
//Before
{}
//After
{"data1": "value1"}
```
**How about we want to edit the data?**
### Well,you can use `rewrite` method
```py
db.data().rewrite('database','data1','value2')
```
### check the `JSON` file
```json
//Before
{"data1": "value1"}
//After
{"data1": "value2"}
```
### To remove data we use `remove` method
```py
db.data().remove('database','data1')
```
```json
//Before
{"data1": "value2"}
//After
{}
```
### To remove all the data in our database,we use `end` method
```py
db.data().end('database')
```
## **Quicklinks**
****
### [**Discord Server**](https://discord.gg/h3SWAaHa22)

## **License**
****
# MIT License

## Copyright (c) `2021` <muhammad184276@gmail.com>
****
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.**
****
