#The provided code stub reads an integer n from STDIN. For all non-negative integers from 0 to n, print n*negative

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
      print(i*i*i)