import datetime


class TestClass:
    def __init__(self, test_name, test_date):
        self.test_name = test_name
        self.test_date = test_date

    def return_class_info(self):
        test_info = (self.test_name, self.test_date)
        return test_info

    def addem(self, aa, bb):
        total = sum(aa, bb)
        return total


def test_func():
    arr = [i for i in range(10)]
    print(f'arr: {arr}')
    return arr


# Create test_class method outside the class that creates an instance of the TestClass,
# and calls the addem method passing two numbers.
def test_class(c, d):
    tn = "test2"
    td = datetime.datetime.now()
    first_test_inst2 = TestClass(tn, td)
    result = first_test_inst2.addem(c, d)
    return result


def main():
    # First example (no class)
    test_func()
    # Second example (using class)
    tn = "selamTest"
    td = datetime.datetime.now()
    first_test_inst1 = TestClass(tn, td)
    cl_inf = first_test_inst1.return_class_info()
    print(f'cl_inf: {cl_inf}')

    res2 = test_class(33, 66)
    print(f'Result: {res2}')


if __name__ == '__main__':
    main()
