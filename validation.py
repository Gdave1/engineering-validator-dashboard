def validate_input(k, A, L):
    errors = []

    if k <= 0:
        errors.append("Thermal conductivity must be positive")

    if A <= 0:
        errors.append("Area must be positive")

    if L <= 0:
        errors.append("Thickness must be positive")

    return errors


def validate_result(Q):
    warnings = []

    if abs(Q) > 1e6:
        warnings.append("Heat transfer unusually high")

    if Q == 0:
        warnings.append("No heat transfer detected")

    return warnings

def validate_physics(T1, T2):
    warnings = []

    if T1 == T2:
        warnings.append("No temperatre difference → No heat transfer expected")

    if T1 < T2:
        warnings.append("Heat flow direction reversed (check inputs)")

    return warnings
