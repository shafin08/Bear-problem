from heapq import heappop, heappush

class Bear_problem(object):
    def __init__(self):
        pass

    def start_node(self):
        """returns start node"""
        start = ("S","S","S","S","S")
        # TODO
        return (start)

    def is_goal(self, node):
        """is True if `node` is a goal"""
        
        # TODO
        count = 0
        for item in node:
            if item == "E":
                count += 1
        if count == 5:
            return True
        else: 
            return False

    def neighbors(self, node):
        """returns a list of the arcs for the neighbors of `node`"""
        # TODO
        neighbor = []
        if (self.is_goal(node)):
            return None
        
        if (node[len(node)-1] == "S"):
            for i in range(len(node)-1):
                new_node = list(node)
                if (node[i] == "S"):
                    new_node[i] = "E"
                    new_node[len(node)-1] = "E"
                    neighbor.append(tuple(new_node))
                else:
                    continue  
        if (node[len(node)-1] == "S"):
            for a in range(len(node) - 1):
                for b in range(a+1, len(node) - 1):
                    n_node = list(node)
                    if(node[a] == "S" and node[b] == "S"):
                        n_node[a] = "E"
                        n_node[b] = "E"
                        n_node[len(node)-1] = "E"
                        neighbor.append(tuple(n_node))
                        continue    
        if(node[len(node) - 1] == "E"):
            for i in range(len(node)-1):
                new_node = list(node)
                if (node[i] == "E"):
                    new_node[i] = "S"
                    new_node[len(node)-1] = "S"
                    neighbor.append(tuple(new_node))
                else:
                    continue        
        
        return neighbor

    def arc_cost(self, arc):
        """Returns the cost of `arc`"""
        # TODO
        cost = 0
        node_a = arc[0]
        node_b = arc[1]
        crossingtime = {'Undergrad': 1.5, 'Graduate': 3, 'Postdoc':7.5,
        'Professor': 10}  
        
        if (node_a[len(node_a) - 1] == "S" and node_b[len(node_b)-1] == "E"):
            char = []
            for i in range(len(node_a)-1):
                if (node_a[i] == "S" and node_b[i] == "E" and i == 0):
                    char.append('Undergrad')
                elif (node_a[i] == "S" and node_b[i] == "E" and i == 1):
                    char.append('Graduate')
                elif (node_a[i] == "S" and node_b[i] == "E" and i == 2):
                    char.append('Postdoc')
                elif (node_a[i] == "S" and node_b[i] == "E" and i == 3):
                    char.append('Professor')
            cost += max(crossingtime[char[0]],crossingtime[char[len(char)-1]])
            
        elif (node_a[len(node_a) - 1] == "E" and node_b[len(node_b) - 1] == "S"):
            char = []
            for i in range(len(node_a)-1):
                if (node_a[i] == "E" and node_b[i] == "S" and i == 0):
                    char.append('Undergrad')
                elif (node_a[i] == "E" and node_b[i] == "S" and i == 1):
                    char.append('Graduate')
                elif (node_a[i] == "E" and node_b[i] == "S" and i == 2):
                    char.append('Postdoc')
                elif (node_a[i] == "E" and node_b[i] == "S" and i == 3):
                    char.append('Professor')
            cost += max(crossingtime[char[0]],crossingtime[char[len(char)-1]])
            cost += 1
        
        return cost        
        

    def cost(self, path):
        """Returns the cost of `path`"""
        return sum(self.arc_cost(arc) for arc in path)

    def heuristic(self, node):
        """Returns the heuristic value of `node`"""
        # TODO
        hcost = 0
        self.undergrad = 1
        self.flashlight = 1
        self.grad = 2
        self.postdoc = 3
        self.proffesor = 4
        
        for i in range(len(node)):
            if((node[i] == "S") and i == 0):
                hcost += self.undergrad
            elif((node[i] == "S") and i == 1):
                hcost += self.grad
            elif((node[i] == "S") and i == 2):
                hcost += self.postdoc
            elif((node[i] == "S") and i == 3):
                hcost += self.proffesor   
            elif((node[i] == "S") and i == 4):
                hcost += self.flashlight          
        
       
        return hcost

    def search(self):
        """Return a solution path"""
        # TODO
        frontier = Frontier()
        start = self.start_node()
        frontier.add([(start,start)], 0)
        
        expanded = []
        
        while not (frontier.is_empty()):
            path = frontier.remove()
            node = path[-1][1]
            
            if (self.is_goal(node)):
                return path
            if node in expanded:
                continue
            
            expanded.append(node)
            
            for neighbor in self.neighbors(node):
                newpath = path + [(node, neighbor)]
                cost = self.arc_cost(newpath) + self.heuristic(neighbor)
                frontier.add(newpath, cost)
                
        return None
             


class Frontier(object):
    """
    Convenience wrapper for a priority queue usable as a frontier
    implementation.
    """

    def __init__(self):
        self.heap = []

    def add(self, path, priority):
        """Add `path` to the frontier with `priority`"""
        # Push a ``(priority, item)`` tuple onto the heap so that `heappush`
        # and `heappop` will order them properly
        heappush(self.heap, (priority, path))

    def remove(self):
        """Remove and return the smallest-priority path from the frontier"""
        priority, path = heappop(self.heap)
        return path

    def is_empty(self):
        return len(self.heap) == 0


def unit_tests():
    """
    Some trivial tests to check that the implementation even runs.
    """
    print("testing...")
    p = Bear_problem()
    assert p.start_node() is not None
    assert not p.is_goal(p.start_node())
    assert p.heuristic(p.start_node()) >= 0
   

    ns = p.neighbors(p.start_node())

    assert len(ns) > 0

    soln = p.search()
    assert p.cost(soln) > 0
    print("tests ok")


def main():
    unit_tests()
    p = Bear_problem()
    soln = p.search()
    if soln:
        print("Solution found (cost=%s)\n%s" % (p.cost(soln), soln))
    else:
        raise RuntimeError("Empty solution")


if __name__ == "__main__":
    main()

