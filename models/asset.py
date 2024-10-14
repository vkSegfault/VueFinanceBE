from enum import Enum
from pydantic import BaseModel
from typing import Optional

# def asset() -> None:
#     pass

# if __name__ == "__asset__":
#     asset()

class AssetType(Enum):
    STOCK = 'STOCK'
    BOND = 'BOND'
    MORTGAGE = 'MORTGAGE'


class Asset(BaseModel):
    id: int
    name: str
    type: AssetType
    description: Optional[str] = ""


class Stock(Asset):
    stocksAmount: int
    stockPrice: int


class Bond(Asset, BaseModel):
    # note that we stor both złote and grosze as int so 2,34 ZŁ is stored as 234 int
    value: int
    rate: int
    days: int
    tax: int
