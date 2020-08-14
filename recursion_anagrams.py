# Anagram is a display of character's permutations
# Ex:
# Given: cat
#
# The output will be:
# cat
# cta
# act
# atc
# tca
# tac
def anagram(text: str):
    solve([], list(text))

def solve(appending: list, remaining: list):
    if len(remaining) == 1:
        print(''.join(appending + remaining))
    for c in remaining:
        re = remaining.copy()
        re.remove(c)

        co = appending.copy()
        co.append(c)

        solve(co, re)

anagram('cat')
