def read_file_line_by_line(file_name):
  with open(file_name, 'r') as f:
      while True:
        line = f.readline()
        if not line:
          break
        yield line
lines_generator = read_file_line_by_line('demo.txt')
print(next(lines_generator))
print(next(lines_generator))
print(next(lines_generator))

