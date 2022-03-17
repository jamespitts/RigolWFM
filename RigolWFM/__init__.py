"""
A utility to process Rigol oscilloscope wfm files.

For full documentation see <https://RigolWFM.readthedocs.io>

    Example:
    >>> import matplotlib.pyplot as plt
    >>> import RigolWFM.wfm as rigol

    >>> filename = 'example.wfm'
    >>> scope = 'DS1000E'

    >>> w = rigol.Wfm.from_file(filename, scope)
    >>> w.plot()
    >>> plt.show()

Info waveform class::

    help(rigol.wfm)

Info about channel class::

    help(rigol.channel)

All the parsing code is auto-generated by `kaitai-struct-compiler`
based on `.ksy` files that describe the binary format of the Rigol
oscilloscope `.wfm` files.
"""
__version__ = '0.9.4'
__author__ = 'Scott Prahl'
__email__ = 'scott.prahl@oit.edu'
__copyright__ = 'Copyright 2020-22, Scott Prahl'
__license__ = 'BSD 3-clause'
__url__ = 'https://github.com/scottprahl/RigolWFM.git'
