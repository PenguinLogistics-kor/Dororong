import random
import time

Heroes = ['아글라이아', '트리비', '마이데이', '카스토리스', '아낙사', '히아킨', '사이퍼', '파이논', '히실렌스', '케리드라']

while Heroes:
    hero = random.choice(Heroes)
    print(f"사망: {hero}")
    Heroes.remove(hero)
    time.sleep(1) 

print("영웅들이 전부 죽었습니다.")
time.sleep(5)
print("재창기에 진입합니다.")
