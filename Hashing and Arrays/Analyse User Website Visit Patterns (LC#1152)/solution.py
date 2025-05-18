class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # 1) sort by user, then time
        modified_list = sorted(
            zip(username, timestamp, website),
            key=lambda x: (x[0], x[1])
        )
        # 2) build per-user visit sequences
        mappings = defaultdict(list)
        for u, t, w in modified_list:
            mappings[u].append(w)
        
        # 3) global count of patterns → number of distinct users who saw them
        pattern_count = Counter()
        for user, visits in mappings.items():
            # every 3-site subsequence in order; 
            # set(...) ensures we only count each pattern once per user
            seen = set(itertools.combinations(visits, 3))
            for pat in seen:
                pattern_count[pat] += 1
        
        # 4) find max score
        max_score = max(pattern_count.values())
        # 5) among those, pick lexicographically smallest tuple
        best = min(p for p, cnt in pattern_count.items() if cnt == max_score)
        return list(best)
