N = int(input())    # 센서의 개수 N
K = int(input())    # 집중국의 개수 M
sensor = list(map(int, input().split()))    # sensor들의 위치를 리스트로 받음

sensor = list(set(sensor))  # sensor가 중복되는 위치에 있을 때 제거해서 정리함
sensor.sort()   # 정렬해서 순서대로

length = len(sensor)    # 중복 제거된 sensor 리스트의 길이만큼 길이 지정
lst = [0] * (length-1) 

for idx in range(1, length): # i-1에서 에러 안나도록 1부터 해서 length길이-1 까지
    lst[idx-1] = sensor[idx] - sensor[idx-1]  # 센서 위치 빼주기(거리)

lst.sort()  # 정렬해줌 ex)[1,4,6,2] -> [1,2,4,6]

sums = 0 # 정답 받을 변수 설정
if K >= length: # 집중국의 개수가 length보다 크거나 같으면 패스
    print(0)
else:   # 집중국의 개수 < length일 때
    for crt in range(length-K):   # 집중국의 개수랑 같아질 때까지 돌려야 하므로
        sums += lst[crt]
    print(sums)