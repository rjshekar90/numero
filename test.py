
def lst(L = None):
    while True:
        if L is None:
            L = []
            L.append(str(input(">>> ")))
            break
    return L

print lst()
