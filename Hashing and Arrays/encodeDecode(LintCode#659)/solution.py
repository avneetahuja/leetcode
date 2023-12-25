class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res=""
        for s in strs:
            res += s+":;"
        return res[0:len(res)-2]

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res = str.split(":;")
        return res
