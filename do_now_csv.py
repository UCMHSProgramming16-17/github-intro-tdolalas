import csv

donowcsv = open('donowcsv.csv', 'w')

csvwriter = csv.writer(donowcsv, delimiter=',')

csvwriter.writerow(['a', 'b', 'c'])
csvwriter.writerow(['d', 'e', 'f'])
csvwriter.writerow(['g', 'h', 'i'])
csvwriter.writerow(['j', 'k', 'l'])
csvwriter.writerow(['m', 'n', 'o'])

donowcsv.close()