# test_evmgrid.py
"""
Tests for EvmGrid module.
"""

import unittest
from evmgrid import EvmGrid

class TestEvmGrid(unittest.TestCase):
    """Test cases for EvmGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EvmGrid()
        self.assertIsInstance(instance, EvmGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EvmGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
