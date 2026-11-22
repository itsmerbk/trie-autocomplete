class TrieNode:
    def __init__(self): self.kids, self.freq = {}, 0

class AutocompleteTrie:
    def __init__(self): self.root = TrieNode()
    def insert(self, word, freq=1):
        cur = self.root
        for ch in word: cur = cur.kids.setdefault(ch, TrieNode())
        cur.freq += freq
    def suggest(self, prefix, k=3):
        cur = self.root
        for ch in prefix:
            if ch not in cur.kids: return []
            cur = cur.kids[ch]
        res = []
        def dfs(node, path):
            if node.freq: res.append((-node.freq, path))
            for ch, nxt in node.kids.items(): dfs(nxt, path + ch)
        dfs(cur, prefix)
        return [w for _, w in sorted(res)[:k]]

if __name__ == "__main__":
    t = AutocompleteTrie()
    for w, f in [("system", 10), ("sync", 25), ("syntax", 15), ("server", 30)]: t.insert(w, f)
    assert t.suggest("sy", 2) == ["sync", "syntax"]
    print("[PASS] 003_trie_autocomplete")
