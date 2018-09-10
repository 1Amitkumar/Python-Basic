frnd = {'ram': '111-222-333', 'sita': '888-999-666', 'gita': '666-33-111'}

print(frnd.popitem())

frnd.clear()

print(frnd)


frnds = {'ravi': '111-222-333', 'rohit': '888-999-666', 'meena': '666-33-111'}

print(frnds.keys())


print(frnds.values())


print(frnds.get('ravi'))


print(frnds.get('rohit', 'Not Exists'))


print(frnds.pop('meena'))


print(frnds)
