try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata  # python<=3.7

from .cli import cli


__version__ = metadata.version("pbsreport")
