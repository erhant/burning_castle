import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams 
rcParams.update({'figure.autolayout': True})

SEQUENCE_NAME = "Burning Castle Sequence" 
 
def compute(x: int, verbose: bool = False) -> int:
  '''
  This is the most verbose version. It can show you the progression.
  ''' 
  seens = {} # this is our dictionary, stored whether we have seen a number or not
  def see(x):
    seens[x] = True
  num_digits = lambda x : len(str(x)) 
  is_not_seen = lambda x : x not in seens 

  while is_not_seen(x): 
    see(x)
    if verbose: 
      print(x, "->", end=" ")    
    if x == 0: 
      x = 1
    else:
      x = abs((x << 1) - int('1' + '0'*num_digits(x)) ) 

  if verbose: 
    print(str(x)+"\n"+str(len(seens))+" values seen.") 
  return len(seens)

def compute_optim(x : int): 
  '''
  Simplest version using dictionary.  
  ''' 
  seens = {} 
  while x not in seens:  
    seens[x] = True
    x = abs((x << 1) - int('1' + '0'*len(str(x)))) if x != 0 else 1     
  return len(seens)

def compute_all(upto: int, start: int = 0, plot: bool = True, create_b_file: bool = False, func = compute_optim):
  '''
  Computes the sequence upto the given number. You can change the starting value with start kwarg.

  Set plot=True to see the results in a plot. 
  
  Set create_b_file=True to save the result to a b_file, refer to OEIS for more info.

  Set func kwarg for a custom function.
  '''
  assert(start >= 0)
  assert(start < upto)
  X = range(start, upto+1)
  Y = [func(x) for x in X]
  
  if plot:
    ax = plt.axes()
    ax.scatter(X, Y, c='black')
    ax.set_title(SEQUENCE_NAME)
    ax.set_xlabel("Starting Number")
    ax.set_ylabel("Number of Unique Values") 
    plt.show() 

  if create_b_file:
    # b_file is for OEIS. It is a file
    towrite = '\n'.join([str(x) + " " + str(y) for x, y in zip(X, Y)])
    f = open("out/BT_"+str(start)+"_"+str(upto)+".txt","w") 
    f.write(towrite) 
    f.close() 


if __name__ == "__main__":
  compute_all(500000, plot=True, func=compute_optim)
  #compute(100, verbose=True)
  #print(compute_optim(1000))