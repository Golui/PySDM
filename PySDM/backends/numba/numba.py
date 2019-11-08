"""
Created at 24.07.2019

@author: Piotr Bartman
@author: Sylwester Arabas
"""

from PySDM.backends.numba.storage_methods import StorageMethods
from PySDM.backends.numba.maths_methods import MathsMethods
from PySDM.backends.numba.physics_methods import PhysicsMethods
from PySDM.backends.numba.special_methods import SpecialMethods


class Numba(StorageMethods, MathsMethods, PhysicsMethods, SpecialMethods):
    pass