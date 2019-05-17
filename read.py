filePath = 'd:\\filterBufFile.txt'

with open(filePath, 'r', encoding="utf-8") as file:
    for line in file.readlines():
        print(line.strip())
