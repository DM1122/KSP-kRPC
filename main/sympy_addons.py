"""Some methods to add additional functionality to sympy."""
# stdlib
import warnings

# external
import sympy as sy


def solve_eq(eq: sy.Equality, symbol: sy.Symbol) -> sy.Equality:
    """Solve an equality with respect to a symbol.

    Args:
        eq: The equation to solve.
        symbol: The symbol to solve for.

    Raises:
        ValueError: No solutions can be found.

    Returns:
        The solved equation.

    """
    soln = sy.solveset(f=eq, symbol=symbol)

    if len(soln.args) == 0:
        raise ValueError(f"No solutions exists:\n{soln}")

    if len(soln.args) > 1:
        warnings.warn(f"More than one solution exists:\n{soln}")
    else:
        soln = soln.args[0]

    return sy.Eq(symbol, soln)
