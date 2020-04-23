solutions = []
currentSolution = ''
unprocessed = ''


def decode(s):
    flipped = s[::-1]
    global solutions
    global unprocessed
    global currentSolution
    currentSolution = ''
    unprocessed = flipped
    _decode()
    return solutions


def is_valid(split):
    if split.startswith('0'):
        return False
    value = int(split)
    if value < 10 or value > 126:
        return False
    return True


def _decode():
    global unprocessed
    global currentSolution
    global solutions
    if len(unprocessed) == 0:
        solutions.append(currentSolution)
    else:
        possible_splits = list()
        possible_splits.append(unprocessed[0:2])
        possible_splits.append(unprocessed[0:3])

        for split in possible_splits:
            if is_valid(split):
                decoded_character = chr(int(split))
                currentSolution += decoded_character
                unprocessed = unprocessed[len(split):]
                _decode()
                currentSolution = currentSolution[0: len(currentSolution) - 1]
                unprocessed = split + unprocessed


def main():
    final_solutions = decode('0018014111117811180180110127')
    final_solutions = decode('711113286778797114101')
    print(final_solutions)


if __name__ == '__main__':
    main()
