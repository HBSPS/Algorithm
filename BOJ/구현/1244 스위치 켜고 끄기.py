# 1244 스위치 켜고 끄기

N = int(input())

light = [0] + list(map(int, input().split()))

def OnOff(arr, index):
    if arr[index] == 1:
        arr[index] = 0
    else:
        arr[index] = 1

for _ in range(int(input())):
    T, S = map(int, input().split())

    if T == 1:
        for i in range(S, N+1, S):
            OnOff(light, i)
    
    else:
        start = S - 1
        end = S + 1

        OnOff(light, S)

        while 1 <= start and end <= N:
            if light[start] == light[end]:
                OnOff(light, start)
                start -= 1

                OnOff(light, end)
                end += 1
            
            else:
                break

for i in range(1, N + 1):
    print(light[i], end=' ')

    if i % 20 == 0:
        print()