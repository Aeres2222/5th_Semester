letter='''To lord [Lord/Lady] of House [House Name],

From the Seat of the Iron Throne, I, King Aeres Targaryen, King of the Andals, the Rhoynar, and the First Men, 
Lord of the Seven Kingdoms Protector of the Realm, doth issue this royal decree.

The winds of change blow fiercely across the realm, and dark shadows encroach upon the land. 
It is with a heavy heart that I summon you, [Lord/Lady] of House [House Name], 
my steadfast and valiant vassal, to join me in the defense of the realm. 
Our unity and loyalty are our strongest shields against the encroaching storm.
As we have known throughout history, 
House Targaryen's strength has always been in the unity of its loyal vassals. 
The dragons may soar high, but they do so with the unwavering support of their allies on the ground.
The realm faces an impending threat that requires our immediate action. 
By virtue of your sworn oaths and fealty to House Targaryen, 
I command you to muster your forces and march forth to [Location of Gathering] without delay. 
Let not any obstacle hinder your resolve, for we stand stronger together than apart.
Our enemies may seek to sow seeds of discord and division amongst us, 
but let not their deceit sway your loyalty. 
Remember the bond that unites us all, 
forged through years of shared history and bloodshed in the name of House Targaryen.
In the face of adversity, we shall rise united, like dragons soaring through the sky, 
a sight that shall strike fear into the hearts of our foes. 
The time has come to prove the strength of our House and defend the legacy of the Dragonlords.
May the gods guide your path, 
and may the spirits of our ancestors watch over you as you prepare for this noble undertaking. 
The future of the Seven Kingdoms lies in our hands, and with your valor and unwavering loyalty, 
I have no doubt that we shall emerge victorious.
Rally to the call, [Lord/Lady] of House [House Name], 
and let the world witness the might and resilience of House Targaryen.

King Aeres Targaryen
First of His Name
King of the Andals, the Rhoynar, and the First Men, 
Lord of the Seven Kingdoms Protector of the Realm
The King on the Iron Throne
"Fire and Blood!"'''


name = input("Enter your name : ")
house = input("Enter house : ")
location = input("Enter location : ")
letter = letter.replace("[Lord/Lady]", name)
letter = letter.replace("[House Name]", house)
letter = letter.replace("[Location of Gathering]", location)
print(letter)