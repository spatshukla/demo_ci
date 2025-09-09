#!/usr/bin/env python3
"""
Test runner for demo_ci.geo2d and demo_ci.geo3d modules.
Run this script to execute all unit tests.
"""

import unittest
import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import test modules
from tests.test_geo2d import TestRectangle, TestTriangle
from tests.test_geo3d import TestCuboid, TestPyramid, TestSphere, TestCylinder


def create_test_suite():
    """Create a test suite with all test cases"""
    suite = unittest.TestSuite()
    
    # Add geo2d tests
    suite.addTest(unittest.makeSuite(TestRectangle))
    suite.addTest(unittest.makeSuite(TestTriangle))
    
    # Add geo3d tests
    suite.addTest(unittest.makeSuite(TestCuboid))
    suite.addTest(unittest.makeSuite(TestPyramid))
    suite.addTest(unittest.makeSuite(TestSphere))
    suite.addTest(unittest.makeSuite(TestCylinder))
    
    return suite


def run_tests():
    """Run all tests and return the result"""
    suite = create_test_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result


if __name__ == '__main__':
    print("Running unit tests for demo_ci.geo2d and demo_ci.geo3d modules...")
    print("=" * 70)
    
    result = run_tests()
    
    print("\n" + "=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}")
            print(f"  {traceback.strip()}\n")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}")
            print(f"  {traceback.strip()}\n")
    
    if result.wasSuccessful():
        print("\nAll tests passed! ✅")
        sys.exit(0)
    else:
        print("\nSome tests failed! ❌")
        sys.exit(1)