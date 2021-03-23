import unittest
from termcolor import colored
class Todo:
    def __init__(self,title:str = 'Empty', body:str = 'Empty', id:int = 1, **kwargs:dict) -> None:
        self.title = title + '11'
        self.body = body
        self.id = id

    def __str__(self) -> str:
        return self.title

class TodoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {
            'title':'title',
            'body':'body',
            'id':1,
            # 'akey':'avalue',
        }
        self.todo = Todo(**self.data)

    def test_content(self):
        """
            Check that all fields in self.data are 
            equall to fields in todo instance
        """
        for key in self.data:
            # check that todo have current attribute with name = key
            self.assertTrue(hasattr(self.todo, key), msg = colored(f'\nTodo don`t have attribute "{key}"', 'red'))
            # check that value of this attr equall to value in data dict
            self.assertEqual(
                getattr(self.todo, key), self.data[key],
                msg = colored(
                f'\n{key.capitalize()}: "{getattr(self.todo,key)}" != "{self.data[key]}"',
                'red'
                )
            )


if __name__ == '__main__':
    unittest.main()

