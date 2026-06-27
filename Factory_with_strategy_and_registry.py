from abc import ABC, abstractmethod


class ConfigStrategy(ABC):
    @abstractmethod
    def configure(self, command):
        pass


class CiscoStrategy(ConfigStrategy):
    def configure(self, command):
        print("configura equipamento cisco", command)

class MikrotikStrategy(ConfigStrategy):
    def configure(self , command):
        print("configura equipamento mikrotik", command)

class JuniperStrategy:
    def configure(self, command):
        print("configurao equipamento juniper")



class StrategyRegistry:
    _strategies = {}

    @classmethod
    def register(cls, name, strategy):
        cls._strategies[name] = strategy

    @classmethod
    def get(cls, name):
        return cls._strategies[name]


#registry strategies

StrategyRegistry.register("cisco", CiscoStrategy)
StrategyRegistry.register("mikrotik", MikrotikStrategy)
StrategyRegistry.register("juniper", JuniperStrategy)


#with registry 

class StrategyFactory:

    """
    factory using if not registry
    """
    @staticmethod
    def create(vendor):
        strategy = StrategyRegistry.get(vendor)


StrategyRegistry.register("cisco", CiscoStrategy)
StrategyRegistry.register("mikrotik", MikrotikStrategy)

strategy = StrategyFactory.create("cisco")
strategy.configure()

