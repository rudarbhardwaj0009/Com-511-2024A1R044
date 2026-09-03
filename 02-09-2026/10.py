# Take a sentence containing double spaces and unwanted spaces at the beginning or end. Clean the sentence.

s = input("Enter sentence: ")

s = s.strip().replace("  ", " ")

print(s)