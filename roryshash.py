import hashlib
from easygui import *
import sys
msg = "my attempt at a recreation of this programme"
choices = ["start", "quit"]
reply = buttonbox(msg,choices=choices)
if(reply == "start"):
	msg = "plz enter the password for hashing, no special characters"
	title = "rorys attempt at this thing at least"
	password = enterbox(msg, title)
	hash = hashlib.sha256(password).hexdigest()
	hash1 = hashlib.sha224(password).hexdigest()
	hash2 = hashlib.sha1(password).hexdigest()
	textbox(msg='The hash of your password is written below. Press control + c to copy it. ', title=" Rorys Hashing program", text="SHA256: " + hash, codebox=0)

elif(reply == "Donate"):
	textbox(msg="Donation Address", title="Matthew's Hashing Program", text="Bitcoin donation address: 169iA76RmnatFXmEthT6AEehxMQ9X1ro3L", codebox=0)

else:
	sys.exit()
