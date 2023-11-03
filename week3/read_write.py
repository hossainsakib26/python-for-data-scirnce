try:
    f = open('My_data_frame.csv','r')
    s = f.readline()
    f.close()
    print(s)
except:
    print('No such files')
finally:
    print('1: Program complete')

try:
    f = open('no_such_files', 'r')
    s = f.readline()
    f.close()
    print(s)
except:
    print('No such files')
finally:
    print('2: Program complete')

try:
    f = open('myTextFile', 'w')
    f.write('hello world')
    f.close()
except:
    print('Cannot create file')
finally:
    print('3: Program complete')

