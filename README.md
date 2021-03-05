# Double-Dec-Abs Sequence
This is a made up sequence by me, the question is how long are the iterations?

```
start with a = 0,xyz... where x,y,z,... are digits.
do { 
  a := |2a - 1|
  if a < 0.1
    a := 10 * a  
} while a != |2a - 1|
```
