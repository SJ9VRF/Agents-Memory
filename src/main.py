from agent import Agent
from state_graph_builder import build_graph

def main():
    graph = build_graph()
    agent = Agent(graph)
    agent.run()

if __name__ == "__main__":
    main()

