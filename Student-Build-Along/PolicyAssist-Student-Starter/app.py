import re
from pathlib import Path

import streamlit as st


# ============================================================
# CONFIGURATION
# ============================================================

APP_TITLE = "PolicyAssist AI"
APP_SUBTITLE = "Student Build-Along Starter"
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

MAX_RESULTS = 2
MIN_RELEVANCE_SCORE = 2
TOP_RESULT_MARGIN = 0.45
MAX_EXCERPT_CHARACTERS = 1600


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📘",
    layout="wide",
)


# ============================================================
# STYLING
# ============================================================

st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }
    .subtitle {
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    .policy-card {
        padding: 1rem;
        border: 1px solid #d9d9d9;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .source-label {
        font-size: 0.85rem;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "be",
    "can",
    "do",
    "does",
    "for",
    "from",
    "get",
    "how",
    "i",
    "in",
    "is",
    "it",
    "me",
    "of",
    "on",
    "or",
    "our",
    "per",
    "please",
    "the",
    "their",
    "they",
    "this",
    "to",
    "what",
    "when",
    "where",
    "which",
    "who",
    "with",
    "you",
    "your",

    # Generic organizational language
    "policy",
    "organization",
    "employee",
    "employees",
    "company",
    "people",
    "work",
}


def normalize_text(text):
    """Normalize text for retrieval matching."""
    return re.sub(r"[^a-z0-9\s-]", " ", text.lower())


def tokenize(text):
    """Return meaningful normalized search terms."""
    normalized = normalize_text(text)

    tokens = re.findall(
        r"[a-z0-9]+(?:-[a-z0-9]+)?",
        normalized,
    )

    meaningful = []

    for token in tokens:
        if token in STOPWORDS:
            continue

        meaningful.append(token)

        if "-" in token:
            meaningful.extend(
                part
                for part in token.split("-")
                if part
            )

    return set(meaningful)


def load_policy_documents():
    """Load all Markdown policy files from the data folder."""
    documents = []

    if not DATA_DIR.exists():
        return documents

    for file_path in sorted(DATA_DIR.glob("*.md")):
        try:
            content = file_path.read_text(
                encoding="utf-8"
            )
        except OSError:
            continue

        documents.append(
            {
                "name": file_path.stem.replace(
                    "_",
                    " ",
                ).title(),
                "filename": file_path.name,
                "content": content,
            }
        )

    return documents


def score_document(query, document):
    """
    Score a policy using weighted topic relevance.

    Specific policy concepts receive more weight than
    generic organizational words.
    """
    query_terms = tokenize(query)

    if not query_terms:
        return 0.0

    policy_name = document["name"]
    filename = Path(
        document["filename"]
    ).stem.replace(
        "_",
        " ",
    )
    content = document["content"]

    name_terms = tokenize(policy_name)
    filename_terms = tokenize(filename)
    content_terms = tokenize(content)

    score = 0.0

    # --------------------------------------------------------
    # 1. Strong policy-name / filename matches
    # --------------------------------------------------------

    title_matches = query_terms.intersection(
        name_terms
    )

    filename_matches = query_terms.intersection(
        filename_terms
    )

    score += len(title_matches) * 8.0
    score += len(filename_matches) * 6.0

    # --------------------------------------------------------
    # 2. Specific content matches
    # --------------------------------------------------------

    content_matches = query_terms.intersection(
        content_terms
    )

    score += len(content_matches) * 1.0

    # --------------------------------------------------------
    # 3. Exact query phrase
    # --------------------------------------------------------

    normalized_query = normalize_text(query)
    normalized_name = normalize_text(policy_name)
    normalized_filename = normalize_text(filename)
    normalized_content = normalize_text(content)

    if (
        normalized_query
        and normalized_query in normalized_name
    ):
        score += 10.0

    if (
        normalized_query
        and normalized_query in normalized_filename
    ):
        score += 8.0

    # --------------------------------------------------------
    # 4. Specific multi-word concepts
    # --------------------------------------------------------

    meaningful_terms = list(query_terms)

    for i, first_term in enumerate(meaningful_terms):
        for second_term in meaningful_terms[i + 1:]:
            phrase_1 = (
                f"{first_term} {second_term}"
            )
            phrase_2 = (
                f"{second_term} {first_term}"
            )

            if phrase_1 in normalized_content:
                score += 2.0

            if phrase_2 in normalized_content:
                score += 2.0

    return round(score, 2)


def find_relevant_policies(
    query,
    documents,
    max_results=MAX_RESULTS,
):
    """
    Return only policies with strong evidence of relevance.

    A policy must:
    1. Meet the minimum relevance score.
    2. Be reasonably close to the strongest result.
    """
    scored = []

    for document in documents:
        score = score_document(
            query,
            document,
        )

        scored.append(
            {
                **document,
                "score": score,
            }
        )

    scored.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    if not scored:
        return []

    top_score = scored[0]["score"]

    if top_score < MIN_RELEVANCE_SCORE:
        return []

    relevant = [
        item
        for item in scored
        if (
            item["score"] >= MIN_RELEVANCE_SCORE
            and (
                item["score"] == top_score
                or (
                    top_score > 0
                    and item["score"] / top_score
                    >= TOP_RESULT_MARGIN
                )
            )
        )
    ]

    return relevant[:max_results]


def extract_relevant_text(
    content,
    query,
    max_characters=MAX_EXCERPT_CHARACTERS,
):
    """
    Return a simple excerpt from the policy.

    The excerpt remains grounded entirely in the
    source policy document.
    """
    query_terms = tokenize(query)

    paragraphs = [
        paragraph.strip()
        for paragraph in re.split(
            r"\n\s*\n",
            content,
        )
        if paragraph.strip()
    ]

    if not paragraphs:
        return content[:max_characters]

    scored_paragraphs = []

    for index, paragraph in enumerate(paragraphs):
        paragraph_terms = tokenize(paragraph)

        score = len(
            query_terms.intersection(
                paragraph_terms
            )
        )

        normalized_paragraph = normalize_text(
            paragraph
        )
        normalized_query = normalize_text(
            query
        )

        if (
            normalized_query
            and normalized_query
            in normalized_paragraph
        ):
            score += 5

        scored_paragraphs.append(
            (
                score,
                -index,
                paragraph,
            )
        )

    scored_paragraphs.sort(
        key=lambda item: (
            item[0],
            item[1],
        ),
        reverse=True,
    )

    selected = []

    for (
        score,
        _,
        paragraph,
    ) in scored_paragraphs:

        if score == 0 and selected:
            break

        selected.append(paragraph)

        current_length = len(
            "\n\n".join(selected)
        )

        if current_length >= max_characters:
            break

    excerpt = "\n\n".join(selected)

    return excerpt[:max_characters]


# ============================================================
# LOAD DATA
# ============================================================

documents = load_policy_documents()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    f'<div class="main-title">📘 {APP_TITLE}</div>',
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="subtitle">{APP_SUBTITLE}</div>',
    unsafe_allow_html=True,
)

