
handle_text = open("mbox-short.txt")

for line in handle_text:
    strip_line = line.rstrip()
    print(strip_line.upper())