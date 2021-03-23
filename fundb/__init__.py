__doc__ = '''FunDB for local dict structured database for python


                 <<< FUN 𝌆 >>>



   -> Easy to use
   -> Offline
   -> python dictnary format

IMPORT AND INTI:
    >>> from fundb import fdb
    >>> db = fdb('nameOfDb',  'secret',  rotate = 8000)

        > db_Name = 'nameOfDb'   [required]
        > password = 'secret'    [optional]
        > rotate = 8000          [optional]

CREATE DB:
   -> It over write data
   -> (type) dict only

    >>> Data = {'name': 'cat', 'age': 2}
    >>> db.write(Data)

        > data = Data
        > verbose = False

READ DATA:
   -> (type) dict only

    >>> db.read()
    {'name': 'cat', 'age': 2}

INSERT PARRENT KEY:
    >>> db.insert('key1', ['value1', 'value2'])
    {'name': 'cat', 'age': 2, 'key1': ['value1', 'value2']}

        > key = 'key1'
        > value = ['value1', 'value2']

REMOVE PARRENT KEY:
    >>> db.remove('key1')
    {'name': 'cat', 'age': 2}

        > key = 'key1'

GET VALUE FROM PARRENT KEY:
    >>> db.getval('age')
    2

        > key = 'age'

SEARCH VALUE:
    >>> tmp = db.search('ca')
    >>> list[tmp]
    [{'name': 'cat'}]

        > string = 'ca'

DB INFO:
    >>> db.db_info()
    {'Name': 'nameOfDb.dbf', 'Created': 'Fri Mar 12 07:52:32 2021', 'Modifyed': 'Fri Mar 12 07:52:32 2021', 'Size': 120, 'Mode': 33152, 'UId': 1000, 'GId': 1000}

FREE READ AND WRITE:
   -> Insert Any format

    >>> Data2 = 'String type'
    >>> db.free_write(Data2)

        > data = Data2

    >>> db.free_read()
    'String type'

'''

from fundb.fundb import Fundb as fdb
