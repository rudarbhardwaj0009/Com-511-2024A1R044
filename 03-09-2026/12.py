# Write a python program to detect whether a comment is spam or not . A comment should be treated
# as spam if it contains any of these keybords : " make a lot of money ", "buy now ", "subscribe this",
# or " click this".

c = input("Comment: ")

if "buy now" in c or "click this" in c:
    print("Spam")
else:
    print("Not Spam")