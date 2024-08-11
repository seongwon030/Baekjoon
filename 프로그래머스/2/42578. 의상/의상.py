def solution(clothes):
    c_dict = {}
    answer = 1

    for i in range(len(clothes)):
      if not clothes[i][1] in c_dict:
        c_dict[clothes[i][1]] = 1
      else:
        c_dict[clothes[i][1]] += 1


    for value in c_dict.values():
      answer *= (value+1)
    return answer-1