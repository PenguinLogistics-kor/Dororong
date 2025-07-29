import random
import time

Heroes = ['Aglaea', 'Tribbie', 'Mydei', 'Castorice', 'Anaxa', 'Hyacine', 'Cipher', 'Phainon', 'Hysilens', 'Cerydra']

while Heroes:
    hero = random.choice(Heroes)
    print(f"Dead: {hero}")
    Heroes.remove(hero)
    time.sleep(1)

print("All Heroes are dead.")
