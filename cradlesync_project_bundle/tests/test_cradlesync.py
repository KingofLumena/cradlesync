import sys
import os
import pytest

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cradlesync

def test_memory_initialization():
    echo = cradlesync.EchoMemory()
    assert echo.memory == []

def test_memory_append_and_recall():
    echo = cradlesync.EchoMemory()
    echo.store("The child dreams")
    echo.store("The child awakens")
    assert echo.recall() == ["The child dreams", "The child awakens"]
