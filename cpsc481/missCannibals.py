from search import *
class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)
    # YOUR CODE GOES HERE

    def actions(self, state):
        m, c, onLeft = state
        possible_actions = ['M', 'C', 'MM', 'CC', 'MC']
        valid_actions = []

        for action in possible_actions:
            m_move = action.count('M')
            c_move = action.count('C')

            # Determine new left-bank counts after the action
            if onLeft:
                new_m = m - m_move
                new_c = c - c_move
            else:
                new_m = m + m_move
                new_c = c + c_move

            # Skip actions that move too many people or lead to impossible states
            if new_m < 0 or new_c < 0 or new_m > self.M or new_c > self.C:
                continue

            # Calculate right-bank counts from left-bank counts
            right_m = self.M - new_m
            right_c = self.C - new_c

                # Ensure missionaries are never outnumbered (unless zero)
            if (new_m == 0 or new_m >= new_c) and (right_m == 0 or right_m >= right_c):
                valid_actions.append(action)

        return sorted(valid_actions)

    def result(self, state, action):
        m, c, onLeft = state
        m_move = action.count('M')
        c_move = action.count('C')

        if onLeft:
            return (m - m_move, c - c_move, False)  # boat moves to right
        else:
            return (m + m_move, c + c_move, True)   # boat returns to left
if __name__ == '__main__':
    mc = MissCannibals(M=3,C=3)

    print(mc.actions((3, 2, True))) # Test your code as you develop! This should return ['CC', 'C', 'M']

    dfs_node = depth_first_graph_search(mc)
    print("DFS path:", dfs_node.solution())
    print("DFS reached goal:", mc.goal_test(dfs_node.state))

    bfs_node = breadth_first_graph_search(mc)
    print("BFS path:", bfs_node.solution())
    print("BFS reached goal:", mc.goal_test(bfs_node.state))
