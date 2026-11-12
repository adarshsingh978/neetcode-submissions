class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return "-"
        s = ""
        for i in range(len(strs)-1):
            s = s + strs[i] + "-"
        s = s + strs[-1]
        print(f"{s=}")
        return s

    def decode(self, s: str) -> List[str]:
        if s == "-":
            return []
        print("Splitting")
        print(s.split("-"))
        return s.split("-")
