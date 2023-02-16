import pytest

try:
    import networkx as nx
except ImportError:
    raise "Module networkx not imported" 

# Do modules load?
try:
    from nx import nxNode, AdjView, NodeView, EdgeView, DegreeView, NodeDataView, EdgeDataView, DegreeView, DataView, id
except ImportError:
    raise "Module nxNode not imported" 

try:
    from sim import Sim
except ImportError:
    raise "Module Sim not imported" 

try:
    from params import make_params
    params = make_params()
except ImportError:
    raise "Params not imported" 

# What dependencies are installed?

try:
    import time
except ImportError:
    has_time = False

try:
    import numpy

    has_numpy = True
except ImportError:
    has_numpy = False

try:
    import scipy

    has_scipy = True
except ImportError:
    has_scipy = False

try:
    import pandas

    has_pandas = True
except ImportError:
    has_pandas = False

try:
    import dash
except ImportError:
    has_dash = False

try:
    import seaborn
except ImportError:
    has_seaborn = False

try:
    import sympy

    has_sympy = True
except ImportError:
    has_sympy = False



