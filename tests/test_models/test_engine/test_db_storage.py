#!/usr/bin/python3
""" Module for testing DBstorage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from models.state import State


class test_dbstorage(unittest.TestCase):
    """ Class to test the DBstorage method """

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Cannot storage if db is active")
    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage.all(self).keys():
            del_list.append(key)
        for key in del_list:
            storage._DBStorage__session.delete(storage.all(self)[key])
            storage._DBStorage__session.commit()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.db_storage import DBStorage
        self.assertEqual(type(storage), DBStorage)
