"""
Python unit-test
"""

import unittest

import numpy as np
import numpy.testing as npt

from .. import givens_rotation


class TestGivensRotation(unittest.TestCase):
    """Test case for module givens_rotation."""

    def test_wikipedia_example1(self):
        """Test of Wikipedia example

        The example for the following QR decomposition is taken from
        https://en.wikipedia.org/wiki/Givens_rotation#Triangularization.
        """

        A = np.array([[6, 5, 0],
                      [5, 1, 4],
                      [0, 4, 3]])

        (Q, R) = givens_rotation.qr_decomposition(A)

        Q_desired = np.array([[0.7682, 0.3327, 0.5470],
                              [0.6402, -0.3992, -0.6564],
                              [0, 0.8544, -0.5196]])
        R_desired = np.array([[7.8102, 4.4813, 2.5607],
                              [0, 4.6817, 0.9664],
                              [0, 0, -4.1843]])

        npt.assert_almost_equal(Q, Q_desired, 4)
        npt.assert_almost_equal(R, R_desired, 4)

    def test_wikipedia_example2(self):
        """Test of Wikipedia example

        The example for the following QR decomposition is taken from
        http://de.wikipedia.org/wiki/Givens-Rotation.
        """

        A = np.array([[3, 5],
                      [0, 2],
                      [0, 0],
                      [4, 5]])

        (Q, R) = givens_rotation.qr_decomposition(A)

        Q_desired = np.array([[0.6, 0.3577, 0, -0.7155],
                              [0, 0.8944, 0, 0.4472],
                              [0, 0, 1, 0],
                              [0.8, -0.2683, 0, 0.5366]])
        R_desired = np.array([[5, 7],
                              [0, 2.2360],
                              [0, 0],
                              [0, 0]])

        npt.assert_almost_equal(Q, Q_desired, 4)
        npt.assert_almost_equal(R, R_desired, 4)


if __name__ == "__main__":
    unittest.main()
