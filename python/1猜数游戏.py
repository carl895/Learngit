number = 23
choose = True

while choose:
    guess = int(input("enter an integer :"))

    if guess == number:
        print("congratulation")
        break
    elif guess < number:
        print("litter")
        # 猜小了 游戏结束
        choose = False
    else:
        print("more")
else:
    print("end")

print("Done")