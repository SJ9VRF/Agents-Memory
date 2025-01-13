from langchain_core.tools import tool
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai.embeddings import OpenAIEmbeddings
from utils import get_user_id

recall_vector_store = InMemoryVectorStore(OpenAIEmbeddings())

@tool
def save_recall_memory(memory: str, config):
    user_id = get_user_id(config)
    document = Document(page_content=memory, id=str(uuid.uuid4()), metadata={"user_id": user_id})
    recall_vector_store.add_documents([document])
    return memory

@tool
def search_recall_memories(query: str, config):
    user_id = get_user_id(config)
    def _filter_function(doc: Document):
        return doc.metadata.get("user_id") == user_id
    documents = recall_vector_store.similarity_search(query, k=3, filter=_filter_function)
    return [document.page_content for document in documents]

