import one

print("Top Level Two.py")

one.func()

if __name__ == "__main__":
    print("Two.py is being run directly")
else:
    print("two is being imported")
