# FunDB

'FunDB for local dict structured database for python


* Easy to use
* Offline
* python dictnary format

# INSTALLATION:

```perl
$ python3 -m pip install fundb
```

## IMPORT AND INTI:

```python
>>> from fundb import fdb
>>> db = fdb('nameOfDb',  'secret',  rotate = 8000)
```

## CREATE DB:

* It over write data
* (type) dict only

```python
>>> Data = {'name': 'cat', 'age': 2}
>>> db.write(Data)
```

## READ DATA:
* (type) dict only

```python
>>> db.read()
{'name': 'cat', 'age': 2}
```

## NSERT PARRENT KEY:

```python
>>> db.insert('key1', ['value1', 'value2'])
{'name': 'cat', 'age': 2, 'key1': ['value1', 'value2']}
```

## REMOVE PARRENT KEY:

```python
>>> db.remove('key1')
{'name': 'cat', 'age': 2}
```

## GET VALUE FROM PARRENT KEY:

```python
>>> db.getval('age')
2
```
## SEARCH VALUE:

```python
>>> tmp = db.search('ca')
>>> list[tmp]
[{'name': 'cat'}]
```

## DB INFO:

```python
>>> db.db_info()
{'Name': 'nameOfDb.dbf', 'Created': 'Fri Mar 12 07:52:32 2021', 'Modifyed': 'Fri Mar 12 07:52:32 2021', 'Size': 120, 'Mode': 33152, 'UId': 1000, 'GId': 1000}
```

## FREE READ AND WRITE:
* Insert Any format

```python
>>> Data2 = 'String type'
>>> db.free_write(Data2)
>>> db.free_read()
'String type'
```
