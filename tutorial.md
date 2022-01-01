## Installing on Machine
**Windows**

`$ pip install git+https://github.com/TheReaper62/Subapy.git`


**MacOS**

`$ pip3 install git+https://github.com/TheReaper62/Subapy.git`


## Importing into Project
`import subapy`


## Create a new subapy Client
`supa_client = subapy.Client(db_url='YOUR_DB_URL', api_key='YOUR_API_KEY')`
**DB_URL and API_KEY are required.**
*DB_URL is the unique portion of the URL of the database or the Full URL of the database server.*
*You can also use anon_key or service_key to specify the API key.*


## Reading
**********
### Read all data from the database

`data: list[dict[str,Any]] = supa_client.read('*')`

**equivalent to**

`data: list[dict[str,Any]] = supa_client.read('all')`
```
Output
>>>[{'age': '18', 'name': 'John', 'id': '1'}, {'age': '19', 'name': 'Jane', 'id': '2'}]
```

### Read all data from the 'name' column

`data: list[dict[str, Any]] = supa_client.read('name')`
```
Output
>>>[{'name': 'John'}, {'name': 'Jane'}]
```

### Read data from multiple columns

`data: list[dict[str, Any]] = supa_client.read(['name', 'age'])`
```
Output
>>>[{'age': '18', 'name': 'John''}, {'age': '19', 'name': 'Jane'}]
```

### Read Data for Ids greater than 10 (Filtering)

```py
filter_1 = subapy.Filter('id', 'gt', '10')
data: list[dict[str, Any]] = supa_client.read('users', filters=filter_1)
```
### Syntax for creating Filter

`filter_2 = subapy.Filter('column_name', 'operator', 'value_for_operator')`

*Note: You can also use a list of filters*

### Example Usage: 

`data: list[dict[str, Any]] = supa_client.read('users', filters=[filter_1, filter_2])`


## All Supported Operators
Making use of PostgREST syntax, you can also use the following operators to filter:
- 'lt' for less than
- 'lte' for less than or equal to
- 'ge' for greater than
- 'gte' for greater than or equal to
- 'eq' for equal to
- 'neq' for not equal to
- 'in' for in
- 'is' for is
- 'fts' for full text search


## Insert
*********
## Create New Row

`data = client.insert({"name":"Joe", "age":21})`

*Returns new data*

**Inserting Multiple Rows Supported**

```py
data = client.insert([
    {"name":"Joe", "age":21},
    {"name":"Bob", "age":25}
    ])
```

## Upsert
Update if exist, else insert

Select row(s) to update using Filter

`data = client.insert({"name":"Joe", "age":21}, filters=Filter('id','eq','2'), upsert=True)`


## Update
Updates matched rows, match all rows by default. 

Use Filters

`data = client.update({"age":22},Filter('name','eq','Joe'))`
*Returns replaced values*


## Delete
Deletes matched rows, match all rows by default. 

Use Filters

`data = client.delete(Filter('name','eq','Jane'))`
*Returns None*