import sys
input = sys.stdin.readline

N = int(input())
atime = btime = ascore = bscore = now = 0

for _ in range(N):
    team, time = input().split()
    team = int(team)

    minute, second = map(int, time.split(':'))
    stime = second + minute * 60    

    if ascore > bscore:
        atime += (stime-now)
    elif bscore > ascore:
        btime += (stime-now)

    if team == 1:
        ascore += 1
    else:
        bscore += 1

    now = stime

if ascore > bscore:
    atime += (48*60-now)
elif bscore > ascore:
    btime += (48*60-now)

print(f'{(atime//60):02}:{(atime%60):02}')
print(f'{(btime//60):02}:{(btime%60):02}')