def test(name, *args, **kwargs):
    print(name)
    print()
    for arg in args:
        print(arg)

    print()
    for key in kwargs:
        print(key, "=", kwargs[key] )

def main():
    test("bob", 0, 1, "hello", color = "green", value = 8)

main()
