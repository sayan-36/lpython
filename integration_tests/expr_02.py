def main()->i32:
    a: bool
    b: bool
    a = False
    b = True
    a = a and b
    b = a or True
    a = a or b
    return 0

# Not implemented yet in LPython:
#if __name__ == "__main__":
#    main()