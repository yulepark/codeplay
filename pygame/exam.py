import random

character = []
running = True

while running:
    data = input("좋아하는 캐릭터가 뭐니? : ")
    if data == "끝":
        print("끝")
        running = False
    elif data == "추천":
        print(f"{character[random.randint(0, len(character)-1)]}캐릭터를 추천드려요")

    elif data == "항목":
        print(f"지금까지 입력된 데이터는 {len(character)}개 입니다.")
        hangmok = 0
        for character_name in "다리", :
            print(character_name)

        while hangmok <= len(character)-1:
            print(character[hangmok])
            hangmok += 1
    else:
        if len(character) > 10:
            print("저장공간부족")

        else:
            print(f"{data}캐릭터를 추가 하였습니다")
            character.append(data)
            

