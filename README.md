old
1
2
3
4
5
new
6001
08
=
l'a',
'b', 'a', 'c', 'b', 'a']
= list(dict.fromkeys(old) •keys))
print (new)



inv ={
'Sword': 1,
'Potion': 3
}
loot ={
'Sword': 1,
'Potion': 2.
'Shield': 1
}
new_inv ={
k: inv.get(k,0) + loot.get(k, 0) \
for k in set(inv | 100t)
}

print(new_inv)
