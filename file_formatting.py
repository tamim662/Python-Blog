file=open("file_name",'r')
for line in file:
      if line!= '\n':
          #the strip method is used to remove white spaces in any of the given lines
          file_contents.append(line.strip())
      else:
          #the replace method is used to remove the blank line or new line after the 4th line
          #here instead of replace method we could have used pass too.
          # line.replace('\n', '')
          pass
