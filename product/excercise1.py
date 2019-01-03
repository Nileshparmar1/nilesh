'''
a_triplet = map(int, input().split())
b_triplet = map(int, input().split())
alice_points = 0
bob_points = 0
for a_val, b_val in zip(a_triplet, b_triplet):
    if a_val < b_val:
        bob_points += 1
    elif a_val > b_val:
        alice_points += 1
print(alice_points,bob_points)
'''
alice=input()
bob=input()
a_point=0
b_point=0

for i,j in zip(alice,bob):
    if i>j:
        a_point+=1
    if i<j:
        b_point+=1
print(a_point,b_point)
    