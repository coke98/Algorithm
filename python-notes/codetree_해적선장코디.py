import sys
import heapq

input = sys.stdin.readline

# Problem
# 코드트리 해적 선장 코디
#
# Approach
# - 사격 대기 선박은 ready 힙, 재장전 중 선박은 reload 힙으로 분리해 관리한다.
# - 공격력 갱신으로 힙 안에 구버전 값이 남을 수 있으므로, 실제 ship 정보와 비교해 stale entry를 버린다.
#
# Review
# - 이 문제는 시뮬레이션이라기보다 상태를 가진 우선순위 큐 관리 문제다.

T = int(input())

ship = {}
ready = []
reload = []
reload_set = set()

hour = 0

for _ in range(T):
    cmdline = list(map(int, input().split()))
    cmd = cmdline[0]

    if cmd == 100:
        N = cmdline[1]
        for i in range(N):
            offset = i * 3
            id, p, r = cmdline[2 + offset:5 + offset]
            ship[id] = (p, r)
            heapq.heappush(ready, (-p, id))

    if cmd == 200:
        id, p, r = cmdline[1:4]
        ship[id] = (p, r)
        heapq.heappush(ready, (-p, id))

    if cmd == 300:
        id, pw = cmdline[1:3]
        p, r = ship[id]
        ship[id] = (pw, r)
        if id not in reload_set:
            heapq.heappush(ready, (-pw, id))

    if cmd == 400:
        attack = []
        damage = 0

        while reload:
            ready_hour, id = reload[0]
            if ready_hour <= hour:
                p, r = ship[id]
                heapq.heappop(reload)
                heapq.heappush(ready, (-p, id))
                reload_set.remove(id)
            else:
                break

        while ready and len(attack) < 5:
            p, id = heapq.heappop(ready)
            if -p != ship[id][0]:
                continue
            attack.append(id)
            damage -= p

        for id in attack:
            p, r = ship[id]
            ready_hour = hour + r
            heapq.heappush(reload, (ready_hour, id))
            reload_set.add(id)

        print(damage, len(attack), *attack)

    hour += 1
