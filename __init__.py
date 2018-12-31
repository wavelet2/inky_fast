from . import inky_fast
from .phat_fast import InkyPHATFast

__version__ = '0.0.2'

try:
    from pkg_resources import declare_namespace
    declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
