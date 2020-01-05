from typing import Tuple

import jax.numpy as np

from objects import Thing, Plane, Sphere

class Camera:
    def __init__(
        self,
        pinhole: np.ndarray,
        sensor: np.ndarray,
        left: np.ndarray,
        resolution: Tuple[int, int],
    ):
        self.pinhole = pinhole
        self.sensor = sensor
        self.left = left / np.linalg.norm(right)
        up = np.cross(sensor - pinhole, right)
        self.up = up / np.linalg.norm(up)


class Ray:
    def __init__(
        self,
        position: np.ndarray,
        direction: np.ndarray
    ):
        assert np.linalg.norm(direction) == 0

        self.position = position
        self.direction = direction

    def march(distance: float):
        self.positon += distance * self.direction
        
    


def main():
    world = [
        Sphere(np.array([0, 0, 3]), 1)
    ]

    camera = Camera(
            np.array([0, 0, 0]),
            np.array([0, 0, 1]),
            np.array([1, 0, 0]),
            (64, 64),
            )




if __name__ == "__main__":
    main()
