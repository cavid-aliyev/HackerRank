# Zipped! -> https://www.hackerrank.com/challenges/zipped/problem

students,subjects = map(int, input().split())

scores = [map(float, input().split()) for _ in range(subjects)]

for student in zip(*scores):
    print(sum(student)/subjects)

