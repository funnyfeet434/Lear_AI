f = open('my_file.txt', 'r+')
content = f.read()
f.seek(0, 0)
f.write('Hello world!' + content)
f.close