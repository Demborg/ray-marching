from typing import Tuple, List

import jax.numpy as np
import matplotlib.pyplot as plt
import numpy as onp

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
        self.left = left / np.linalg.norm(left)
        up = np.cross(sensor - pinhole, left)
        self.up = up / np.linalg.norm(up)
        self.resolution = resolution

    def image(self, world: List[Thing]):
        image = onp.zeros(self.resolution)
        for i, x in enumerate(np.linspace(-1, 1, self.resolution[0])):
            for j, y in enumerate(np.linspace(-1, 1, self.resolution[1])):
                direction = self.sensor + x * self.left + y * self.up - self.pinhole
                direction /= np.linalg.norm(direction)
                ray = Ray(
                    self.pinhole,
                    direction,
                )      

                for i in range(10):
                    distance_to_world = min(thing.distance(ray.position) for thing in world)
                    ray.march(distance_to_world)
                
                image[i, j] = distance_to_world < 0.01
        return image
                


class Ray:
    def __init__(
        self,
        position: np.ndarray,
        direction: np.ndarray
    ):
        assert np.abs(np.linalg.norm(direction) - 1) < 0.01

        self.position = position
        self.direction = direction

    def march(self, distance: float):
        self.position += distance * self.direction
        
    
def main():
    world = [
        Sphere(np.array([0, 0, 3]), 1),
        #Plane(np.array([0, -1, 0]), np.array([0, 1, 0]))
    ]

    camera = Camera(
            np.array([0, 0, 0]),
            np.array([0, 0, 1]),
            np.array([1, 0, 0]),
            (32, 32),
            )

    plt.imshow(camera.image(world))
    plt.show()

if __name__ == "__main__":
    main()
