def get_input_data() -> tuple[list[str], list[int], list[int], list[str]]:
    f = open("inputData.txt", "r")
    passes: list[str] = []
    lower_limits: list[int] = []
    higher_limits: list[int] = []
    letters: list[str] = []
    for line in f:
        repeats, letter, passwd = line.split(" ")
        lower, higher = repeats.split("-")
        letter = letter.replace(":", "")
        passwd = passwd.strip()
        passes.append(passwd)
        lower_limits.append(int(lower))
        higher_limits.append(int(higher))
        letters.append(letter)
    return passes, lower_limits, higher_limits, letters
