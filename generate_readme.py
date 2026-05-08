import os

def generate_readme():
    # 1. Header with integrated bio in the banner
    header = """<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,20&height=240&section=header&text=Aashutosh%20Kuikel&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=AI/ML%20·%20Full-Stack%20Dev%20·%20Web%20%26%20App%20Development%20·%20Cybersecurity&descAlignY=56&descAlign=50" width="100%"/>

**AI/ML · Full-Stack Dev · Web & App Development · Automation · Cybersecurity · Data Science** 📍 Kathmandu, Nepal 🇳🇵

Building intelligent products — from ML pipelines and AI automation to full-stack web apps and secure systems.
</div>

---

## 🚀 About Me
I'm a self-driven developer working across AI, full-stack development, cybersecurity, and data science. I build things that solve real problems — from training deep learning models and engineering prompts to shipping web apps and automating workflows.

- 🤖 **AI/ML** — Computer vision, NLP, deep learning, LLM fine-tuning, RAG systems
- 🌐 **Full-Stack Dev** — React, Next.js, Node.js, FastAPI, mobile apps
- ⚡ **AI Automation** — n8n, LangChain, AI agents, vibe coding, MCP
- 🔐 **Cybersecurity** — Ethical hacking, network security, secure coding
"""

    # 2. Tree Structure for Organizations
    tree_structure = """
## 🌳 Organization & Project Guide
A structural overview of my repositories and their focus areas:

```text
ak-Machine_Learning/ (Primary Org)
├── 🧠 Deep-Learning-Collections  # CNNs, Sentiment Analysis, Doodle Recognition
├── 🤖 AI-Orchestration          # LangChain, AI Agents, Automation workflows
└── 📊 Data-Science-Lab          # Predictive modeling & Analysis scripts

aKmsdfhjb/ (Personal Profile)
├── 📱 StudyFlow                 # Android APK, Productivity & Calendar App
├── 🛠️ Poem-PIN-Extractor        # General Utility & Automation tool
└── 🌐 Portfolio-V3              # Next.js Full-Stack Web Application
```
"""

    # 3. Certifications Table
    certs = """
## 📜 Certifications & Learning

| Issuer | Certification / Course | Status |
|--------|-----------------------|--------|
| Google | Google Certifications | ✅ Completed |
| Kaggle | Intro to Machine Learning | ✅ Completed |
| Harvard | CS50's Intro to Cybersecurity | ✅ Completed |
| NVIDIA | NCA — AI Infrastructure | ⏳ In Progress |
| FCC | Full-Stack Developer | ⏳ In Progress |
"""

    # 4. Tech Stack Badges
    tech_stack = """
## 🛠️ Tech Stack
**AI/ML & Data:** `Python`, `TensorFlow`, `PyTorch`, `Scikit-Learn`, `Pandas`, `OpenCV`, `HuggingFace`  
**Web & App:** `React`, `Next.js`, `Node.js`, `FastAPI`, `TailwindCSS`, `PostgreSQL`, `MongoDB`  
**Tools & Cloud:** `Docker`, `Jenkins`, `AWS`, `Git`, `n8n`, `LangChain`, `Ollama`
"""

    # 5. Stats Section
    stats = """
## 📊 GitHub Ecosystem
<div align="center">
<img src="https://github-readme-stats.vercel.app/api?username=aKmsdfhjb&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=aKmsdfhjb&theme=tokyonight&hide_border=true&layout=compact" />
</div>

<div align="center">
<img src="https://github-profile-trophy.vercel.app/?username=aKmsdfhjb&theme=tokyonight&no-frame=true&no-bg=true&margin-w=4&row=1" />
</div>

---
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,20&height=100&section=footer" width="100%"/>
</div>
"""

    full_content = header + tree_structure + certs + tech_stack + stats

    # Create profile directory if not exists
    if not os.path.exists("profile"):
        os.makedirs("profile")

    with open("profile/README.md", "w", encoding="utf-8") as f:
        f.write(full_content)
    
    print("README.md has been successfully generated in the profile/ directory.")

if __name__ == "__main__":
    generate_readme()
