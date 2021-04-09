from typing import Any

import numpy as np


class DiscreteSpace:
    def __init__(self, n: int):
        assert n > 0, "Argument must be a positive integer"
        self.n = n

    def sample(self) -> int:
        return np.random.randint(self.n)

    def __contains__(self, item: Any) -> bool:
        if isinstance(item, int):
            return 0 <= item < self.n
        else:
            return False

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, DiscreteSpace) and self.n == other.n

    def __repr__(self) -> str:
        return f"Discrete({self.n})"
