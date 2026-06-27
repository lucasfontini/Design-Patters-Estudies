from abc import ABC, abstractmethod

"""
StrategyFactory.create("cisco")
           │
           ▼
StrategyRegistry.get("cisco")
           │
           ▼
Retorna a classe CiscoStrategy
           │
           ▼
CiscoStrategy()
           │
           ▼
Objeto criado
           │
           ▼
configure("show ip int br")
"""

class ConfigStrategy(ABC):
    @abstractmethod
    def configure(self, command):
        pass

class StrategyRegistry:

    _strategies = {}

    @classmethod
    def register(cls, name):

        def decorator(strategy):
            cls._strategies[name] = strategy

            return strategy

        return decorator

    @classmethod
    def get(cls, name):
        strategy = cls._strategies.get(name)
        if strategy is None:
            raise ValueError(f"Vendor '{name}' not supported.")
        return strategy

@StrategyRegistry.register("cisco")
class CiscoStrategy(ConfigStrategy):
    def configure(self, command):
        print("configura equipamento cisco", command)

@StrategyRegistry.register("mikrotik")
class MikrotikStrategy(ConfigStrategy):
    def configure(self , command):
        print("configura equipamento mikrotik", command)

@StrategyRegistry.register("junos")
class JuniperStrategy(ConfigStrategy):
    def configure(self, command):
        print("configurao equipamento juniper")

class StrategyFactory:

    @staticmethod
    def create(vendor):
        strategy_class = StrategyRegistry.get(vendor)
        return strategy_class()

strategy = StrategyFactory.create("arista")
strategy.configure("show ip int br")


