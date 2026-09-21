from lab.attention import attention

if __name__ == "__main__":
    keys = [[1, 0], [0, 1], [1, 1]]
    values = [[10, 0], [0, 10], [5, 5]]
    for query in [[1, 0], [0, 1]]: print(query, "->", [round(x, 2) for x in attention(query, keys, values)])
