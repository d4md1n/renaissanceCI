import abc


class ChainLink(metaclass=abc.ABCMeta):
    def __init__(self, successor=None):
        self._successor = successor


class PipelineChainLink(ChainLink, metaclass=abc.ABCMeta):
    data = {}

    @abc.abstractmethod
    def before_process(self):
        pass

    @abc.abstractmethod
    def process(self):
        pass

    @abc.abstractmethod
    def after_process(self):
        pass

    def complete(self):
        if self._successor is not None:
            self._successor.data = self.data
            self._successor.run()

    def run(self):
        self.before_process()
        self.process()
        self.after_process()
        self.complete()
