#!usr/bin/python3
"""Tets Rectangle class"""


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """This class tests for Rectangle class"""

#Testing height attribute

    #Testing height attribute
    def test_height_int(self):
        """Tests when height is an int"""
        result = Rectangle(10, 50)
        self.assertTrue(result.height, True)

    def test_height_str(self):
        """Tests when height is a string"""
        with self.assertRaises(TypeError):
            Rectangle(10, '20')

    def test_height_float(self):
        """Tests when height is a float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 6.78)

    def test_height_less(self):
        """Test when height is less than 0"""
        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_height_zero(self):
        """Test when height is zero"""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    #Testing width attribute
    def test_width_int(self):
        """Tests when width is an int"""
        result = Rectangle(10, 50)
        self.assertTrue(result.width, True)
    
    def test_width_str(self):
        """Test when width is a string"""
        with self.assertRaises(TypeError):
            Rectangle('10', 50)

    def test_width_float(self):
        """Tests when width is a float"""
        with self.assertRaises(TypeError):
            Rectangle(3.54, 50)

    def test_width_less(self):
        """Test when width is less than zero"""
        with self.assertRaises(ValueError):
            Rectangle(-3, 5)

    def test_width_zero(self):
        """Test when width is zero"""
        with self.assertRaises(ValueError):
            Rectangle(0, 5)


    #testing x atttribute
    def test_x_int(self):
        """Tests when x is an int"""
        result = Rectangle(10, 50, 70)
        self.assertTrue(result.x, True)

    def test_x_str(self):
        """Tests when x is a string"""
        with self.assertRaises(TypeError):
            Rectangle(10, 50, "Ben")

    def test_x_float(self):
        """Tests when x is a float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 50, 4.5)

    def test_x_less(self):
        """Test when x is less than zero"""
        with self.assertRaises(ValueError):
            Rectangle(30, 40, x=-3)

    #Testing y attribute
    def test_y_int(self):
        """Tests when y is an int"""
        result = Rectangle(10, 50, y=20)
        self.assertTrue(result.y, True)

    def test_y_str(self):
        """Tests when y is a string"""
        with self.assertRaises(TypeError):
            Rectangle(10, 50, y='30')

    def test_y_float(self):
        """Tests when y is a float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 50, y=5.76)

    def test_y_less(self):
        """Tests when y is less than zero"""
        with self.assertRaises(ValueError):
            Rectangle(30, 40, y=-3)

#Testing getters and setters
    
    #Testing width getter and setter
    def test_width(self):
        """Tests with getter"""
        result = Rectangle(10, 50)
        self.assertEqual(result.width, 10)

    def test_width_setter(self):
        """Test width setter"""
        result = Rectangle(10, 50)
        result.value = 30
        self.assertEqual(result.value, 30)

    def test_setter_int(self):
        """Test when width is set to an int"""
        result = Rectangle(10, 50)
        result.value = 20
        self.assertTrue(result.value, True)

    def test_setter_str(self):
        """Test when width is set to a string"""
        result = Rectangle(20, 30)
        with self.assertRaises(TypeError):
            result.width = 'Ben'

    def test_setter_float(self):
        """Test when width is set to float"""
        result = Rectangle(10, 50)
        with self.assertRaises(TypeError):
            result.width = 3.997

    #Testing height getter and setter
    def test_height(self):
        """Test height getter"""
        result = Rectangle(10, 50)
        self.assertEqual(result.height, 50)

    def test_height_setter(self):
        """Tests height setter"""
        result = Rectangle(10, 50)
        result.value = 100
        self.assertEqual(result.value, 100)
    
    #Testing height getter and setter
    def test_x(self):
        """Tests x getter"""
        result = Rectangle(10, 50)
        self.assertEqual(result.x, 0)

    def test_x_setter(self):
        """Tests x setter"""
        result = Rectangle(10, 50)
        result.value = 20
        self.assertEqual(result.value, 20)
    
    #Testing height getter and setter
    def test_y(self):
        result = Rectangle(10, 50)
        self.assertEqual(result.y, 0)

    def test_y_setter(self):
        result = Rectangle(10,50)
        result.value = 60
        self.assertEqual(result.value, 60)

#Test Rectangle area function
    def test_area(self):
        result = Rectangle(10, 20)
        self.assertEqual(result.area(), 200)

#Test display function
#    def test_display(self):
#        result = Rectangle(3, 3)
#        expected_output = "###\n###\n###\n"
#        self.assertEqual(result.display(), expected_output)
#
#Test __str__ overriding function
    def test_str_overide(self):
        result = Rectangle(20, 30, x=50, y=60, id=10)
        expected = '[Rectangle] (10) 50/60 - 20/30'
        self.assertEqual(result.__str__(), expected)

    def test_update(self):
        result = Rectangle(30, 40, x=60, y=70, id=10)
        expected = '[Rectangle] (10) 60/70 - 30/40'
        self.assertEqual(result.__str__(), expected)

if __name__ == '__main__':
    unittest.main()
