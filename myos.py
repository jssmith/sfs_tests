import os as origos

O_RDWR = origos.O_RDWR
O_CREAT = origos.O_CREAT

def open(path, flags, mode=0o777):
    print('calling open')
    return savedos_open(path, flags, mode)

def write(fd, str):
    print('calling write')
    return savedos_write(fd, str)

def read(fd, n):
    print('calling read')
    return origos.read(fd, n)

savedos_open = origos.open
origos.open = open

savedos_write = origos.write
origos.write = write
