line_map={
    "C":"1", "D":"2", "E":"3", "F":"4", "G":"5", "A":"6", "B":"7"
}

def line_to_staff(note):
     if note in line_map:
         return line_map[note]
     else:
         return None
     
line_staff=["C", "D", "E", "F", "G", "A", "B"]
for note in line_staff:
    print(line_to_staff(note))
