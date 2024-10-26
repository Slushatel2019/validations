def check_rows(rows: "list") -> bool:
    res = []
    for row in rows:
        res.append(
            all(([True if str(x) in row else False for x in range(1, 10)])))
    return all(res)


def check_cols(rows: "list") -> bool:
    res = []
    for i in range(9):
        col = ""
        for j in range(9):
            col += rows[j][i]
    res.append(all(([True if str(x) in col else False for x in range(1, 10)])))
    return all(res)


def check_tiles(rows: "list") -> bool:
    tiles = ["" for _ in range(9)]
    res = []
    for j in range(0, 9, 3):
        for k in range(3):
            row = rows[j+k]
            for i in range(3):
                tiles[j+i] += row[:3]
                row = row[3:]
    for tile in tiles:
        res.append(
            all(([True if str(x) in tile else False for x in range(1, 10)])))
    return all(res)


def input_rows() -> list:
    rows = []
    for i in range(9):
        row = input(f"Please enter row {i+1} : ")
        while not row.isalpha or len(row) != 9:
            print("Row is invalid. Only nine digits must be in one row!")
            row = input(f"Please enter row {i+1} : ")
        rows.append(row)
    return rows


def check_sudoku() -> print:
    rows = input_rows()
    is_valid_rows = check_rows(rows)
    is_valid_cols = check_cols(rows)
    is_valid_tiles = check_tiles(rows)
    is_valid_sudoku = all([is_valid_cols, is_valid_rows,
                           is_valid_tiles])
    print("check_rows = ", is_valid_rows)
    print("check_cols = ", is_valid_cols)
    print("check_tiles = ", is_valid_tiles)
    print("Sudoku is Valid" if is_valid_sudoku else "Sudoku is Invalid")


check_sudoku()
