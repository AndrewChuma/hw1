from typing import List, Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[str]:
    val = []
    with open(file_name) as fi:
        for line in fi:
            val.append(int(line.rstrip()))

    val.sort()
    print(val)
    return (val[0], val[-1])
