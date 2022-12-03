import random

choice = 0
com_choice = 0
com_choose = ["가위", "바위", "보"]
running = True

while running:
    choice = input("나의 선택: ")
    com_choice = random.choice(com_choose)
    print("상대의 선택:" + com_choice)

    if choice == "꺼지셈":
        running = False
        print("끝")

    if choice == "가위":
        if com_choice == "바위":
            print("내 패배")

    if choice == "가위":
        if com_choice == "보":
            print("내 승리")

    if choice == "가위":
        if com_choice == "가위":
            print("무승부")

    if choice == "바위":
        if com_choice == "보":
            print("내 패배")

    if choice == "바위":
        if com_choice == "가위":
            print("내 승리")

    if choice == "바위":
        if com_choice == "바위":
            print("무승부")

    if choice == "보":
        if com_choice == "바위":
            print("내 승리")

    if choice == "보":
        if com_choice == "가위":
            print("내 패배")

    if choice == "보":
        if com_choice == "보":
            print("무승부")
