import sys
import os

# Add the parent path so Python sees the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cradlesync  # Now this should include EchoMemory
