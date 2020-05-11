"""
Define the plugin class - unless you want to customize the behavior, you only really need to declare the class. The
rest of the information will be picked up from ``default.config``, ``schemas.yml`` and ``scripts.yml`` by default.
"""

from __future__ import print_function
from __future__ import division

import cea.plugin

__author__ = "Daren Thomas"
__copyright__ = "Copyright 2020, Architecture and Building Systems - ETH Zurich"
__credits__ = ["Daren Thomas"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Daren Thomas"
__email__ = "cea@arch.ethz.ch"
__status__ = "Production"


class DemandSummaryPlugin(cea.plugin.CeaPlugin):
    pass