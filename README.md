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
