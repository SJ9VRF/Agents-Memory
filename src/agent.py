from langgraph.graph import StateGraph

class Agent:
    def __init__(self, graph: StateGraph):
        self.graph = graph

    def run(self):
        config = {"configurable": {"user_id": "1", "thread_id": "1"}}
        for chunk in self.graph.stream({"messages": [("user", "my name is John")]}, config=config):
            self.pretty_print_stream_chunk(chunk)

    @staticmethod
    def pretty_print_stream_chunk(chunk):
        for node, updates in chunk.items():
            print(f"Update from node: {node}")
            if "messages" in updates:
                updates["messages"][-1].pretty_print()
            else:
                print(updates)
            print("\n")

