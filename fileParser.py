quotes = "Quotes.txt"
  
# quotesFile = open(quotes,"r")
#
# line = quotesFile.readline()
#
# print(line)
#
# linePieces = line.split()
#
# print(linePieces)
#
# linePieces = line.split("-")
#
# print(linePieces)
#
# line = line.strip()
#
# linePieces = line.split("-")
#
# print(linePieces)
#
# quotesFile.close()

quotesFile = open(quotes,"r")

# for line in quotesFile:
#     line = line.strip()
#     linePieces = line.split("-")
#     print(f"Quote: {linePieces[0]}")
#     print(f"Speaker: {linePieces[1]}")
#
# quotesFile.close()

sunspotData = "Sunspots.csv"

sunspotFile = open(sunspotData,"r")

for line in sunspotFile:
    line = line.strip()
    linePieces = line.split(",")

    dateSplit = linePieces[0].split("-")

    print(f"Month: {dateSplit[1]}", end=" ")
    print(f"Year: {dateSplit[0]}", end=" ")
    print(f"Mean Sunspots: {linePieces[1]}")

sunspotFile.close()

