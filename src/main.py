import matplotlib.pyplot as plt
from matplotlib import rcParams 
rcParams.update({'figure.autolayout': True})
  
def formerly_A343274_verbose(n : int) -> int: 
  '''
  A verbose version of formerly A343274, that shows the number sequence.
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

def formerly_A342631_verbose(n: int) -> int:
  '''
  A verbose version of formerly A342631, that shows the number sequence.
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


def formerly_A342631(n : int) -> int: 
  '''
  a(n) = number of distinct values in the recursive iterations of 
  f(x) = f(g(|2x-1|)) starting from a real number x where x = 0 or 
  0.1 <= x < 1, n is the fractional part of x, and g(x) removes 
  prepending zeros of x.

  Equivalently, x = n/10^(num digits in n)
  '''
  seens = {}  
  while n not in seens:  
    if n == 0:
      return len(seens) + 2 # +2 for 0.0 and 1.0
    else:
      seens[n] = True
      n = abs((n << 1) - (10 ** len(str(n))))
  return len(seens)
 

def formerly_A343274(n : int) -> int: 
  '''
  a(n) = number of distinct values in the recursive iterations of 
  f(x) = f(|2x-1|) starting from a real number x where x = 0 or 
  0.1 <= x < 1, n is the fractional part of x.

  Equivalently, x = n/10^(num digits in n)
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
  a(n) = |2n-10^num_digits(n)|, n > 0
  ''' 
  return abs((n << 1) - (10 ** len(str(n))))

def compute(upto: int, offset: int, plot: bool = True, bfile_name: str = None, a : callable = A343275):
  '''Computes the sequence for numbers in range [offset, upto]

  Set plot=True to see the results in a plot. 
  Set bfile_name kwarg to output a b file for OEIS.
  Set a kwarg for a custom sequence. 
  '''  
  assert(offset < upto)
    
  N = range(offset, upto+1) # inclusive
  A_N = [a(n) for n in N]
  
  if plot:
    ax = plt.axes()
    ax.scatter(N, A_N, c='black') 
    ax.set_xlabel("n")
    ax.set_ylabel("a(n)") 
    plt.show() 

  if bfile_name != None:
    towrite = '\n'.join([str(n) + " " + str(a_n) for n, a_n in zip(N, A_N)])
    f = open("out/"+bfile_name,"w") 
    f.write(towrite) 
    f.close() 

if __name__ == "__main__":
  compute(10000, 1, bfile_name='b343275.txt', a=A343275) 
