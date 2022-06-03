import unittest
from sort import bubble_sort

class SortTestCase(unittest.TestCase):

  def test_Normal_Sort(self):
    """Test Case Normal Sort. Should work"""
    assert bubble_sort([3, 2, 1]) == [1,2, 3], "bubble sort does not his job correctly"

  def test_Sort_A_Max_Val_Array(self):
    """Test Case Sort A Max Val Array. Should work"""
    assert bubble_sort([1,2,3,4,5]) == [1,2,3,4,5], "bubble sort does not his job correctly"

  def test_Array_Too_Long(self):
    """Test Case Array Too Long. Shouldn't work"""
    assert bubble_sort([6,5,4,3,2,1]) == None, "bubble sort does not his job correctly"

  def test_Empty_Array(self):
    """Test Case Empty Array. Should work"""
    assert bubble_sort([]) == [], "bubble sort does not his job correctly"
  
  def test_Array_With_Non_Numeric_Elements(self):
    """Test Case Array With Non Numeric Elements. Should work"""
    assert bubble_sort(['a', 'c', 'b']) == ['a', 'b', 'c'], "bubble sort does not his job correctly"
  
  def test_Array_With_Numeric_Elements_And_Non_Numeric_Elements(self):
    """Test Case Array With Numeric Elements And Non Numeric Elements. Must raise error"""
    with self.assertRaises(TypeError):
      bubble_sort(['a', 'b', 'c', 1, 2])
    
  

if __name__ == '__main__':
  unittest.main()