def solution(n, lighthouse):
    answer = 0
    dic = {}
    for item in lighthouse :
        if not item[0] in dic.keys() : dic.setdefault(item[0], 0)
        else : dic[item[0]] += 1
        if not item[1] in dic.keys() : dic.setdefault(item[1], 0)
        else : dic[item[1]] += 1
    sorted_dic = sorted(dic.items(),key=lambda item: item[1], reverse=True)
    order = []
    for item in sorted_dic :
        order.append(item[0])
    print(order)
    while len(lighthouse) :
        for item in lighthouse :
            if order[answer] in item :
                lighthouse.remove(item)
        print(lighthouse)
        answer += 1               
    return answer

print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))