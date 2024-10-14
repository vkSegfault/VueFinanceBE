from models.asset import Stock, Bond, AssetType

stock_list = [
    Stock(id=1, name='CDR', type=AssetType.STOCK, description="worst sttock I ever bought, dont do it ever, I mean I really like them but theirs stocks are risky as fcuk - someday in futuire mauybe", stocksAmount=20, stockPrice=16023),
    Stock(id=2, name='APPL', type=AssetType.STOCK, stocksAmount=5, stockPrice=123023)
]

bond_list = [
    Bond(id=3, name='moja lokata 1', type=AssetType.BOND, value=500000, rate=65, days=90, tax=19),
    Bond(id=4, name='moja lokata 2', type=AssetType.BOND, value=200000, rate=65, days=90, tax=19),
]