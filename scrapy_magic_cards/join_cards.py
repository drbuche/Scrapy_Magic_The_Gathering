import pandas as pd

cards_lega = pd.read_csv('cards_legacy.csv')
cards_modern = pd.read_csv('cards_modern.csv')
cards_pioneer = pd.read_csv('cards_pioneer.csv')
cards_standard = pd.read_csv('cards_standard.csv')
cards_special = pd.read_csv('cards_special.csv')

cards_unidas = pd.concat([cards_lega, cards_modern,cards_pioneer,cards_standard, cards_special])

cards_unidas.dropna(subset=['nome'], inplace=True)

cards_unidas.to_csv('data_cards.csv', index=False)