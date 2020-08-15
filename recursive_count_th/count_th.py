'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
arr = []
def count_th(word):
    count = 0
    if 'th' not in word:
        global arr
        count = len(arr)
        arr = []
        print(count)
        return count
    else:
        arr.append('th')
        word = word.replace('th', 'a', 1)

    return count_th(word)
    # TBC
