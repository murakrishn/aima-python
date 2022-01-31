from ast import Import
from inspect import getsource
import ipywidgets as widgets
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from IPython.display import HTML
from IPython.display import display
from PIL import Image
from matplotlib import lines


# ----------------------------------------------------------------------
# Magic words

def psource(*functions):
    """Print the pseudocode for the given algorithms"""
    source_code = '\n\n'.join(getsource(fn) for fn in functions)
    # print(source_code)
    try:
        from pygments.formatters import HtmlFormatter
        from pygments.lexers import PythonLexer
        from pygments import highlight
        display(HTML(highlight(source_code, PythonLexer(), HtmlFormatter(full=True))))
    except ImportError:
        print(source_code)