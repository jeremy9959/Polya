import numpy as np
from scipy.stats import multinomial

class PolyaUrn:
    """A two-color Polya Urn.
    """

    def __init__(self, a, b, n=50):
        """Create a Polya Urn

        Args:
          a: the number of white balls to start
          b: the number of black balls to start
          n: the number of balls to draw each time
        """
        self._a = a
        self._b = b
        self._n = n
        self._accumulate = np.zeros(n + 1)
        return

    def draw(self):
        """Draw from the urn.

        Returns:
          an (n+1) x 2 numpy array x where (x[i,0],x[i,1]) are the numbers
          of white and black balls in the urn after i draws.

        Updates self._accumulate, a n+1 element array whose ith entry is the number of times
        the urn ended a draw with a+i white balls. 
        """

        x = np.zeros((self._n + 1, 2), dtype=int)
        x[0, :] = np.array([self._a, self._b])
        for i in range(1, self._n + 1):
            p = x[i - 1, :] / x[i - 1, :].sum()
            s = multinomial(1, p=p).rvs(1)
            x[i, :] = x[i - 1, :] + s

        self._accumulate[x[self._n, 0] - self._a] += 1
        y = np.dot(x, np.array([[1, 1], [0, 1]]))
        walk = {"x": y[:, 0], "y": y[:, 1] - self._a - self._b}
        return walk, self._accumulate

    def reset(self):
        """Set the accumulator back to zero."""

        self._accumulate = np.zeros(self._n + 1)
