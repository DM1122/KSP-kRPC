from main import models
import numpy as np


def test_model():
    # model instantiation
    model = models.ConstantMassModel(x_0=np.array([[1], [1]]), m=1, b=0.01, g=9.81)