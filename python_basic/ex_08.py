mt = {'대성리':0,
      '춘천':0,
      '을왕리':0,
      '청평':0}

for key in mt :
    print(f'{key}:{mt[key]}표', end=" ")
print('\n')
print("<< MT 장소 투표 >>")

while True :
    vote = input("장소 : ")
    if not vote :
        break
    mt[vote] += 1

result = max(mt, key=mt.get) # key : 비교의 기준

for key in mt :
    print(f'{key}:{mt[key]}표', end=" ")
print('\n')
print(f'최다득표 : {result} {mt[result]}표')



