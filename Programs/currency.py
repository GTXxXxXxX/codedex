m_left_yuan = int(input("What do you have left in yuan ? : "))
m_left_yen = int(input("What do you have left in yen ? : "))
m_left_won = int(input("What do you have left in won ? : "))

yuan_usd = (1 / 7.17) * m_left_yuan
yen_usd = (1 / 139.12) * m_left_yen
won_usd = (1 / 1335.56) * m_left_won

yuan_usd = float(yuan_usd)
yen_usd = float(yen_usd)
won_usd = float(won_usd)

print(yuan_usd + yen_usd + won_usd)


# Sotution de Codédex

# -------------------------

# yuan = int(input('What do you have left in yuan? '))
# yen = int(input('What do you have left in yen? '))
# won = int(input('What do you have left in won? '))

# total = yuan * 0.15 + yen * 0.0077 + won * 0.00080

# print(total)
