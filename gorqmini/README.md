
# 📚 AI Exam Tutor

An AI-powered exam preparation assistant built using Python, Streamlit, and the Groq API. It helps engineering students understand concepts and prepare exam answers according to the marks allotted.

## ✨ Features

- 🤖 **AI-Powered Answers:** Generate answers using the Groq API.
- 📖 **Subject Selection:** Choose subjects such as Data Structures, Python Programming, Artificial Intelligence, Computer Networks, Java Programming, and Operating Systems.
- 📝 **Marks-Based Answers:** Generate answers suitable for 2, 5, or 10 marks.
- 📄 **PDF Study Notes:** Upload PDF notes and ask questions based on the uploaded material.
- ⚡ **Streaming Responses:** View answers as they are generated.
- 🎛️ **Creativity Control:** Adjust the creativity of AI responses.
- 💬 **Chat History:** View previous questions and answers during a conversation.
- 🆕 **New Chat:** Start a fresh conversation whenever needed.

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- PyPDF

## 📂 Project Structure

```text
gorqmini/
├── app.py
├── exam_tutor.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Install Python

Install Python on your computer if it is not already installed.

### 2. Download or Clone the Project

After uploading this project to GitHub, clone it using:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd gorqmini
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

Alternatively, download the project files from GitHub.

### 3. Install Dependencies

Open a terminal inside the project folder and run:

```bash
pip install -r requirements.txt
```

### 4. Get a Groq API Key

Create an API key through the Groq Console:

https://console.groq.com/

Keep your API key private.

### 5. Configure the API Key

In Windows PowerShell, run:

```powershell
$env:GROQ_API_KEY="your_actual_api_key"
```

Replace `your_actual_api_key` with your own API key.

Do not upload your API key to GitHub.

### 6. Run the Application

Start the Streamlit application using:

```bash
python -m streamlit run app.py
```

Open the following address in your browser:

http://localhost:8501

## 🧪 How to Use

1. Launch the application.
2. Select your subject from the sidebar.
3. Choose the required answer length: 2, 5, or 10 marks.
4. Adjust the creativity setting if needed.
5. Upload a PDF containing your study notes, if available.
6. Enter your question in the chat box.
7. Read the generated answer.
8. Start a new chat when you want to begin another topic.

## 🔐 Security

- Never share your Groq API key publicly.
- Never commit API keys, passwords, or secret files to GitHub.
- Keep private configuration files out of version control using `.gitignore`.

## 🎯 Project Objective

The objective of this project is to make exam preparation easier by providing students with subject-specific explanations, marks-based answers, and support for learning from PDF study notes.

## 👩‍💻 Author

**Chinmitha**

Engineering Student | CSE (AI & ML)

---

*Built as a learning project to explore Generative AI and API integration using Python.*
