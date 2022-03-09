class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        p = 0
        ans = []
        while p < len(words):
            currlen = len(words[p])
            currwords = [words[p]]
            p += 1
            while p < len(words) and currlen + 1 + len(words[p]) <= maxWidth:
                currwords.append(words[p])
                currlen += 1 + len(words[p])
                p += 1
            if p < len(words): # not last line
                extralen = maxWidth - currlen
                if len(currwords) == 1:
                    ans.append(currwords[0] + ' ' * extralen)
                else: # add spaces between
                    num_larger_spaces = extralen % (len(currwords) - 1)
                    q = 0
                    adder = ""
                    while q < num_larger_spaces:
                        adder += currwords[q] + ' ' * (extralen // (len(currwords) - 1) + 2)
                        q += 1
                    while q < len(currwords) - 1:
                        adder += currwords[q] + ' ' * (extralen // (len(currwords) - 1) + 1)
                        q += 1
                    adder += currwords[q]
                    ans.append(adder)
            else: # last line
                extralen = maxWidth - currlen
                adder = ' '.join(currwords) + ' ' * extralen
                ans.append(adder)
        return ans