
filename = "hamlet_text.txt"

outputFile = "Lines.txt"

player = "BERNARDO"

isPlayerLine = False
with open (filename, 'rt') as file:
  with open (outputFile, "wt") as out:
    for line in file.readlines():
      if line.startswith(player):
        isPlayerLine = True
        out.write(line)
      elif line.startswith('\t') and isPlayerLine:
        out.write(line)
      else:
        isPlayerLine = False