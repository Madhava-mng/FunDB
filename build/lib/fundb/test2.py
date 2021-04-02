import fundb;a = fundb.Fundb("final", "pass",87)
a.write({})

for i in range(1, 7):
    a.insert(f"key{i}", 'value')
print(a.read())
