f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test268.txt','w')


#to write only values
d={100:'durga',200:'ravi'}
f.writelines([d[100],d[200]])

#or below method

#to write only values
d={100:'durga',200:'ravi'}
f.writelines(d.values())