<p align="center">
  <img src="img/5monfire.jpg">
</p>

# Burning Castle
This repository includes codes and plots for the following OEIS submissions: 

- [A342631](https://oeis.org/A342631) `a(n)` is the number of distinct values in the recursive iterations of `f(x) = f(g(|2x-1|))` starting from a real number `x` where `x = 0` or `0.1 <= x < 1`, `n` is the decimal part of `x`, and `g(x)` removes prepending zeros of `x`. I thought this looked like a burning castle image, thus has been given the name of this repository. The image seen above is the plot of [A342631](https://oeis.org/A342631) up to 5 million, _with some additional visual flare :)_

![5000_A342631](img/upto5000.png) 

- [A343274 (draft)](https://oeis.org/draft/A343274) `a(n)` is the number of distinct values in the recursive iterations of `f(x) = f(|2x-1|)` starting from a real number  `x` where `x = 0` or `0.1 <= x < 1`, `n` is the decimal part of `x`. The only difference between [A342631](https://oeis.org/A342631) and this one is the `g` function inside `f`; however, that significantly changes the resulting plot.

![5000_A343274](img/upto5000_2.png) 

- [A343275 (draft)](https://oeis.org/draft/A343275) `a(n) = |2n-10^num_digits(n)|`, `n` is a positive integer. This is basically what is done inside [A342631](https://oeis.org/A342631) and [A343274 (draft)](https://oeis.org/draft/A343274). The plots are V shaped for each interval `0`-`10`-`100`-`1000` and so on.

![5000_A343275](img/upto5000_3.png) 