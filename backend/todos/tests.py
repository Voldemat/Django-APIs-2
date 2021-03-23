# django imports
from django.test import TestCase

# typing
from collections.abc import Sequence

# library to change color in cmd
from termcolor import colored

# models
from .models import Todo

class TodoModelTest(TestCase):
	def setUp(self) -> None:
		# create todo data
		self.data:dict = {
			'title':'Test Title',
			'body':'Test Body',
		}
		self.fake_data:dict = {
			'title':'Test Title',
			'body':'Test Body',
			
		}
		self.todo:Sequence[Todo] = Todo.objects.create(**self.data)
	
	def test_todo_content(self) -> None:
		"""
			Check that all fields in self.data are 
			equall to fields in todo instance
		"""
		dictionary:dict = self.data

		for key in dictionary:
			# check that value of this attr equall to value in data dict
			self.assertEqual(
				# Todo.key == dictionary[key]
				getattr(self.todo, key), dictionary[key],
				# custom error message
				msg = colored(
				f'\n{key.capitalize()}: "{getattr(self.todo,key)}" != "{dictionary[key]}"',
				'red'
				)
			)