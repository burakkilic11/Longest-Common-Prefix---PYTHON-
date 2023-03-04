def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    base = strs[0]
    for i in range(len(base)):
        for word in strs[1:]:
            if i == len(word) or word[i] != base[i]:
                return base[0:i]
    return base


def main():
    strings = []
    is_there_any_other_string = "yes"
    while is_there_any_other_string == "yes":
        string = input("Type string:")
        strings.append(string)
        is_there_any_other_string = input("Is there any other string? (yes/no): ")
    prefix = longestCommonPrefix(strings)
    print("The longest common prefix is:", prefix)

if __name__ == "__main__":
    main()
