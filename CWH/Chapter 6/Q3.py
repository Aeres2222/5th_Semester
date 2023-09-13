text = input("Enter your text : ")

if ("subscribe" in text) :
    spam = True
elif ("like" in text) :
    spam = True
elif ("comment" in text) :
    spam = True
elif ("share" in text) :
    spam = True
else :
    spam = False

if (spam) :
    print("This is a spam")
else :
    print("This is not spam")