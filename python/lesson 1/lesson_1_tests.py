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

multiply_array_data = [
  {
    'in_data': [2,2,3,4,5],
    'target': 240,
    'exp': 'accepts normal arrays'
  },
  {
    'in_data': [0,6,9,12],
    'target': 0,
    'exp': 'accepts arrays with zeroes'
  },
  {
    'in_data': [-12, 4, 3, 1, 1],
    'target': -144,
    'exp': 'accepts arrays with negatives'
  },
  {
    'in_data': [2, -2, -2, -2, -2, 0],
    'target': -0,
    'exp': 'accepts arrays with zeroes at end'
  },
  {
    'in_data': [6],
    'target': 6,
    'exp': 'accepts arrays with one element'
  }
]
multiply_odd_add_even_data = [
  {
    'in_data': [2,2,3,4,5],
    'target': 23,
    'exp': 'accepts arrays of positive numbers'
  },
  {
    'in_data': [0,6,9,0,12,0],
    'target': 27,
    'exp': 'accepts arrays with zeroes'
  },
  {
    'in_data': [5],
    'target': 5,
    'exp': 'accepts arrays with one element'
  },
  {
    'in_data': [6,4,2],
    'target': 12,
    'exp': 'accepts arrays with no odd elements'
  },
]

odd_even_test_data = [
  {
    'in_data': [1,2,3,4,5,6],
    'target': [[1,3,5],[2,4,6]],
    'exp': 'accepts arrays of positive integers'
  },
  {
    'in_data': [1],
    'target': [[1],[]],
    'exp': 'accepts arrays of one element'
  },
  {
    'in_data': [2,4],
    'target': [[],[2,4]],
    'exp': 'accepts arrays of only even elements'
  },
  {
    'in_data': [6,6,6,6,6,6],
    'target': [[],[6,6,6,6,6,6]],
    'exp': 'accepts arrays of repeated elements'
  },
  {
    'in_data': [9,2,7,3,1,8,5],
    'target': [[9,7,3,1,5],[2,8]],
    'exp': 'accepts arrays of repeated elements'
  },
]

times_by_index_data = [
  {
    'in_data': [],
    'target': [],
    'exp': 'accepts empty arrays'
  },
  {
    'in_data': [1],
    'target': [0],
    'exp': 'accepts arrays of one element'
  },
  {
    'in_data': [1,2,3,4,5],
    'target': [0,2,6,12,20],
    'exp': 'accepts arrays of consecutive positive integers'
  },
  {
    'in_data': [-8,5,-2,0,4,16,-22],
    'target': [ -0, 5, -4, 0, 16, 80, -132 ],
    'exp': 'accepts arrays of mixed positive and negative integers and 0'
  }
];

fibonacci_data = [
  {
    'in_data': 1,
    'target': 1,
    'exp': 'calculates the 1st fibonacci number'
  },
  {
    'in_data': 5,
    'target': 5,
    'exp': 'calculates the 5th fibonacci number'
  },
  {
    'in_data': 20,
    'target': 6765,
    'exp': 'calculates the 20th fibonacci number'
  }
]

build_string_data = [
  {
    'in_data': '',
    'target': '',
    'exp': 'accepts empty strings'
  },
  {
    'in_data': '2a',
    'target': 'aa',
    'exp': 'accepts strings with two elements'
  },
  {
    'in_data': '1a2b3c4d5c',
    'target': 'abbcccddddccccc',
    'exp': 'accepts longer strings'
  }
];

highest_pair_data = [
  {
    'in_data': [1,3],
    'target': 3,
    'exp': 'accepts arrays of 2 elements'
  },
  {
    'in_data': [5,2,12,19,4,2],
    'target': 228,
    'exp': 'accepts arrays with positive elements'
  },
  {
    'in_data': [-10,-2,-1,-4,-12],
    'target': 48,
    'exp': 'accepts arrays of only negative elements'
  },
  {
    'in_data': [-1,5,-6,2,-4,5,-1,2],
    'target': -2,
    'exp': 'accepts arrays of mixed positive and negative elements'
  }
];

highest_sub_sum_data = [
  {
    'in_data': [5],
    'target': 5,
    'exp': 'accepts arrays of 1 elements'
  },
  {
    'in_data': [5,3,6],
    'target': 14,
    'exp': 'accepts arrays with multiple positive elements'
  },
  {
    'in_data': [5,5,5,5, -10, -20],
    'target': 20,
    'exp': 'accepts arrays with large negative subarrays at end'
  },
  {
    'in_data': [-5,10, -20, 5,5,5],
    'target': 15,
    'exp': 'accepts arrays with negative subarrays at start'
  },
  {
    'in_data': [5,5,5,5, -10, 100, 100],
    'target': 210,
    'exp': 'works for arrays with small negative subarrays in middle'
  },
  {
    'in_data': [5,5,5,5, -500, -50, 100, 100],
    'target': 200,
    'exp': 'works for arrays with large negative subarrays in middle'
  },
];
