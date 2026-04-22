import numpy as np

class LinearSystem:
    "PRUZ"
    def __init__(self, A : np.ndarray, b : np.ndarray):
        #A is a n by n matrix, b is a vector in R^n

        self.A = np.array(A, dtype=np.float64)
        self.b = np.array(b, dtype=np.float64)

        if A.shape[0] != A.shape[1]:
            
            raise ValueError("The system matrix must be square")

        if A.shape[0] != b.shape[0]:

            raise ValueError("The right side vector must have dimension compatible with the matrix")

        self.n = A.shape[0]

    def gaussMethod(self):

        R = self.A.copy()
        c = self.b.copy()

        for i in range(self.n - 1):

            # checks whether there is at least one non-zero entry
            if np.allclose(R[i+1:, i], 0, atol=1e-12):
    
                continue

            #partial pivoting
            pivotIndex = np.argmax(np.abs(R[i:, i])) + i #it is relative to i
            if pivotIndex != i: 

                R[[i, pivotIndex]] = R[[pivotIndex, i]] #swap
                c[[i, pivotIndex]] = c[[pivotIndex, i]]


            #this is a broadcasting approach equivalent to np.outer
            # R[i+1:, i:] -= (R[i, i:] / R[i, i])[np.newaxis, :] * R[i+1:, i][:, np.newaxis]
            
            l = R[i+1:, i] / R[i, i] #multipliers
            R[i+1:, i:] -= np.outer(l, R[i, i:])

            c[i+1:] -= l * c[i]

        self.R = R
        self.c = c

    def solveUpperTriangular(self):

        sol = np.zeros(self.n)
        for i in range(self.n - 1, -1, -1):
            
            #back subsitution
            sol[i] = (self.c[i] - np.dot(self.R[i, i+1:], sol[i+1:])) / self.R[i, i]

        self.sol = sol

    def solve(self):

        self.gaussMethod()
        self.solveUpperTriangular()


if __name__ == "__main__":

    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 11]])
    b = np.array([1, 2, 3])
    s = LinearSystem(A, b)
    s.gaussMethod()

    print(s.R)
    print(s.c)



