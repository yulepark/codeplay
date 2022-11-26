words = ["느금마", "시발", "좆까", "개새끼", "병신", "지랄", "니앰창", "썅년", "븅딱", "박찬"]
bad_word = 0
chat = 0
s = 0
while True:
    chat = input("코딩쌤한테 하고싶은말")
    bad_word = 0
    if chat == "관리자":
        s = input("새로운 금칙어를 입력하세요")
        words.append(s)
        print(f"{s} 단어를 금칙어로 등록했습니다")
        print(words)
        continue

    for q in words:
        if q in chat:
            bad_word += 1
    if bad_word > 0:
        print("관리자: 아 씨발련들아 욕좀 작작쳐쓰라고 앰뒤색기들")
    else:
        print(chat)
            