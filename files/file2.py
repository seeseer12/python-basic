with open("test.txt", "r") as f:
    print(f.tell())   # 0

    print(f.read(5))
    print(f.tell())   # 5

    f.seek(0)
    print(f.tell())   # 0