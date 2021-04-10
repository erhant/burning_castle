import matplotlib.pyplot as plt
from matplotlib import rcParams 
rcParams.update({'figure.autolayout': True})
  
def A343274_verbose(n : int) -> int: 
  '''
  A verbose version of A343274, that shows the number sequence.
  '''
  init_len = len(str(n)) 
  sub = 10 ** init_len
  seens = {}  
  while n not in seens:  
    if n == 0:
      print("0."+'0'.zfill(init_len), "-> 1."+'0'.zfill(init_len)+" -> 0."+'0'.zfill(init_len)) 
      print(str(len(seens)+2)+" distinct values seen.") 
      return len(seens) + 2 # +2 for 0.0 and 1.0
    else:
      seens[n] = True
      print("0."+str(n).zfill(init_len), "->", end=" ")    
      n = abs((n << 1) - sub)
    
  print("0."+str(n)+"\n"+str(len(seens))+" distinct values seen.") 
  return len(seens)

def A342631_verbose(n: int) -> int:
  '''
  A verbose version of A342631, that shows the number sequence.
  '''  
  seens = {} # this is our dictionary, stored whether we have seen a number or not 
  while n not in seens: 
    if n == 0:
      print("0."+str(n), "-> 1.0 -> 0.0") 
      print(str(len(seens)+2)+" distinct values seen.") 
      return len(seens) + 2 # +2 for 0.0 and 1.0
    else:
      seens[n] = True 
      print("0."+str(n), "->", end=" ")    
      n = abs((n << 1) - (10 ** len(str(n)))) 

  print("0."+str(n)+"\n"+str(len(seens))+" distinct values seen.") 
  return len(seens)


def A342631(n : int) -> int: 
  '''
  A342631(n) = number of distinct values in the recursive iterations of 
  f(x) = f(g(|2x-1|)) starting from a real number x where x = 0 or 
  0.1 <= x < 1, n is the decimal part of x, and g(x) removes 
  prepending zeros of x.
  '''
  seens = {}  
  while n not in seens:  
    if n == 0:
      return len(seens) + 2 # +2 for 0.0 and 1.0
    else:
      seens[n] = True
      n = abs((n << 1) - (10 ** len(str(n))))
  return len(seens)
 

def A343274(n : int) -> int: 
  '''
  A343274(n) = number of distinct values in the recursive iterations of 
  f(x) = f(|2x-1|) starting from a real number x where x = 0 or 
  0.1 <= x < 1, n is the decimal part of x.
  '''
  init_len = len(str(n)) 
  sub = 10 ** init_len
  seens = {}  
  while n not in seens:  
    if n == 0: 
      return len(seens) + 2 # +2 for 0.0 and 1.0
    else:
      seens[n] = True 
      n = abs((n << 1) - sub)
  return len(seens)

def A343275(n : int) -> int: 
  '''
  A343275(n) = |2n-10^num_digits(n)|, n > 0
  ''' 
  return abs((n << 1) - (10 ** len(str(n))))

def compute(upto: int, offset: int, plot: bool = True, bfile_name: str = None, a : callable = A342631):
  '''Computes the sequence upto the given number with an offset.

  Set plot=True to see the results in a plot. Set create_b_file to a string to save the result to a b_file as str_upto, refer to OEIS for more info.
  Set a kwarg for a custom sequence. Default is A342631.
  '''  
  assert(offset < upto)
    
  X = range(offset, upto+1) # inclusive
  Y = [a(n) for n in X]
  
  if plot:
    ax = plt.axes()
    ax.scatter(X, Y, c='black') 
    ax.set_xlabel("Number")
    ax.set_ylabel("Iterations") 
    plt.show() 

  if bfile_name != None:
    # b_file is for OEIS. It is a file
    towrite = '\n'.join([str(x) + " " + str(y) for x, y in zip(X, Y)])
    f = open("out/b"+bfile_name+"_"+str(upto)+".txt","w") 
    f.write(towrite) 
    f.close() 

  return Y

if __name__ == "__main__":
  compute(5000, 0, a=A342631) 