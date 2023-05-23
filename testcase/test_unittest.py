import unittest


class TestStringMethods(unittest.TestCase):
    #  每一条测试用例的前后，分别执行了setup teardown操作
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    # cls 是类级别的方法，需要加上装饰器classmethod
    # setup 和tearDown 方法是在每条测试用例前后分别调用的方法
    # setUpClass和tearDownClass  是在整个类的前后分别调用的方法
    @classmethod
    def setUpClass(cls) -> None:
        print("set Up Class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown  class")

    def test_abc(self):
        print("test abc")

    def test_upper(self):
        print("test_upper  11 1")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper  222")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split  3333")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
