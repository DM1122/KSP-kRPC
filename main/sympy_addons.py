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


def L(f):
    t, s = sy.symbols("t, s")
    return sy.laplace_transform(f, t, s, noconds=True)


def L_inv(F):
    t, s = sy.Symbol("t, s")
    return sy.inverse_laplace_transform(F, s, t)
