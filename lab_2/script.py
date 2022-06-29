
import magic
import glob
import hashlib

##task 1##
filenames= glob.glob("Evidence1/*")

for filename in filenames:
    print(filename, magic.from_file(filename))
    print(filename, magic.from_buffer(open(filename,"rb").read(2048)))

##task 2##
filenames= glob.glob("Evidence2/*")

for filename in filenames:
    with open(filename,'rb') as inputFile:
        data=inputFile.read()
        print('--------------',filename,'-----------------')
        print(hashlib,hashlib.md5(data).hexdigest())
        print(hashlib,hashlib.sha1(data).hexdigest())
        print(hashlib,hashlib.sha256(data).hexdigest())
          # different hashes

##task 3 ##
filenames= glob.glob("Evidence3/*")

for filename in filenames:
    with open(filename,'rb') as inputFile:
        data=inputFile.read()
        print('--------------',filename,'-----------------')
        print(hashlib,hashlib.md5(data).hexdigest())
        print(hashlib,hashlib.sha1(data).hexdigest())
        print(hashlib,hashlib.sha256(data).hexdigest())
        #same hash#

##task 3.b ##
filenames= glob.glob("Evidence4/*")
CHALLENGE="c15e32d27635f248c1c8b66bb012850e5b342119"

for filename in filenames:
    with open(filename,'rb') as inputFile:
        data=inputFile.read()
        if hashlib.sha1(data).hexdigest() == CHALLENGE:
            print('Found target file')
            print('------', filename, '-------')
            print(filename, magic.from_file(filename))
            break