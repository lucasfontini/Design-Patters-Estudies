# Design Patterns: Strategy, Factory e Registry

## Objetivo

Este documento explica como utilizar os padrões **Strategy**, **Factory** e **Registry** em projetos Python, especialmente em automação de redes.

---

# Visão Geral

Os três padrões trabalham juntos para deixar o código mais organizado, extensível e desacoplado.

```text
                Vendor
                  │
                  ▼
          StrategyFactory
                  │
                  ▼
          StrategyRegistry
                  │
      ┌───────────┼────────────┐
      ▼           ▼            ▼
 CiscoStrategy MikrotikStrategy JuniperStrategy
      │           │            │
      ▼           ▼            ▼
 configure() configure() configure()
```

---

# Strategy

## O que é?

O Strategy encapsula um comportamento em uma classe.

Em vez de vários `if/elif`, cada comportamento possui sua própria implementação.

## Problema

```python
if vendor == "cisco":
    ...
elif vendor == "mikrotik":
    ...
elif vendor == "juniper":
    ...
```

À medida que novos fabricantes são adicionados, esse código cresce e fica difícil de manter.

## Solução

Criamos uma interface comum.

```python
from abc import ABC, abstractmethod

class ConfigStrategy(ABC):

    @abstractmethod
    def configure(self, command):
        pass
```

Cada fabricante implementa sua própria estratégia.

```python
class CiscoStrategy(ConfigStrategy):

    def configure(self, command):
        print(command)
```

---

# Registry

## O que é?

O Registry mantém um catálogo das estratégias disponíveis.

Em vez da Factory conhecer todas as classes, ela consulta o Registry.

```python
class StrategyRegistry:

    _strategies = {}
```

## Registro automático

```python
@StrategyRegistry.register("cisco")
class CiscoStrategy(ConfigStrategy):
    ...
```

Ao importar o módulo, a classe é registrada automaticamente.

O dicionário passa a conter:

```python
{
    "cisco": CiscoStrategy,
    "mikrotik": MikrotikStrategy,
    "junos": JuniperStrategy
}
```

---

# Factory

## O que é?

A Factory é responsável por criar o objeto correto.

Quem utiliza a Factory não conhece nenhuma implementação concreta.

```python
strategy = StrategyFactory.create("cisco")
```

Internamente:

```python
strategy_class = StrategyRegistry.get("cisco")

return strategy_class()
```

---

# Fluxo Completo

Quando executamos:

```python
strategy = StrategyFactory.create("cisco")
strategy.configure("show ip int br")
```

A sequência é:

```text
StrategyFactory.create("cisco")
           │
           ▼
StrategyRegistry.get("cisco")
           │
           ▼
Retorna CiscoStrategy
           │
           ▼
Instancia CiscoStrategy()
           │
           ▼
configure("show ip int br")
```

---

# Organização do Projeto

Uma estrutura simples pode ser:

```text
project/
│
├── main.py
│
├── core/
│   ├── interfaces.py
│   ├── registry.py
│   ├── factory.py
│   └── exceptions.py
│
├── strategies/
│   ├── __init__.py
│   ├── cisco.py
│   ├── mikrotik.py
│   ├── juniper.py
│   └── arista.py
│
├── services/
│   └── automation_service.py
│
└── tests/
```

---

# Responsabilidade de cada pasta

## core/

Contém componentes reutilizáveis da aplicação.

* Interfaces
* Factory
* Registry
* Exceções

---

## strategies/

Implementações concretas.

Exemplo:

```text
CiscoStrategy
JuniperStrategy
MikrotikStrategy
```

Cada estratégia conhece apenas um fabricante.

---

## services/

Implementa os casos de uso da aplicação.

Exemplo:

```python
service.configure(device)
```

O serviço decide quando chamar a Factory.

---

# Exemplo Completo

```python
strategy = StrategyFactory.create(device.vendor)

strategy.configure("router ospf 1")
```

A aplicação não sabe qual fabricante está sendo utilizado.

---

# Quando usar cada padrão?

## Use Strategy quando...

Existirem diferentes formas de executar a mesma tarefa.

Exemplos:

* Configurar dispositivos
* Autenticar usuários
* Calcular descontos
* Calcular frete
* Processar pagamentos

---

## Use Factory quando...

A criação do objeto depender de alguma condição.

Exemplo:

```python
StrategyFactory.create(vendor)
```

Em vez de:

```python
if vendor == "cisco":
    ...
```

---

## Use Registry quando...

Novas implementações serão adicionadas frequentemente.

Exemplo:

Hoje:

* Cisco
* MikroTik

Amanhã:

* Juniper
* Arista
* Nokia
* Huawei

Você adiciona apenas uma nova Strategy registrada, sem modificar a Factory.

---

# Benefícios

* Elimina grandes blocos de `if/elif`
* Facilita adicionar novos fabricantes
* Segue o princípio Open/Closed (SOLID)
* Reduz acoplamento
* Código mais organizado
* Facilita testes unitários
* Facilita manutenção

---

# Aplicação em Network Automation

Imagine um inventário:

```yaml
devices:
  - hostname: R1
    vendor: cisco

  - hostname: MT1
    vendor: mikrotik

  - hostname: J1
    vendor: junos
```

O serviço percorre os dispositivos:

```python
for device in devices:

    strategy = StrategyFactory.create(device.vendor)

    strategy.configure("router ospf 1")
```

Cada estratégia envia os comandos corretos para seu fabricante.

---

# Relação com SOLID

## Single Responsibility

Cada Strategy possui apenas uma responsabilidade.

---

## Open/Closed

Adicionar um novo fabricante não exige alterar código existente.

Basta criar:

```python
@StrategyRegistry.register("arista")
class AristaStrategy(ConfigStrategy):
    ...
```

---

## Liskov Substitution

Todas as estratégias implementam a mesma interface.

```python
ConfigStrategy
```

---

## Dependency Inversion

Os serviços dependem da abstração:

```python
ConfigStrategy
```

e não de implementações concretas.

---

# Conclusão

Os três padrões se complementam:

| Padrão   | Responsabilidade                 |
| -------- | -------------------------------- |
| Strategy | Implementa o comportamento       |
| Factory  | Cria a estratégia correta        |
| Registry | Mantém o catálogo de estratégias |

Essa combinação é muito utilizada em frameworks e plataformas de automação porque facilita a evolução do sistema sem modificar código existente.
