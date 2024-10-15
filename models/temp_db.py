from models.asset import Stock, Bond, AssetType


stock_list = [
    Stock(id='cf57432e-809e-4353-adbd-9d5c0d733868', name='CDR', type=AssetType.STOCK, description="worst sttock I ever bought, dont do it ever, I mean I really like them but theirs stocks are risky as fcuk - someday in futuire mauybe", stocksAmount=20, stockPrice=16023),
    Stock(id='cf57432e-809e-4353-adbd-9d5c0d733868', name='APPL', type=AssetType.STOCK, stocksAmount=5, stockPrice=123023)
]

bond_list = [
    Bond(id='cf57432e-809e-4353-adbd-9d5c0d733868', name='moja lokata 1', type=AssetType.BOND, value=500000, rate=65, days=90, tax=19),
    Bond(id='cf57432e-809e-4353-adbd-9d5c0d733868', name='moja lokata 2', type=AssetType.BOND, value=200000, rate=65, days=90, tax=19),
]