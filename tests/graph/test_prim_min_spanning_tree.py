from algorithms.graph import prim_min_spanning_tree as prim
import unittest


class TestSuite(unittest.TestCase):
    def test_prim(self):
        # given
        N = 5
        edges = [(1, 2, 10), (2, 3, 5), (3, 4, 20), (1, 4, 80), (4, 5, 30), (1, 4, 15)]
        graph = prim.Graph(N)
        for edge in edges:
            graph.add_edge(edge[0], edge[1], edge[2])
        # when
        start_node = 1
        min_spanning_tree = graph.prim(start_node)
        tree_edges = min_spanning_tree.get_edges()
        # then
        self.assertEqual(len(tree_edges), 4)
        self.assertEqual(sorted(tree_edges), sorted([(1, 2, 10), (1, 4, 15), (2, 3, 5), (4, 5, 30)]))


if __name__ == '__main__':
    unittest.main()
