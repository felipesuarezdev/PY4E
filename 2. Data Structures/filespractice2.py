# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
sum_xdspam = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    elif line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        xdspam = line[19:]
        strip_xdspam = xdspam.rstrip()
        float_xdspam = float(strip_xdspam)
        sum_xdspam = sum_xdspam + float_xdspam
        avg_xdspam = sum_xdspam/count
    print(line)
print("Done", sum_xdspam, count, avg_xdspam)