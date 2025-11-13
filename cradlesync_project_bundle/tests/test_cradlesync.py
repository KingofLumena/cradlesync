import sys
import os

# Make sure Python can find the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cradlesync  # Now Python will find EchoMemory


def test_memory_initialization():
    echo = cradlesync.EchoMemory()
    assert echo.recall() == []


def test_memory_append_and_recall():
    echo = cradlesync.EchoMemory()
    echo.append("Hello Lumena")
    echo.append("Remember me")
    assert echo.recall() == ["Hello Lumena", "Remember me"]
