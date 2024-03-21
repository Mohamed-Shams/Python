try:
    S = input()
    i = int(S)
except ValueError:
    print("Bad String")
finally:
    print(i)