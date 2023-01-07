def word_in():
    k = open("korean.txt", "a", encoding = "UTF-8")
    e = open("english.txt", "a", encoding = "UTF-8")
    while True:
        word = input("한글 단어를 입력하시오(종료 = q) : ")
        if word == "q":
            break
        else:
            k.write(word + "\n")
        word = input("영어 단어를 입력하시오(종료 = q) : ")
        if word == "q":
            break
        else:
            e.write(word + "\n")
    k.close()
    e.close()
def exam():
    k = open("korean.txt", "w", encoding = "UTF-8")
    e = open("english.txt", "w", encoding = "UTF-8")

    kwords = []
    ewords = []

    for r in k.readlines():
        kwords.append(r.strip())
    for r in e.readlines():
        ewords.append(r.strip())

    score = 0

    for i in len(kwords):
        answer = input(f"{kwords[0]} 단어를 영어로? => ")
        if answer == "q":
            break
        if answer == ewords[0]:
            print("정답입니다")
            score += 1
        else:
            print(f"땡! 정답 = {ewords[0]}")
    print("수고하셧음")
    print(f"{len(kwords)}문제중 {score}개 정답")
    if score ==  len(kwords):
        print("만점")
    else:
        print("분발하세요")

    k.close
    e.close

mode = 0

while True:
    mode = int(input("1 = 단어입력, 2 =단어시험, 3 = 종료"))
    if mode == 1:
        word_in()
    elif mode == 2:
        exam()
    elif mode == 3:
        break
    else:
        print("재입력 해주세요")