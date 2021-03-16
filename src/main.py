import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams 
rcParams.update({'figure.autolayout': True})

SEQUENCE_NAME = "Burning Castle Sequence" 
 
def compute_verbose(x: int) -> int:
  '''
  This is the most verbose version. It can show you the progression.
  ''' 
  seens = {} # this is our dictionary, stored whether we have seen a number or not
  x = int(str(x).strip())    
  while  x not in seens: 
    seens[x] = True 
    print(x, "->", end=" ")    
    x = abs((x << 1) - (10 ** len(str(x))))
    x = int(str(x).strip())
 
  print(str(x)+"\n"+str(len(seens))+" values seen.") 
  return len(seens)

def compute(x : int): 
  '''
  Simplest version using dictionary.  
  ''' 
  seens = {}  
  while x not in seens:  
    seens[x] = True
    x = abs((x << 1) - (10 ** len(str(x))))
  return len(seens)
 

def compute_all(upto: int, start: int = 0, plot: bool = True, create_b_file: bool = False, func = compute):
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

  return Y

if __name__ == "__main__":
  compute_all(50000000, plot=True, func=compute) 
  #compute_verbose(100)
  #print(compute(1000))