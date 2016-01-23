import sys

def fizzbuzz(n):
  for i in range(1,n+1):
    if i % 2 == 0:
      if i % 3 == 0:
        print 'fizzbuzz'
      else:
        print 'fizz'
    elif i % 3 == 0:
      print 'buzz'
    else:
      print i

if __name__ == '__main__':
  n = int(sys.argv[1])
  fizzbuzz(n)
