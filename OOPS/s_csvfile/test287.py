from zipfile import ZipFile, ZIP_DEFLATED

#zip the file

f=ZipFile('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/test287.zip','w',ZIP_DEFLATED)
f.write('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/zipunziofolders/file1.txt', 'file1.txt')
f.write('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/zipunziofolders/file2.txt', 'file2.txt')
f.write('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/zipunziofolders/file3.txt', 'file3.txt')

print('zip is doen ')

