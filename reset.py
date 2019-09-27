from linepy import *
import json, codecs
token = input("login:")
cl = LINE(token,appName="IOS\t8.14.2\tIphone X\t8.1.0")
inv = cl.getGroupIdsInvited()
for y in inv:
    cl.rejectGroupInvitation(y)
    print("reject "+y)
for x in cl.groups:
    cl.leaveGroup(x)
    print("leave "+x)