f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test273.txt','r')



line=f.readline()

while line!='':  #line not equal to empty
      print(line,end='')
      #read next line
      line = f.readline()

f.close()
