# Long-Term Memory Agents
## Overview
This project demonstrates the implementation of an agent with long-term memory capabilities using LangGraph.


![Screenshot_2025-01-07_at_9 42 34_PM-removebg-preview](https://github.com/user-attachments/assets/7a373819-fed9-4d56-babf-7d3a79f8f170)

## Technical Overview of the Long-Term Memory Agent

The Long-Term Memory Agent is designed to simulate a conversational AI that retains information across sessions. It integrates several advanced technologies and libraries focused on machine learning, natural language processing, and memory management. Here is a detailed breakdown of the system components and their interactions.

### Core Components

1. **LangChain and LangGraph**:
   - **LangChain**: A framework that provides tools for building language models and integrating them with functionalities like web searching or memory storage.
   - **LangGraph**: Facilitates the creation of stateful conversational agents using a graph-based approach, managing flow control in conversations.

2. **Memory Tools**:
   - **InMemoryVectorStore**: Uses in-memory storage to keep vectors of embedded sentences, enabling quick retrieval of information based on similarity searches.
   - **OpenAIEmbeddings**: Provides embeddings from OpenAI models, converting text into vector representations for storage and retrieval.

3. **Agent Functionality**:
   - **Memory Management**: Stores memories as vectors with associated metadata (e.g., user IDs) for personalized retrieval, maintaining context in interactions.
   - **Search and Retrieval**: Searches through stored memories to find relevant information based on the current conversational context, enhancing responses with historical data.

### Data Flow

1. **Initialization**:
   - Environment variables for API keys are set to ensure secure API interactions.
   - The system initializes with necessary embeddings and tools loaded.

2. **Conversation Start**:
   - The agent begins with a memory loading phase where it fetches any existing memories relevant to the user.
   - User input is processed and responded to by dynamically generating replies based on both the current input and retrieved memories.

3. **Memory Operations**:
   - Memories can be saved or recalled at any point in the conversation, with saving involving embedding the text and storing it with user-specific metadata. Recall involves searching the vector store for vectors close to the query vector derived from the current conversation.

4. **Graph-Based Execution**:
   - The conversation is managed as a traversal through a graph of states (nodes), where each node represents a functional step like memory recall, user input processing, or external tool invocation.
   - Conditional edges in the graph determine the next node based on the conversation state, allowing for dynamic response generation and memory integration.

5. **Tool Invocation**:
   - Tools such as memory storage and retrieval or external search are invoked as needed, bound to the model and can be triggered by specific conditions or user inputs.

### Extensions and Scalability

- **Scalability**: While the current system uses an in-memory vector store, it can be scaled to use distributed databases or cloud storage solutions for handling larger data volumes and more complex retrieval algorithms.
- **Extensibility**: New tools and functionalities, such as additional APIs for different types of data retrieval or more advanced embedding techniques, can be integrated seamlessly due to the modular nature of LangChain and LangGraph.

This agent demonstrates the potential of advanced AI models in providing personalized and context-aware interactions, making it a robust solution for scenarios requiring long-term interaction memory.
