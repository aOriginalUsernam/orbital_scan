def main():
    try:
        rows = int(input("rows: "))
        columns = int(input("columns: "))
        data_float = int(input("data: "))
        data_2D_format = makeFormat(rows, columns, data_float)
        print_2D_format(data_2D_format)
        print(calc_highest_terain(data_2D_format))
    except ValueError:
        print("corrupt data")


def makeFormat(rows: int, columns: int, data_float: float) -> list[list[bool]]:
    data_str = bin(data_float).removeprefix("0b")
    # data is cannot be bigger than the size of the 2D_list
    if len(data_str) > rows * columns:
        print("data is to big for that format.")
        raise ValueError
    data_2D_format = []
    ind = len(data_str) - 1
    for row in range(rows):
        data_row_format = []
        for column in range(columns):
            if ind < 0:
                data_row_format.append(False)
                continue
            binary_value = data_str[ind]
            if binary_value == "1":
                data_row_format.append(True)
            else:
                data_row_format.append(False)
            ind -= 1
        data_row_format.reverse()
        data_2D_format.append(data_row_format)
    data_2D_format.reverse()
    return data_2D_format


def print_2D_format(data_2D_format: list[list[bool]]) -> None:
    for row in data_2D_format:
        print(row)


def calc_highest_terain(data_2D_format: list[list[bool]]) -> int:
    row_nr = -1
    for row in data_2D_format:
        row_nr += 1
        column_nr = -1
        for column in row:
            column_nr += 1
            if column:
                if check_if_highest(data_2D_format, row_nr, column_nr):
                    return len(data_2D_format) - row_nr
    return -1


def check_if_highest(
    data_2D_format: list[list[bool]], row_id: int, column_id: int
) -> bool:
    if row_id + 1 == len(data_2D_format):
        return True
    elif not data_2D_format[row_id + 1][column_id]:
        return False
    return check_if_highest(data_2D_format, row_id + 1, column_id)


if __name__ == "__main__":
    main()
