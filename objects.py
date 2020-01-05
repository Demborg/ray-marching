from abc import ABC, abstractmethod

import jax.numpy as np

class Thing(ABC):
   @abstractmethod
   def distance(self, point: np.ndarray) -> float:
        pass

class Sphere(Thing):
    def __init__(self, center: np.ndarray, radius: float):
        self.center = center
        self.radius = radius

    def distance(self, point: np.ndarray) -> float:
        return np.linalg.norm(self.center - point) - self.radius


class Plane(Thing):
    def __init__(self, center: np.ndarray, normal: np.ndarray):
        assert np.linalg.norm(normal) == 1

        self.center = center
        self.normal = normal

    def distance(self, point: np.ndarray) -> float:
        return (self.center - point).dot(self.normal)
