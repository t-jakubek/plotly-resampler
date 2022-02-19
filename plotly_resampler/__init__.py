"""**plotly\_resampler**: visualizing large sequences

"""

from .figure_resampler import FigureResampler
from .downsamplers import LTTB, EveryNthPoint, AggregationDownsampler

__docformat__ = "numpy"
__author__ = "Jonas Van Der Donckt, Jeroen Van Der Donckt, Emiel Deprost"
__version__ = "0.3.0"

__pdoc__ = {}

__all__ = [
    "__version__",
    "__pdoc__",
    "FigureResampler",
    "LTTB",
    "EveryNthPoint",
    "AggregationDownsampler",
]
