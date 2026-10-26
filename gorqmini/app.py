
import streamlit as st
from groq import Groq
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Exam Tutor",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI Exam Tutor")
st.caption("Your personal AI tutor for engineering exam preparation")

# Connect to Groq
try:
    client = Groq()
except Exception:
    st.error(
        "Groq API key not found. Set GROQ_API_KEY "
        "in your terminal and restart the app."
    )
    st.stop()


# Initialize chat
def start_new_chat():
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a friendly AI exam tutor for engineering students. "
                "Explain concepts in simple English. Adapt answers to the "
                "marks specified by the student: 2 marks means a short answer, "
                "5 marks means a medium answer with key points, and 10 marks "
                "means a detailed, well-structured answer. Use uploaded study "
                "notes as the main source when provided. Do not invent "
                "citations. If the notes do not contain the answer, say so "
                "and clearly distinguish general knowledge from the notes."
            )
        }
    ]


if "messages" not in st.session_state:
    start_new_chat()


# Sidebar settings
st.sidebar.header("⚙️ Study Settings")

subject = st.sidebar.selectbox(
    "Choose your subject",
    [
        "Data Structures",
        "Python Programming",
        "Artificial Intelligence",
        "Computer Networks",
        "Java Programming",
        "Operating Systems",
        "Other"
    ]
)

if subject == "Other":
    custom_subject = st.sidebar.text_input(
        "Enter your subject",
        placeholder="e.g. Engineering Mathematics"
    )
    selected_subject = custom_subject.strip() or "General Studies"
else:
    selected_subject = subject

marks = st.sidebar.selectbox(
    "Answer length",
    [2, 5, 10],
    format_func=lambda x: f"{x} marks"
)

temperature = st.sidebar.slider(
    "Creativity",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    step=0.1
)

st.sidebar.divider()

# PDF upload
st.sidebar.subheader("📄 Study Notes")

uploaded_file = st.sidebar.file_uploader(
    "Upload your notes (PDF)",
    type=["pdf"]
)

pdf_text = ""

if uploaded_file is not None:
    try:
        reader = PdfReader(uploaded_file)

        pdf_text = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )

        if pdf_text.strip():
            st.sidebar.success("PDF uploaded successfully!")
            st.sidebar.caption(
                f"{len(reader.pages)} pages detected"
            )
        else:
            st.sidebar.warning(
                "No selectable text found. This PDF may be scanned."
            )

    except Exception as error:
        st.sidebar.error(f"Could not read PDF: {error}")


# Chat controls
if st.sidebar.button("🆕 New Chat", use_container_width=True):
    start_new_chat()
    st.rerun()

if st.sidebar.button("🗑️ Clear Chat", use_container_width=True):
    start_new_chat()
    st.rerun()


# Display previous messages
for message in st.session_state.messages:
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Ask a question
question = st.chat_input(
    "Ask a question about your subject..."
)

if question:
    if selected_subject == "General Studies":
        st.warning("Choose a subject or enter your subject in the sidebar.")
    else:
        # Keep the displayed question separate from the full AI prompt
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        notes = pdf_text[:18000]

        user_prompt = f"""
Subject: {selected_subject}

Student's question:
{question}

Required answer length: {marks} marks.

Instructions:
- Answer specifically for the selected subject.
- Use simple English suitable for an engineering student.
- For 2 marks, give a concise definition or direct answer.
- For 5 marks, include an explanation and important points.
- For 10 marks, include a detailed, structured answer with examples
  where useful.
- Use headings, numbered steps, or bullet points when appropriate.
- If study notes are provided, use them as the main reference.
- Never claim that something is in the notes unless it actually is.

Study notes:
{notes if notes.strip() else "No PDF notes uploaded. Answer using your general knowledge."}
"""

        # Send the question to Groq and stream the answer
        with st.chat_message("assistant"):
            answer_placeholder = st.empty()
            full_answer = ""

            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        *st.session_state.messages[:-1],
                        {
                            "role": "user",
                            "content": user_prompt
                        }
                    ],
                    temperature=temperature,
                    max_completion_tokens=2048,
                    stream=True
                )

                for chunk in response:
                    content = chunk.choices[0].delta.content

                    if content:
                        full_answer += content
                        answer_placeholder.markdown(full_answer + "▌")

                answer_placeholder.markdown(full_answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_answer
                })

            except Exception as error:
                st.error(f"Something went wrong: {error}")

                # Remove the unanswered question from chat history
                st.session_state.messages.pop()
