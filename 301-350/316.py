
'''
316. Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"

Thought Process:
If we take the example 'bcabc'; and we try to manually solve this one.

encountered b, [good] --store it [we have nothing, let's start with this character]
encountered c, -- store it too [this is bigger than last one --> good! (lexicographically)]
encountered a, [this is smaller than the ones we have come across in the past, right? If we skip all the past ones because they were bigger than current and also presume that they appear in the future than this is a good candidate to start with.]
-->>Its very clear now, that a stack would be a good DS to use here or perhaps one of the better choices if not the best.
encountered b, [good] -- store it [lexicographically preffered candidate when compared to last item in the stack -- 'a']
...... and keep going on till the string ends; we now have the required string in the stack.
'''


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''Let's start with having three DS - counter for all the character frequecies in the string
                                            - a boolean list for the characters which we encounter so that we can skip them once they are encountered
                                            - a stack to store the lexicographically appropriate order of the string without the duplicates
        '''
        countList = [0]*26
        boolList = [False]*26
        stack = []
        '''Initializer the counter array'''
        for character in s:
            countList[ord(character) - ord('a')] += 1

        '''Traverse the given string'''
        for character in s:
            '''Decrease the count in the counter array as we came across this letter in a respective iteration'''
            countList[ord(character)- ord('a')] -= 1
            '''skip the character altogether if we have encountered it already'''
            if boolList[ord(character) - ord('a')]:
                continue

            '''if the stack is not empty and the iterator points to a character which is smaller than the last element in the stack --> we need to skip all the characters in the stack which are bigger than the current item. And we can only skip the items if there is a chance of encountering them in the future so we also should check for this in this while loop threshold statment'''
            while stack and character<stack[-1] and countList[ord(stack[-1]) - ord('a')] >0:
                '''the control comes here only if the logic found candidates to be removed from the stack. Hence lets just reverse the boolean values for these items as we should consider them fresh new items when we encounter them in the future so that we don't skip them'''
                boolList[ord(stack[-1]) - ord('a')] = False
                '''pop the item'''
                stack.pop()

            '''just add the item to the stack'''
            stack.append(character)

            '''Don't forget to switch the boolean key ON for this item, so we can skip it, if possible'''
            boolList[ord(character) - ord('a')] = True 

        return ''.join(stack)
