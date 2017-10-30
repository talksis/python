
f = open('text.txt', 'r')
for i in range(10):
    f.write('안녕하세요 저는 박성준 입니다.'+str(i)+"\n")
f.close()
