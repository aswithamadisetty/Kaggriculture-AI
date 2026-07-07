# 🌾 Kaggriculture-AI

> Multi-Agent AI System for Intelligent Agricultural Assistance

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![AI Agents](https://img.shields.io/badge/Multi-Agent%20AI-green)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 📖 Overview

Kaggriculture-AI is a **Multi-Agent AI agricultural assistant** designed to help farmers, agricultural students, and researchers make better farming decisions using Generative AI.

Instead of relying on a single AI model, the application routes requests to specialized AI agents, each responsible for a different agricultural task.

The system provides:

- 🌱 Crop recommendations
- 📅 Farming planning
- 🔬 Agricultural research
- 👨‍🌾 Personalized farming advice

---

# 🚀 Features

## 🌾 Advisor Agent
Provides personalized agricultural guidance including:

- Crop recommendations
- Fertilizer suggestions
- Irrigation advice
- Soil management tips
- Best farming practices

---

## 🌿 Crop Analysis Agent

Analyzes crop-related questions such as:

- Crop suitability
- Seasonal recommendations
- Growth stages
- Plant health guidance
- Yield improvement suggestions

---

## 📅 Planner Agent

Creates structured farming plans including:

- Seasonal crop plans
- Sowing schedules
- Irrigation planning
- Harvest timelines
- Farming activity planning

---

## 🔬 Research Agent

Performs agricultural research by providing:

- Scientific farming information
- Sustainable agriculture practices
- Pest management knowledge
- Organic farming guidance
- Latest agricultural techniques

---

# 🧠 Multi-Agent Workflow

```
                User Query
                     │
                     ▼
            Flask Web Application
                     │
                     ▼
          Intelligent Request Router
                     │
     ┌─────────┬─────────┬─────────┬─────────┐
     ▼         ▼         ▼         ▼
 Advisor    Planner   Crop AI   Research AI
     │         │         │         │
     └─────────┴─────────┴─────────┘
                     │
                     ▼
             Combined AI Response
                     │
                     ▼
                  User
```

---

# 🏗️ Project Structure

```
Kaggriculture-AI/
│
├── agents/
│   ├── advisor.py
│   ├── planner.py
│   ├── crop_analysis.py
│   ├── research.py
│
├── config/
│   └── gemini.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── index.html
│
├── main.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Technologies Used

- Python
- Flask
- Google Gemini API
- HTML
- CSS
- JavaScript
- Jinja Templates

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/aswithamadisetty/Kaggriculture-AI.git
```

Go inside the project

```bash
cd Kaggriculture-AI
```

Create a virtual environment

Windows

```bash
python -m venv .venv
```

Activate it

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure API Key

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your Google Gemini API key.

---

# ▶️ Run the Project

```bash
python main.py
```

or

```bash
flask run
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 💬 Example Queries

Advisor Agent

```
Which crop is suitable for black soil?
```

Planner Agent

```
Create a cultivation plan for potato during winter.
```

Crop Analysis Agent

```
How can I improve tomato yield?
```

Research Agent

```
Explain sustainable agriculture practices.
```

---

# 🌍 Real-World Impact

Kaggriculture-AI can help:

- Farmers
- Agricultural students
- Researchers
- Farming consultants
- Extension officers

Benefits include:

- Better farming decisions
- Time-saving recommendations
- Easy access to agricultural knowledge
- AI-assisted crop planning

---

# 🔮 Future Improvements

- Weather API integration
- Satellite image analysis
- Crop disease detection
- Voice assistant
- Regional language support
- Market price prediction
- Fertilizer optimization
- IoT sensor integration

---

# 📸 Screenshots

Add screenshots here after running the application.

```
screenshots/
    home.png
    advisor.png
    planner.png
    crop_analysis.png
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Aswitha Madisetty**

B.Tech (Computer Science Engineering in Artificial Intelligence)

Vasireddy Venkatadri Institute of Technology (VVIT)

---

# ⭐ Acknowledgements

- Google Gemini
- Flask
- Python
- Kaggle AI Agents Intensive Vibe Coding Capstone
- Open Source Community

---

If you found this project useful, don't forget to ⭐ the repository.
