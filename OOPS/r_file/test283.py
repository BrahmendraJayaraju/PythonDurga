import os


fname=input('enter the file name:')
if os.path.isfile('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/'+fname):
    print('file is present:',fname)
    lcount=wcount=ccount=0
    f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/'+fname,'r')

    for line in f:
        lcount=lcount+1
        n_of_words_currentline=len(line.split())
        wcount=wcount+n_of_words_currentline
        noofcharacters_in_currentline=len(line)
        ccount=ccount+noofcharacters_in_currentline
print('the no of lines :',lcount)
print('the no of words:',wcount)
print('the no of characters:',ccount)