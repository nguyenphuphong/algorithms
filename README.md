# Algorithms

## Bubble Sort

Given:

[64, 34, 25, 12, 22, 11, 90]

- 1: [34, 25, 12, 22, 11, 64, 90] -> 6 comparison
- 2: [25, 12, 22, 11, 34, 64, 90] -> 5 comparison
- 3: [12, 22, 11, 25, 34, 64, 90] -> 4 comparison
- 4: [12, 11, 22, 25, 34, 64, 90] -> 3 comparison
- 5: [11, 12, 22, 25, 34, 64, 90] -> 2 comparison
- 6: [11, 12, 22, 25, 34, 64, 90] -> 1 comparison

$T_n = 1 + 2 + ... + (n - 1) = \frac{1}{2}(n - 1)n, \forall n \geq 2$

$T_n = \frac{1}{2}n^2 - \frac{1}{2}n \leq \frac{1}{2}n^2$

$T_n = \frac{1}{2}n^2 - \frac{1}{2}n = \frac{1}{4}n^2 + \frac{1}{4}n^2 - \frac{2}{4}n = \frac{1}{4}n^2 + \frac{1}{4}n(n - 2) \geq \frac{1}{4}n^2$

$\frac{1}{4}n^2 \leq T_n \leq \frac{1}{2}n^2$

$\theta_n = n^2$
