---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(pandas)=

# pandas

> \"Let\'s be clear: the work of science has nothing whatever to do with
> consensus. Consensus is the business of politics. Science, on the
> contrary, requires only one investigator who happens to be right,
> which means that he or she has results that are verifiable by
> reference to the real world. In science consensus is irrelevant. What
> is relevant is reproducible results.\" -- Michael Crichton

## Overview

[Pandas](https://en.wikipedia.org/wiki/NumPy) is a first-rate library for
numerical programming

-   Widely used in academia, finance and industry.
-   Mature, fast, stable and under continuous development.

We have already seen some code involving NumPy in the preceding
lectures.

In this lecture, we will start a more systematic discussion of both

-   NumPy arrays and
-   the fundamental array processing operations provided by NumPy.

### References

-   [The official NumPy documentation](http://docs.scipy.org/doc/numpy/reference/).

(pandas_array)=

## NumPy Arrays

The essential problem that NumPy solves is fast array processing.

The most important structure that NumPy defines is an array data type
formally called a
[numpy.ndarray](http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html).

NumPy arrays power a large proportion of the scientific Python
ecosystem.

Let\'s first import the library.

```{code-cell} ipython3
import numpy as np
```

To create a NumPy array containing only zeros we use
[np.zeros](http://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html#numpy.zeros)

```{code-cell} ipython3
a = np.zeros(3)
a
```
