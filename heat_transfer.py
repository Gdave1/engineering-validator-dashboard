def heat_conduction(k, A, T1, T2, L):
    """
    Calculates heat transfer using Fourier's Law
    Q = kA(T1 - T2) / L
    """
    if L <= 0:
        raise ValueError("Thickness must be greater than zero")

    Q = k * A * (T1 - T2) / L
    return Q