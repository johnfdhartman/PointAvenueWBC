def test_func (func, test_data):
    print('testing ' + func.__name__)
    for test in test_data:
        if func(test['in_data']) == test['target']:
            print ('passed: ' + test['exp'])
