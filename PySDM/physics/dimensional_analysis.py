"""
Crated at 2019
"""

from importlib import reload
from PySDM.physics import _flag
from PySDM.physics import constants
from PySDM.physics import formulae
from PySDM.backends.numba import numba_helpers


class DimensionalAnalysis:

    def __enter__(*_):
        _flag.DIMENSIONAL_ANALYSIS = True
        reload(constants)
        reload(numba_helpers)
        reload(formulae)

    def __exit__(*_):
        _flag.DIMENSIONAL_ANALYSIS = False
        reload(constants)
        reload(numba_helpers)
        reload(formulae)
