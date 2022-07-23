running = True

while running:
    ask = input("궁금한 계산을 넣어주세요 : ")
    numbers = []
    result = 0
    if ask == "꺼져":
        print("님이나 ㅋ")
        running = False  
    else: 
        if "+" in ask:
            print("덧셈결과")
            numbers = ask.split("+")
            result = (int(numbers[0]) + int(numbers[1]))
            print(f"{ask} = {result}")
        elif "-" in ask:
            print("뺄셈결과")
            numbers = ask.split("-")
            result = (int(numbers[0]) - int(numbers[1]))
            print(f"{ask} = {result}")
        elif "*" in ask:
            print("곱셈결과")
            numbers = ask.split("*")
            result = (int(numbers[0]) * int(numbers[1]))
            print(f"{ask} = {result}")
        elif "/" in ask:
            print("나눗셈결과")
            numbers = ask.split("/")
            result = (int(numbers[0]) / int(numbers[1]))
            print(f"{ask} = {result}")
        else:
            print("똑바로 말해라")