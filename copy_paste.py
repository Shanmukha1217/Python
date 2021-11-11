from io import StringIO


handle = open("/media/shanmukha/DATA/Python/File_Handling/demo.txt")
strng =handle.read()

paste = open("/media/shanmukha/DATA/Python/File_Handling/test.txt",'a')

paste.write(strng)
paste.flush()
paste.close()
print('done')
