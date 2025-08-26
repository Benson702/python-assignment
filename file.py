fout = open('file.txt', 'w')
line1 = 'This is the first line.\n'
fout.write(line1)
line2 = 'This is the second line.\n'
fout.write(line2)
fout.close()
fhand = open('file.txt', 'r')
print(fhand.read())