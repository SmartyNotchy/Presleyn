from imports import *

class Email:
  def __init__(self, starred, unread):
    self.subject = "gib codehs answers pls"
    self.sender = "Henry"
    self.contents = '''\
pls gib codehs answer
due friday
my compsci grade suffer
pls help

- henry'''

    self.starred = starred
    self.unread = unread
    self.deleteable = True

  def getName(self):
    if self.starred:
      return "|Y| ☆ " + self.subject
    elif self.unread:
      return "|R| ! |W|" + self.subject
    else:
      return "|DG|   " + self.subject

  def printDesc(self, offset):
    startStr = "\x1b[{}C".format(offset)
    printC(startStr + "|B|" + self.subject)
    printC(startStr + "*Sent by {}*".format(self.sender))
    printC(startStr + "━" * 50, "B")
    print()
    for line in self.contents.split("\n"):
      printC(startStr + line, "B")