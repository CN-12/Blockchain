import random as rd

a = int(input("몇자리 암호가 필요하신가요? "))

alphabet = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ"
coin = []
for i in range(rd.randint(1, 1000)):
    coin.append(str(rd.randint(0, 10)))
    coin.append(rd.choice(alphabet))

for i in range(rd.randint(1, 1000)):
    rd.shuffle(coin)
    
완성 = "".join(coin)
print(완성[0:a])
