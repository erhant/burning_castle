import matplotlib.pyplot as plt
from matplotlib import rcParams 
rcParams.update({'figure.autolayout': True})
  

def compute_verbose(x: int) -> int:
  '''
  This is the most verbose version. It can show you the progression. 
  
  This does not include the simulation for 1.0
  ''' 
  assert(x >= 0)
  if x == 0:
    print("0 -> 1 -> 1\n2 values seen.")    
    return 2
  elif x == 5 or (str(x)[0] == '5' and int(str(x)[1:]) == 0):
    # 500...0
    print(x,"-> 0 -> 1 -> 1\n3 values seen.")
    return 3
  else:
    seens = {} # this is our dictionary, stored whether we have seen a number or not 
    while  x not in seens: 
      seens[x] = True 
      print(x, "->", end=" ")    
      x = abs((x << 1) - (10 ** len(str(x)))) 
  
    print(str(x)+"\n"+str(len(seens))+" values seen.") 
    return len(seens)

def compute(x : int) -> int: 
  '''
  Simplest version using dictionary.  

  This does not include the simulation for 1.0
  ''' 
  assert(x >= 0)
  if x == 0: 
    return 2
  elif x == 5 or (str(x)[0] == '5' and int(str(x)[1:]) == 0):
    # 500...0 
    return 3
  else:
    seens = {}  
    while x not in seens:  
      seens[x] = True
      x = abs((x << 1) - (10 ** len(str(x))))
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
  Y = [compute(x) for x in X]
  
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
  #print(compute_all(100, plot=False))
  compute_verbose(12)