# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути. Если только вы не умеете проходить
# сквозь стены, вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.

p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())

s1 = (p1 - q1)
s2 = (p2 - q2)

if s1 < 0:
    s1 = s1 * -1
if s2 < 0:
    s2 = s2 * -1
print(s1 + s2)