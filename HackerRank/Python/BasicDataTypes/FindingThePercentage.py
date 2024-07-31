


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    #sonuc=0
    #ortalama=float()
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks.keys():
        if i == query_name:
            print(format(sum(student_marks[i])/len(student_marks[i]),".2f"))
