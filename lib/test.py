import numpy as np
import linsys

n = 10
for i in range(100):

    A = np.random.rand(10, 10)
    sol = np.arange(n, dtype=np.float64)

    b = A @ sol

    s = linsys.LinearSystem(A, b)
    s.solve()
    if not np.allclose(sol, s.sol, atol=1e-11):

        print(A, sol)


#mistico. Funziona!