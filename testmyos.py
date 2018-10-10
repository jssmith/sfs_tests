import myos as os
import io
import othermodule


def test1():
    print('in testmyos test1')
    print(os.open)
    fd = os.open('test1.txt', os.O_RDWR | os.O_CREAT)
    os.write(fd, 'hello\n'.encode('utf-8'))


def test2():
    print('in testmyos test2')
    f = io.open('test2.txt', 'w')
    f.write('hello\n')

# def test3():
#     print('in testmyos test3')
#     print(open)
#     f = open('test3.txt', 'w')
#     f.write('hello\n')

if __name__ == '__main__':
    test1()
    othermodule.test1()
    test2()
    # test3()
