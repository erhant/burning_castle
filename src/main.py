import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams 
rcParams.update({'figure.autolayout': True})

SEQUENCE_NAME = "Burning Towers Sequence" 

def compute_optim(x):
  '''
  A bit more concise, nothing verbose.
  '''
  if x == 0:
    return 2 # 0.0 -> 1.0 -> 1.0 ... 

  subDivTen = int('1'+'0'*(len(str(x))-1))
  sub = (subDivTen << 3) + (subDivTen << 1)  # x * 10 = x * (8 + 2) = x * 2^3 + x *  2^1 = x << 3 + x << 1
   
  # memoize results 
  memo = np.zeros(sub) # we can see at most "sub" many values
  memo[x] = 1

  seens = 1 
  while True:
    x = int(abs((x << 1) - sub))
    if memo[x] == 1:
      break
    else:
      seens += 1
      memo[x] = 1
      while x < subDivTen:
        sub = subDivTen
        subDivTen = int(sub/10) 

  return seens
 
def compute(x, verbose=False): 
  '''
  Compute the Burning Tower value for 0.x. Note that 0.x >= 0.1 because x is an integer and it can't start with 0.
  '''
  if x == 0:
    if verbose:
      print("0 -> 1 -> 1")
      print("2 unique values seen.") 
    return 2  
  #sub = 10**int(np.ceil(np.log10(x))) # this was the old formula, then I decided to use strings instead
  sub = int('1'+'0'*(len(str(x))))
  subDivTen = int(sub/10) 

  # memoize results 
  memo = np.zeros(sub) # we can see at most "sub" many values
  memo[x] = 1

  seens = 1 
  if verbose:
    print(x, "->", end=" ")
  while True:
    x = int(abs((x << 1) - sub))
    if memo[x] == 1:
      break
    else:
      seens += 1
      memo[x] = 1
      while x < subDivTen:
        sub = subDivTen
        subDivTen = int(sub/10)
    if verbose:
      print(x, "->", end=" ")

  if verbose:  
    print(x) 
    print(seens,"unique values seen.") 
  return seens
 

def compute_all(upto, start=0, plot=True):
  '''
  Computes the sequence upto the given number. 
  '''
  assert(start < upto)
  X = range(start, upto+1)
  Y = [compute_optim(x) for x in X]
  
  if plot:
    ax = plt.axes()
    ax.scatter(X, Y, c='black')
    ax.set_title(SEQUENCE_NAME)
    ax.set_xlabel("Starting Number")
    ax.set_ylabel("Number of Unique Values") 
    plt.show() 

  return Y

if __name__ == "__main__":
  #compute_all(25000)
  compute(794, verbose=True)