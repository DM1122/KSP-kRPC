# external
import numpy as np
import pytest


class ConstantMassModel:
    def __init__(self, x_0, m, b, g):
        self.x_0 = x_0
        self.x = x_0
        self.m = m
        self.b = b
        self.g = g

    def plant(self, u, dt):
        # alloc
        dx = np.zeros((len(self.x), 1))

        # process
        dx[0] = self.x[1]
        dx[1] = -self.b / self.m * self.x[1] - self.g + 1 / self.m * u

        # update
        self.x = self.x + dx * dt

        return self.x

    def reset(self):
        self.x = self.x_0

    def __call__(self, u, dt):

        x = self.plant(u, dt)

        return x
