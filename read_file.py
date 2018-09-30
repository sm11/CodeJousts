# f = open('my_path/my_file.txt', 'r')
# file_data = f.read()
# f.close()

camelot_lines = []
with open("some_file.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)