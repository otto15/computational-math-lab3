from data.functions import functions_primordial

eps = 1e-10


def is_death_dot(f, a):
    try:
        f(a)
        return False
    except Exception:
        return True


def check_convergence(f, a):
    try:
        functions_primordial[f](a + eps)
    except Exception:
        raise ValueError("Integral does not converge")


def find_death_dot_intervals(f, a, b) -> list[tuple[float, float]]:
    intervals: list[tuple[float, float]] = []
    step = (b - a) / 1000
    left = a
    if is_death_dot(f, a):
        check_convergence(f, a)
        left = a + eps
    while a < b:
        a += step
        if is_death_dot(f, a):
            check_convergence(f, a)
            intervals.append((left, a - eps))
            left = a + eps
    if is_death_dot(f, b):
        check_convergence(f, b)
        intervals.append((left, b - eps))
    else:
        intervals.append((left, b))
    return intervals
