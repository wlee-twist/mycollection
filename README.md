inv =
3
4
loot
{
'Sword': 1,
'Potion': 3
6
7
'Sword': 1,
'Potion': 2.
'Shield': 1
9
10
11
12
13
14
15
new_inv =
{
k: inv. get(k.
0)
+ loot-get (k, 0) \
for k
in set(inv | 100t)
print(new_inv)


* main.py
main.py > ... inv =
3
4
loot
{
'Sword': 1,
'Potion': 3
6
7
'Sword': 1,
'Potion': 2.
'Shield': 1
9
10
11
12
13
