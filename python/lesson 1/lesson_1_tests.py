from lesson_1_answers import sum_list
from test_functions import test_func

sum_list_data = [
    {
    'in_data': [1,2,3,4],
    'target': 10,
    'exp': 'should sum a list of positive integers'
    },
    {
    'in_data': [],
    'target': 0,
    'exp': 'should accept lists with no elements'
    },
    {
    'in_data': [5],
    'target': 5,
    'exp': 'should accept lists with 1 element'
    },
    {
    'in_data': [-5,4,5,-6],
    'target': -2,
    'exp': 'should accept lists with negative elements'
    },
]
