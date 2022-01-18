teksts = input("Ievadi tekstu: ")
def deleteE(text):
  if text.count("e")>0:
    text = text.upper()
    print(text)
  else:
    text = "TEKSTS NESATUR VAJADZĪGO BURTU."
    print(text)
  return text
deleteE(teksts)