from renaissance_ci.core.chain import PipelineChainLink

import unittest


class HelloPrinter(PipelineChainLink):
    value = None

    def before_process(self):
        print("hello before")

    def process(self):
        if self.value is None:
            value = 0
        else:
            value = self.value
        print("hello world {}".format(value))

    def after_process(self):
        print("hello after")

    def set_value(self, value):
        self.value = value


class TestPipelineChainLink(unittest.TestCase):

    def test_that_HelloPrinter_chain_has_successors(self):
        hello = HelloPrinter()
        hello2 = HelloPrinter(hello)

        self.assertTrue(hello2._successor is not None)

    def test_that_HelloPrinters_chain_has_the_correct_values(self):
        hello = HelloPrinter()
        hello.set_value(5)
        hello2 = HelloPrinter(hello)
        self.assertTrue(hello2.value is None)
        self.assertEqual(hello2._successor.value, 5)


if __name__ == "__main__":
    unittest.main()
