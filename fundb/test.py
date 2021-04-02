
from milkycow import *
from codelib.base import base64encode as benc
from codelib.base import base64decode as bdec
from re import search, ASCII
from getpass import getpass as ainput
from os import remove, stat
from time import ctime



RDATA = {
        "FNF" : "\u001b[31m[!] DBNotFound:\u001b[0m Please create data base with write().",
        "DWV" : "[✓] Data written db: {} bytes: {} data: {}.",
        "UDE" : "\u001b[31m[!] InvaliedPassword:\u001b[0m Unable to get data.",
        "TYE" : "\u001b[31m[!] InvaliedData:\u001b[0m Unable to get dictnary data use free_read().",
        "TYE2": "\u001b[31m[!] InvaliedData:\u001b[0m read() accepts only dictnary data use free_write().",
        "KEE" : "\u001b[31m[!] InvaliedKey:\u001b[0m key '{}' is not found in this database.",
        "TEI" : "\u001b[31m[!] InvaliedKey:\u001b[0m insert() only works with dictnary data.",
        "TER" : "\u001b[31m[!] InvaliedKey:\u001b[0m remove() only works with dictnary data.",
        "INE" : "\u001b[31m[!] InvaliedDBName:\u001b[0m Please Use valied database name.",
        "EXP" : [ "", None, ".", ".."]
        }



class Fundb:
    def __init__(self, db_name, password = "pass", rotate = 509, layer=0, rrotate=6):
        if(db_name in RDATA["EXP"]):
            raise Exception(RDATA["INE"])
        self.db_name = db_name
        self.passwd = password
        self.rotate = rotate
        self.layer = layer
        self.rrotate = rrotate
        self.exten = ".dbf"
        if(self.db_name == ""):
            raise Exception(RDATA["FNF"])

    def write(self, data ,verbose = False):
        """
        >>> # The data will be over write
        >>> # pass the data in dict
        >>> mdb.write({"name": "foo"})
        """
        if(type(data) != dict):
            raise Exception(RDATA["TYE2"])
        with open(self.db_name+self.exten, "w") as a:
            enc_data = encrypt(str(data), self.passwd, self.rotate, self.layer, self.rrotate)
            a.write(enc_data)
            a.close()
            if(verbose):
                return RDATA["DWV"].format(self.db_name, len(enc_data), data)
            else:
                return data

    def read(self):
        """
        >>> # It read only in dict format
        >>> mdb.read()
        """
        try:
            with open(self.db_name+self.exten, "r") as a:
                data = decrypt(a.read(), self.passwd, self.rotate, self.layer, self.rrotate)
                a.close()
                return eval(data)
        except UnicodeDecodeError:
            raise Exception(RDATA["UDE"])
        except FileNotFoundError:
            raise Exception(RDATA['FNF'])
        except TypeError:
            raise Exception(RDATA["TYE"])
        except:
            raise Exception(RDATA["TYE"])

    def free_write(self, data , verbose = False):
        """
        >>> # The data will be over write
        >>> # write what ever you want. use free_read() to get tha data back
        >>> mdb.free_write("data")
        """
        with open(self.db_name+self.exten, "w") as a:
            enc_data = encrypt(benc(str(data)), self.passwd, self.rotate, self.layer, self.rrotate)
            a.write(enc_data)
            a.close()
            if(verbose):
                return RDATA["DWV"].format(self.db_name, len(enc_data), data)
            else:
                return data

    def free_read(self):
        """
        >>> # It reads any format and return as str
        >>> mdb.free_read()
        """
        try:
            with open(self.db_name+self.exten, "r") as a:
                data = decrypt(a.read(), self.passwd, self.rotate, self.layer, self.rrotate)
                a.close()
                return bdec(data)
        except UnicodeDecodeError:
            raise Exception(RDATA["UDE"])
        except FileNotFoundError:
            raise Exception(RDATA["FNF"])

    def rmdb(self):
        return remove(self.db_name+self.exten)

    def db_info(self):
        """
        >>> # data base Information
        >>> mdb.db_info()
        """
        data = list(stat(self.db_name+self.exten))
        info = {"Name": self.db_name+self.exten}
        info["Created"] = ctime(data[-3])
        info["Modifyed"] = ctime(data[-1])
        info["Size"] = data[-4]
        info["Mode"] = data[0]
        info["UId"] = data[4]
        info["GId"] = data[5]
        return info

    def insert(self, key, value):
        try:
            data = self.read()
            data[key] = value
            self.write(data)
            return self.read()
        except TypeError:
            raise Exception(RDATA["TEI"])


    def remove(self, key):
        try:
            data = self.read()
            del data[key]
            self.write(data)
            return self.read()
        except KeyError:
            raise Exception(RDATA["KEE"].format(key))
        except TypeError:
            raise Exception(RDATA["TER"])



    def close(self):
        self.db_name = ""
        self.passwd = ""

