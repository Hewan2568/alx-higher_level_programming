

   

#!/usr/bin/python3



import unittest

import json

from models.rectangle import Rectangle

from models.base import Base

from models.square import Square

import pep8

import sys

import os

from io import StringIO





class TestBase(unittest.TestCase):

    

        def checking(self):

                    self.assertIsNotNone(Base.__doc__)

                            self.assertIsNotNone(save_to_file.__doc__)

                                    self.assertIsNotNone(from_json_string.__doc__)

                                            self.assertIsNotNone(create.__doc__)

                                                    self.assertIsNotNone(load_from_file.__doc__)

                                                    

                                                        def test_style_base(self):

                                                                    """

                                                                            Tests for pep8

                                                                            """

                                                                            style = pep8.StyleGuide(quiet=True)

                                                                                    p = style.check_files(['tests/test_models/test_base.py'])

                                                                                            self.assertEqual(p.total_errors, 0, "fix pep8")

                                                                                                    p = style.check_files(['models/base.py'])

                                                                                                            self.assertEqual(p.total_errors, 0, "fix pep8")

                                                                                                            

                                                                                                                def test_00_documentation(self):

                                                                                                                            """

                                                                                                                                    Test to see if documentation is

                                                                                                                                    created and correct

                                                                                                                                    """

                                                                                                                                    self.assertTrue(hasattr(Base, "__init__"))

                                                                                                                                            self.assertTrue(hasattr(Base, "create"))

                                                                                                                                                    self.assertTrue(hasattr(Base, "to_json_string"))

                                                                                                                                                            self.assertTrue(hasattr(Base, "from_json_string"))

                                                                                                                                                                    self.assertTrue(hasattr(Base, "save_to_file"))

                                                                                                                                                                            self.assertTrue(hasattr(Base, "load_from_file"))

                                                                                                                                                                            

                                                                                                                                                                                @classmethod

                                                                                                                                                                                    def setUpClass(cls):

                                                                                                                                                                                                Base._Base__nb_objects == 0

                                                                                                                                                                                                        cls.r1 = Rectangle(3, 5, 1, id=9)

                                                                                                                                                                                                                cls.r3 = Rectangle(2, 4, id=11)

                                                                                                                                                                                                                        cls.s1 = Square(5, id=99)

                                                                                                                                                                                                                                cls.s2 = Square(7, 9, 1, id=78)

                                                                                                                                                                                                                                
