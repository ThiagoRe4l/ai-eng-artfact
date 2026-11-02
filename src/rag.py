from functools import lru_cache
from pathlib import Path

from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import MarkdownHeaderTextSplitter

from src.config import EMBEDDING_MODEL_ID

POLICIES_PATH = Path(__file__).resolve().parent.parent / "data" / "policies.md"
HEADERS = [("##", "section"), ("###", "subsection")]
INTERNAL_SECTIONS = ("7.", "10.") # diretrizes para funcionários, já contempladas pelo sistema(prompt).


def load_policy_chunks() -> list[Document]:
    """Divida o manual em seções/subseções, prefixando cada seção com o caminho do título."""
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=HEADERS)
    documents = []
    for chunk in splitter.split_text(POLICIES_PATH.read_text(encoding="utf-8")):
        section = chunk.metadata.get("section")
        if not section or section.startswith(INTERNAL_SECTIONS):
            continue  # Apenas o título do documento, sem conteúdo.
        title = " > ".join(filter(None, [section, chunk.metadata.get("subsection")]))
        documents.append(
            Document(page_content=f"{title}\n\n{chunk.page_content}", metadata={"title": title})
        )
    return documents


@lru_cache(maxsize=1)
def get_policy_store() -> InMemoryVectorStore:
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL_ID)
    return InMemoryVectorStore.from_documents(load_policy_chunks(), embeddings)


def retrieve_policies(question: str, k: int = 3) -> list[Document]:
    return get_policy_store().similarity_search(question, k=k)