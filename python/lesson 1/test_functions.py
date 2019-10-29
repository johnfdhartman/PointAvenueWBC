class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test_func (func, test_data):
    num_args = func.__code__.co_argcount

    print('testing ' + func.__name__)
    for test in test_data:
        if num_args == 1:
            result = func(['in_data'])
        elif num_args > 1:
            result = func(*['in_data'])
        if result == test['target']:
            print (bcolors.OKBLUE + 'passed: ' + test['exp']+ bcolors.ENDC)
        else:
            print (bcolors.FAIL + 'failed: ' + test['exp']+ bcolors.ENDC)
