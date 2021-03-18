import matplotlib.pyplot as plt
from matplotlib import rcParams 
rcParams.update({'figure.autolayout': True})
  
def a_nonignoring_verbose(n : int) -> int: 
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

def a_nonignoring(n : int) -> int: 
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

def a_verbose(n: int) -> int:
  '''
  This is the most verbose version. It can show you the progression. 
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

def a(n : int) -> int: 
  seens = {}  
  while n not in seens:  
    if n == 0:
      return len(seens) + 2 # +2 for 0.0 and 1.0
    else:
      seens[n] = True
      n = abs((n << 1) - (10 ** len(str(n))))
  return len(seens)
 


def compute_all(upto: int, start: int = 0, plot: bool = True, create_b_file: bool = False):
  '''
  Computes the sequence upto the given number. You can change the starting value with start kwarg.

  Set plot=True to see the results in a plot. 
  
  Set create_b_file=True to save the result to a b_file, refer to OEIS for more info.

  Set func kwarg for a custom function.
  '''
  assert(start >= 0)
  assert(start < upto)
    
  X = range(start, upto+1)
  Y = [a(n) for n in X]
  
  if plot:
    ax = plt.axes()
    ax.scatter(X, Y, c='black')
    ax.set_title("Burning Castle Sequence")
    ax.set_xlabel("Number")
    ax.set_ylabel("Iterations") 
    plt.show() 

  if create_b_file:
    # b_file is for OEIS. It is a file
    towrite = '\n'.join([str(x) + " " + str(y) for x, y in zip(X, Y)])
    f = open("out/BT_"+str(start)+"_"+str(upto)+".txt","w") 
    f.write(towrite) 
    f.close() 

  return Y

if __name__ == "__main__":
  compute_all(5000000)
  #a_verbose(123)