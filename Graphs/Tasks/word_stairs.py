import itertools

from Graphs.graph import Graph


def build_graph(words):
    g = Graph()
    buckets = {}
    for word in words:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in buckets:
                buckets[bucket].append(word)
            else:
                buckets[bucket] = [word]

    for bucket in buckets.keys():
        if len(buckets[bucket]) > 1:
            for w1, w2 in itertools.product(buckets[bucket], buckets[bucket]):
                if w1 != w2:
                    g.add_edge(w1, w2)
    return g


if __name__ == '__main__':
    words = ['SAGE', 'SALE', 'PALE', 'PAGE', 'POPE', 'POLE', 'POLL', 'PALL',
             'FALL', 'FAIL', 'FOIL', 'FOUL', 'FOOL', 'COOL', 'POOL']
    g = build_graph(words)
    g.bfs('SAGE')
    path = g.traverse('FOOL')
    
    [print(el.get_key()) for el in path]
