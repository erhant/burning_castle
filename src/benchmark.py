import time

def compare(f1, f2, vals, repeat_each, title1="first", title2="second"):
  start = time.time()
  for i in vals:
    for j in repeat_each:
      f1(i)
  end = time.time()
  print(end - start,"ms for",title1,"function.")

  start = time.time()
  for i in vals:
    for j in repeat_each:
      f2(i)
  end = time.time()
  print(end - start,"ms for",title2,"function.")
 

## Compare 10 ** a with int('1' + '0'*a)
compare(lambda x : 10**x, lambda x : int('1'+'0'*x) if x !=0 else 1, range(100), range(10000), title1="**", title2="string")


'''
Results:

- x*10 works faster than (x<<3) + (x<<1)
- For smaller x, int('1'+'0'*x) works better than 10**x. But then the power takes over. But when we add the constraint for 0, it becomes worse. 
'''