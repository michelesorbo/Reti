def sort_file_content(in_path, out_path):
    lines = []

    with open(in_path) as in_f:
        for line in in_f:
            line.replace('\n', '')
            lines.append(line)

    lines.sort()

    with open(out_path, 'w') as out_f:
        for line in lines:
            out_f.writelines(line)

input_file = "input.txt"
output_file = "output.txt"
sort_file_content(input_file, output_file)