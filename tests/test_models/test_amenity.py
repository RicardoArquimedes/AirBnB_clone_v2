#!/usr/bin/python3
""" Amenity tests """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from os import getenv


class test_Amenity(test_basemodel):
    """ Class tests """

    if getenv("HBNB_TYPE_STORAGE") != "db":
        def __init__(self, *args, **kwargs):
            """ """
            super().__init__(*args, **kwargs)
            self.name = "Amenity"
            self.value = Amenity

        def test_name2(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.name), str)
    else:
        def test_name2(self):
            """ """
            new = Amenity(name="cool")
            self.assertEqual(type(new.name), str)
