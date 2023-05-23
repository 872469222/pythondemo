# 被测方法
import unittest


class Search:
    def search_fun(self):
        print("search")
        return True


class TestSearch(unittest.TestCase):
    # setup 和tearDown 方法是在每条测试用例前后分别调用的方法
    # setUpClass和tearDownClass  是在整个类的前后分别调用的方法
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("setup class ")
    #     cls.search = Search()
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("teardown class")
    def setUp(self) -> None:
        print("TestSearch1   >>>>>>>>>    setup")
        self.search = Search()

    def tearDown(self) -> None:
        print("TestSearch1    >>>>>>>>> tearDownClass")

    def test_search1(self):
        # 实例化类
        print("testsearch1")
        #  search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        # 实例化类
        print("testsearch2")
        #  search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        # 实例化类
        print("testsearch3")
        #   search = Search()
        assert True == self.search.search_fun()


class TestSearch1(unittest.TestCase):
    # setup 和tearDown 方法是在每条测试用例前后分别调用的方法
    # setUpClass和tearDownClass  是在整个类的前后分别调用的方法
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("setup class ")
    #     cls.search = Search()
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("teardown class")
    def setUp(self) -> None:
        print("TestSearch1 -----------setup _  方法级别")
        self.search = Search()

    def tearDown(self) -> None:
        print("TestSearch1 -----------tearDown _  方法级别")

    def test_search1(self):
        # 实例化类
        print("testsearch1")
        #  search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        # 实例化类
        print("testsearch2")
        #  search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        # 实例化类
        print("testsearch3")
        #   search = Search()
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1, 2, "判断 1 ==2 ")

    # def test_notequal(self):
    #     print("断言不相等")
    #     self.assertNotEqual(1, 2, "判断1！=2")
    #     self.assertTrue(1 == 2, "verift")


class TestSearch2(unittest.TestCase):
    def test_case1(self):
        print("testcase1")


if __name__ == '__main__':
    # 方法一:执行当前文件所有的unittest测试用例，全部执行
    # unittest.main
    # 方法二：执行指定的测试用例，将要执行的测试用例添加到测试套件里面,批量执行测试方法
    # 执行指定的测试用例
    # 创建一个测试套件，TestSuite
    suite = unittest.TestSuite()
    suite.addTest(TestSearch("test_search1"))
    suite.addTest(TestSearch("test_search3"))
    unittest.TextTestRunner().run(suite)

    # 方法三：执行某个测试类,将测试类添加到测试套件里面，批量执行测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)