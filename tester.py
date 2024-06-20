import hw1


# DO NOT SUBMIT THIS FILE
# It is just an example of a few tests that we will run on your code that you can use as a starting point
# to make sure the code is correct.
# You should put the two python files in the same folder and run this one

def testNumberOfNodes():
    n5 = 5
    n0 = 0
    graph = hw1.UndirectedGraph(n5)
    assert graph.number_of_nodes() == n5
    graph = hw1.UndirectedGraph(n0)
    assert graph.number_of_nodes() == n0


def testEmptyGraph():
    n = 10
    graph = hw1.UndirectedGraph(n)
    assert graph.number_of_nodes() == n
    for i in range(n):
        for j in range(n):
            if i != j:
                assert graph.check_edge(i, j) == False
        assert len(graph.edges_from(i)) == 0
    print("tested empty graph")


def test_edges_from_and_check_edge():
    n = 5
    graph = hw1.UndirectedGraph(n)
    for i in range(n):
        assert len(graph.edges_from(i)) == 0
    for i in [0, 2, 3, 4]:
        graph.add_edge(1, i)
    for i in [0, 2, 3, 4]:
        assert len(graph.edges_from(i)) == 1
        assert graph.check_edge(i, 1) == True
        assert graph.check_edge(1, i) == True
    assert len(graph.edges_from(1)) == 4
    graph.add_edge(0, 4)
    assert len(graph.edges_from(0)) == 2
    assert len(graph.edges_from(4)) == 2
    assert len(graph.edges_from(2)) == 1
    assert len(graph.edges_from(3)) == 1
    assert len(graph.edges_from(1)) == 4
    assert graph.check_edge(2, 3) == False
    assert graph.check_edge(3, 4) == False
    assert graph.check_edge(0, 3) == False
    print("tested edge_from function, check_edge function")


def test_avg_shortest_path(n):
    test_graph = hw1.UndirectedGraph(3)
    assert test_graph.number_of_nodes() == 3
    test_graph.add_edge(0, 1)
    test_graph.add_edge(2, 1)
    avg = hw1.avg_shortest_path(test_graph)
    assert avg > 1.2  # Should be close to true value of 1.3333
    assert avg < 1.5  # Should be close to true value of 1.3333

    half_n = int(n / 2)
    test_graph = hw1.UndirectedGraph(n)
    for i in range(n-1):
        test_graph.add_edge(i, i+1)
    assert (hw1.avg_shortest_path(test_graph) - (n + 1)/3) < 0.5 #since it's just a sample
    print("tested avg_shortest_path function")


def test_shortest_path(n):
    # empty graph
    test_graph = hw1.UndirectedGraph(n)
    for i in range(n - 1):
        j = i + 1
        while j < n:
            assert hw1.shortest_path(test_graph, i, j) == -1
            j += 1
    assert hw1.shortest_path(test_graph, n - 1, 0) == -1

    half_n = int(n/2)
    # disconnected graph
    for i in range(half_n):
        test_graph.add_edge(i, i+1)

    for i in range(half_n+1):
        assert hw1.shortest_path(test_graph, 0, i) == i
    for i in range(half_n+1, n):
        assert hw1.shortest_path(test_graph, 0, i) == -1
    # line
    for i in range(n-1):
        test_graph.add_edge(i, i+1)
    for i in range(n-1):
        assert hw1.shortest_path(test_graph, i, i + 1) == 1
    i3 = int(n/3)
    assert hw1.shortest_path(test_graph, half_n, i3) == (half_n-i3)
    # cycle
    test_graph.add_edge(0, n-1)
    for i in range(n-2):
        assert hw1.shortest_path(test_graph, i, i + 1) == 1
    assert hw1.shortest_path(test_graph, 0, i3) == i3
    assert hw1.shortest_path(test_graph, 0, half_n) == half_n
    assert hw1.shortest_path(test_graph, 0, n-i3) == i3
    print("tested test_shortest_path")

def test_create_graph_with_P(n, p):
    testGraph2 = hw1.create_graph(n, p)
    outboundNode1List = testGraph2.edges_from(1)
    assert len(
        outboundNode1List) > 2  # With very, very small probability this test will fail even for correct implementation


testNumberOfNodes();
testEmptyGraph()
test_edges_from_and_check_edge()
test_shortest_path(10)
test_avg_shortest_path(10)
test_create_graph_with_P(100, 0.5)

# Now, assuming that facebook_combined.txt is in the same directory as tester.py
testFbGraph = hw1.create_fb_graph("facebook_combined.txt")
assert testFbGraph.number_of_nodes() == 4039
assert testFbGraph.check_edge(107, 1453) == True
assert testFbGraph.check_edge(133, 800) == False

print("all tests passed")
