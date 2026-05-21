def main():
    list1 = ["a", "b", "c", 1, 2, 3]
    list2 = ["에이","비","씨",'one','two','three']

    # pydentic code
    for ele in list1:
        print(ele)
    
    # bad ex..
    for i in range(len(list1)):
        print(list1[i],i)
    for i in range(len(list1)):
        print(list1[i],list2[i])
    
    # 루프의 횟수를 체크를 해야하는 경우
    for i, ele in enumerate(list1):
        print(ele,i)
    for ele1, ele2 in zip(list1, list2):
        print(ele1, ele2)


if __name__=="__main__":
    main()