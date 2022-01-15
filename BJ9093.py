import sys

M = int(sys.stdin.readline())



for i in range(M):
    s = sys.stdin.readline().rstrip() #rstrip 오른쪽 공백삭제
    words = list(s.split()) #split()안의 매개변수 기준으로 리스트정렬
    #print(list(words))
    reverse_words = []
    for word in words:
        reverse_words.append(word[::-1])
    answer = " ".join(reverse_words)
    print(answer)
