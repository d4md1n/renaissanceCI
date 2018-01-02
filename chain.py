import abc

class ChainLink(metaclass=abc.ABCMeta) :

    def __init__(self, successor=None):
        self._successor = successor

class PipelineChainLink(ChainLink, metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def before_process(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def process(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def after_process(self, *args, **kwargs):
        pass

    def complete(self):
        if self._successor is not None:
            self._successor.run()

    def run(self):
        self.before_process()
        self.process()
        self.after_process()
        self.complete()
    
    
class HelloPrinter(PipelineChainLink):
    
    def before_process(self):
        pass

    def process(self, value=1):
        print("hello world")

    def after_process(self):
        pass

def main():
    hello = HelloPrinter()
    HelloPrinter(hello).run()

if __name__ == "__main__":
    main()
