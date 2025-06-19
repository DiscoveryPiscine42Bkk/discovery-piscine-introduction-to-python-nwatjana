import sys
def downcase_it(text):
    return text.lower()
args = sys.argv[1:]
if not args:
    print("none")
else:
    for word in args:
        print(downcase_it(word))