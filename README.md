# 🧠 MyCloudAI — Personalized AI Assistant with Private Cloud Automation

**MyCloudAI** is a self-hosted, privacy-first AI assistant that runs entirely on your own laptop or desktop. It uses a local Large Language Model (LLM) like Mistral or Phi-3 to understand and execute natural language commands — such as opening apps, managing calendar events, or summarizing notes — all without sending your data to external servers.

---

## 🔑 Key Features

| Feature | Description |
|--------|-------------|
| 🔒 100% Privacy | Runs completely on your machine, no cloud APIs or data sharing |
| 🤖 Personalized LLM | Choose or fine-tune your own LLM (e.g., Mistral, Phi-3) |
| 🧩 App Automation | Automate tasks like opening files, sending messages, launching software |
| 📱 Cross-Device Access | Connect from mobile via browser or Termux |
| 🗃️ Memory System (Optional) | Store past conversations and context locally |
| ⚙️ Modular Architecture | Easy to expand with APIs, scripts, or IoT control |
| 🛠️ Built with Python | Open and customizable source code for any platform |

---

## 🧠 Example Use Cases

> ✅ “Open WhatsApp and say ‘On my way’ to Mom”  
> ✅ “Remind me tomorrow at 10AM to call John”  
> ✅ “List all PDF files in the Downloads folder”  
> ✅ “Summarize notes.txt and email it to me”  
> ✅ “Play the latest trailer of a Marvel movie”

---

## 📁 Project Structure

```
MyCloudAI/
├── llm_backend/              # Load and query the local LLM
│   └── model_loader.py
├── automation/               # Scripts for file/app control
│   └── file_opener.py
├── memory/                   # Store context or history (optional)
│   └── memory_store.py
├── api/                      # Flask or FastAPI server
│   └── main.py
├── assets/                   # Icons, sounds, avatars (optional)
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/MyCloudAI.git
cd MyCloudAI
```

### 2. Set up virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run your local LLM
You can use `transformers` to run Mistral, Phi-3, or any other HuggingFace-supported model.

```python
from llm_backend.model_loader import LLMEngine

llm = LLMEngine()
response = llm.query("What's the weather?")
print(response)
```

### 5. Start the API (optional)
```bash
cd api
uvicorn main:app --reload
```

---

## 📦 Dependencies

- `transformers`
- `torch`
- `uvicorn`
- `fastapi` or `flask`
- `python-dotenv`
- `termcolor` (optional)

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more info.

---

## ❤️ Contribute

Pull requests are welcome! If you want to suggest improvements, new integrations, or help expand this into a more advanced AI assistant, feel free to fork and contribute.

---

## 🙋 Support

Need help or want to showcase your own MyCloudAI setup?  
Open an issue or reach out on [GitHub Discussions](https://github.com/yourusername/MyCloudAI/discussions).

---