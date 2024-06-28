# settings/__init__.py
from .local import *
try:
    from .local import *
except ImportError:
    pass
