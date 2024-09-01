# Implementation of Factoring Methods

As part of my research project in Cryptography under the supervision of Professor Takei in John Abbott College, I implemented different factoring algorithms in order to calculate the factoring times of semi-primes of various lengths.

## Implementations

### Quadratic Sieve - R

I implemented the quadratic sieve factorization algorithm in R, which connected to a remote MySQL database and stored the semi-prime length, its factorization time as well as the number itself.

### Python

In order to generate large semi-primes, I generate 2 large primes by making an API call to a prime generator of custom lengths, and multiply them together. Once the semi-prime generated, I factorize it with the desired algorithm, then store the computing time, the number and its length to my MySQL Database.

#### RSA and Fermat Factorization Algorithms

Implemented both algorithm from scratch, and manually optimizing it to achieve the best times possible.
