letter='''To lord [Lord/Lady] of House [House Name],

From the Seat of the Iron Throne, I, King Aeres Targaryen,\nKing of the Andals, the Rhoynar, and the First Men,\nLord of the Seven Kingdoms Protector of the Realm,\ndoth issue this royal decree.
\nThe winds of change blow fiercely across the realm,\nand dark shadows encroach upon the land.\nIt is with a heavy heart that I summon you,\n[Lord/Lady] of House [House Name],\nmy steadfast and valiant vassal,\nto join me in the defense of the realm.\nOur unity and loyalty are our strongest shields against the encroaching storm.
\nAs we have known throughout history,\nHouse Targaryen's strength has always been in the unity of its loyal vassals.\nThe dragons may soar high,\nbut they do so with the unwavering support of their allies on the ground.
\nThe realm faces an impending threat that requires our immediate action.\nBy virtue of your sworn oaths and fealty to House Targaryen,\nI command you to muster your forces and march forth to [Location of Gathering] without delay.\nLet not any obstacle hinder your resolve,\nfor we stand stronger together than apart.
\nOur enemies may seek to sow seeds of discord and division amongst us,\nbut let not their deceit sway your loyalty.\nRemember the bond that unites us all,\nforged through years of shared history and bloodshed in the name of House Targaryen.
\nIn the face of adversity, we shall rise united, like dragons soaring through the sky,\na sight that shall strike fear into the hearts of our foes.\nThe time has come to prove the strength of our House's and defend the legacy of the Dragonlords.
\nMay the gods guide your path,\nand may the spirits of our ancestors watch over you as you prepare for this noble undertaking.\nThe future of the Seven Kingdoms lies in our hands,\nand with your valor and unwavering loyalty,\nI have no doubt that we shall emerge victorious.
\nRally to the call, [Lord/Lady] of House [House Name],\nand let the world witness the might and resilience of House Targaryen.

King Aeres Targaryen
First of His Name
King of the Andals, the Rhoynar, and the First Men, 
Lord of the Seven Kingdoms Protector of the Realm
The King on the Iron Throne
"Fire and Blood!""'''


name = input("Enter your name : ")
house = input("Enter house : ")
location = input("Enter location : ")
letter = letter.replace("[Lord/Lady]", name)
letter = letter.replace("[House Name]", house)
letter = letter.replace("[Location of Gathering]", location)
print(letter)