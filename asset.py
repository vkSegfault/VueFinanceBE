from dataclasses import dataclass
from enum import Enum

def asset() -> None:
    pass

if __name__ == "__asset__":
    asset()

class AssetType(Enum):
    STOCK = 1
    BOND = 2
    MORTGAGE = 3

@dataclass
class Asset:
    id: int
    name: str


@dataclass
class Stock(Asset):
    stocksAmount: int
    stockPrice: Decimal

@dataclass
class Bond(Asset):
    # note that we stor both złote and grosze as int so 2,34 ZŁ is stored as 234 int
    value: int
    rate: int
    days: int
    tax: int
