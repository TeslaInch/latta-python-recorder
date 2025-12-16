from .latta import Latta

# Expose Latta directly for easy import
__all__ = ["Latta"]

# Alias for official docs compatibility
import sys
sys.modules['latta'] = sys.modules[__name__]
