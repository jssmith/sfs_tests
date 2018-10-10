import os

def test1():
    print('in othermodule test1')
    print(os.open)
    fd = os.open('test1.txt', os.O_RDWR | os.O_CREAT)
    os.write(fd, 'hello\n'.encode('utf-8'))
