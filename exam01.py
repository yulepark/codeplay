import random
criminal = ["송쌤", "코딩쌤", "진원쌤", "빡빡이"]
place = ["코드플레이", "편의점", "코딩학원", "용문역"]
tool = ["머리 한가닥", "안경", "마스크", "칼"]
d = random.choice(criminal)
c = random.choice(place)
f = random.choice(tool)
print(f"{d}(이)가 {c}에서 {f}(으)로 사람을 죽임. 와 대박사건")