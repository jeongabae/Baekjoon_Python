import sys
N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(N)]
cnt = []

for a in range(N - 7):
    for b in range(M - 7):
        idx1 = 0  # 보드판이 W로 시작할 경우 다시 칠해야 하는 정사각형 개수
        idx2 = 0  # 보드판이로 시작할 경우 다시 칠해야 하는 정사각형 개수
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0: #x,y좌표의 합이 짝수인 경우
                    if board[i][j] == 'B': # 그 중에서 보드판이 W로 시작할 경우 해당 위치에는 W가 있어야하는데 B가 있으므로 idx1+=1
                                            # 그 중에서 보드판이 B로 시작할 경우 해당 위치에는 B가 제 위치에 있으므로 idx2 변화없음.
                        idx1 += 1
                    else:           # 그 중에서 보드판이 B로 시작할 경우 해당 위치에는 B가 있어야하는데 W가 있으므로 idx+=2
                                    # 그 중에서 보드판이 W로 시작할 경우 해당 위치에는 W가 제 위치에 있으므로 idx1 변화없음.
                        idx2 += 1
                else:                #x,y좌표의 합이 홀수인 경우
                    if board[i][j] == 'W': # 그 중에서 보드판이 W로 시작할 경우 해당 위치에는 B가 있어야하는데 W가 있으므로 idx+=1
                                         # 그 중에서 보드판이 B로 시작할 경우 해당 위치에는 W가 제 위치에 있으므로 idx2 변화없음.
                        idx1 += 1
                    else:           # 그 중에서 보드판이 B로 시작할 경우 해당 위치에는 W가 있어야하는데 B가 있으므로 idx+=2
                                    # 그 중에서 보드판이 W로 시작할 경우 해당 위치에는 B가  제 위치에 있으므로 idx1 변화없음.
                        idx2 += 1
        cnt.append(min(idx1, idx2))
print(min(cnt))