st.info(
    "This starter application is intentionally simple. "
    "You will progressively improve it throughout the "
    "Build-Along."
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.header("Build-Along")

    st.write(
        "Start with the basic policy search experience. "
        "Later milestones will introduce additional AI "
        "capabilities, evaluation, security, testing, "
        "monitoring, and governance."
    )

    st.divider()

    st.subheader("Loaded Policies")

    if documents:
        for document in documents:
            st.write(
                f"• {document['name']}"
            )
    else:
        st.warning(
            "No policy documents were found in the data folder."
        )


# ============================================================
# SEARCH INTERFACE
# ============================================================

st.subheader("Ask a Policy Question")

query = st.text_input(
    "Enter your question:",
    placeholder=(
        "Example: How much paid leave can employees take?"
    ),
)

search_button = st.button(
    "Search Policies",
    type="primary",
)


# ============================================================
# SEARCH RESULTS
# ============================================================

if search_button:

    if not query.strip():
        st.warning(
            "Enter a policy question before searching."
        )

    elif not documents:
        st.error(
            "No policy documents are available."
        )

    else:
        results = find_relevant_policies(
            query,
            documents,
        )

        if not results:
            st.warning(
                "No relevant policy was found."
            )

            st.write(
                "No sufficiently relevant policy source was "
                "identified in the available policy documents. "
                "For questions requiring organizational guidance, "
                "contact Human Resources."
            )

        else:
            st.success(
                f"Found {len(results)} potentially relevant "
                f"policy document(s)."
            )

            for result in results:

                st.markdown(
                    '<div class="policy-card">',
                    unsafe_allow_html=True,
                )

                st.subheader(
                    result["name"]
                )

                st.markdown(
                    '<div class="source-label">Source</div>',
                    unsafe_allow_html=True,
                )

                st.caption(
                    result["filename"]
                )

                excerpt = extract_relevant_text(
                    result["content"],
                    query,
                )

                st.write(excerpt)

                st.caption(
                    "Starter relevance score: "
                    f"{result['score']}"
                )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True,
                )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Student Build-Along starter. Synthetic course data only."
)