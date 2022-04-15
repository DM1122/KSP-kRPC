# stdlib
import warnings

# external
import sympy as sy


def solve_eq(eq, symbol):
    soln = sy.solveset(f=eq, symbol=symbol)
    print(sy.latex(soln))
    if len(soln.args) == 0:
        raise ValueError(f"No solutions exists:\n{soln}")
    elif len(soln.args) > 1:
        warnings.warn(f"More than one solution exists:\n{soln}")
    else:
        soln = soln.args[0]

    return sy.Eq(symbol, soln)
