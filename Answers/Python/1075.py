number = int(input())

ans = ""

for i in range(1,10001):
    if   i % number == 2:
        ans += str(i) + "\n"

print(ans)
