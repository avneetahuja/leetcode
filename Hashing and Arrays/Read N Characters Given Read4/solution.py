"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if n<=4:
            read4(buf)
            temp = n
            while buf[temp-1] == ' ':
                buf[temp-1]=''
                temp-=1
            return n
        remainder = n%4
        quotient = n//4
        c= 0
        for i in range(quotient+1):
            arr = ['']*4
            read4(arr)
            for j in range(4):
                buf[4*c+j] = arr[j]
            c+=1
        ptr = 4*c-1
        for i in range(ptr,ptr-remainder,-1):
            if i==n:
                break
            buf[i] = ''

        return n if n<len(buf) else len(buf)
        
