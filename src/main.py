import numpy as np

x = 100
if x % 10 == 0 or x == 1:
  # note: is this logic correct?
  sub = int(x*10)
else:
  sub = 10**int(np.ceil(np.log10(x)))
subDivTen = int(sub/10)

# need to keep track of the values we come accross 
memo = np.zeros(sub) # we can see at most "sub" many values
memo[x] = 1

seens = 1
print(x, "sub",sub)
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
  print(x)
  
print("looped back to",x)
print(seens,"unique values seen.")
