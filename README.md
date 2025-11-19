# 🌍 FoodBridge Agent System  
### An AI-Powered Surplus Food Redistribution Agent | Kaggle x Google Capstone (Agents for Good)

FoodBridge is an AI-based agent system built using Google’s Agent Development Kit (ADK).  
Its goal is to reduce urban food waste by connecting surplus food providers with NGOs and community food programs in an automated, intelligent, and transparent way.

This repository contains the full code, notebook, and project documentation created for the **Kaggle x Google Developers: Capstone Project – Agents For Good Track**.

---

# 🚀 Project Objective

Every day, restaurants and kitchens generate surplus food that often goes to waste.  
At the same time, NGOs struggle to find enough food for people in need.

FoodBridge acts as a bridge between the two by:

- Detecting surplus food reports  
- Matching them with appropriate NGOs  
- Suggesting basic logistics  
- Estimating social impact  
- Maintaining traceable logs  

The project demonstrates how AI agents can help solve a real social problem.

---

# 🧠 System Architecture Overview

FoodBridge is built as a modular, multi-agent system:

### **1. Surplus Intake Agent**
Extracts food details such as type, quantity, and pickup location.

### **2. NGO Matching Agent**
Suggests suitable NGOs based on:
- food type  
- quantity  
- availability  
- simple location rules  

### **3. Logistics Agent (Basic Version)**
Provides a simple delivery or pickup suggestion and ETA estimate.

### **4. Impact Estimation Agent**
Calculates potential meals saved and waste prevented.

### **5. Orchestrator**
Coordinating agent that executes all the above steps in order and returns structured results.

This makes the pipeline clear, interpretable, and easily extendable.

---

# 🔧 Technologies Used

- **Python**  
- **Google Agent Development Kit (ADK)**  
- **Kaggle Notebook environment**  
- **JSON event workflows**  
- **Rule-based reasoning + LLM guidance**  

---

# 📁 Repository Structure
FoodBridge-Agent-System/
│── README.md
│── FoodBridge_Notebook.ipynb
│── src/
│     ├── donor_agent.py
│     ├── ngo_matching_agent.py
│     ├── logistics_agent.py
│     └── impact_agent.py
│── assets/
      └── architecture.png



Notes:
- The `.py` files are optional placeholders for modularization.
- The main working system is inside the Kaggle Notebook.

---

# 🧪 Agent Testing & Verification

The notebook includes a **Testing Section** that demonstrates:

### ✔ Basic Pipeline Test  
Ensures the entire agent flow runs correctly.

### ✔ Multiple Scenario Test  
Checks if different inputs produce appropriate NGO matches.

### ✔ Edge Case Test  
Tests incorrect, incomplete, or unclear inputs (no crashes).

### ✔ Performance Test  
Runs the system multiple times to evaluate stability.

### ✔ Latency Measurement  
Provides an estimate of response time per request.

Judges and contributors can run these cells directly to evaluate the system’s behavior.

---

# ⚙️ How to Run the Project

### **Option 1: Kaggle Notebook (Recommended)**  
Open the notebook → Click **Run All**  
This will execute the full agent pipeline with logs.

### **Option 2: Local Environment**
Install dependencies:
Then open the notebook in Jupyter or VS Code.

---

# 🔮 Future Enhancements

FoodBridge is designed with scalability in mind. Potential next steps:

- Real geolocation-based routing (Maps API)  
- Volunteer dispatching system  
- Live NGO availability tracking  
- Multi-agent parallel processing  
- Dedicated web/mobile interface  
- Deployment on Google Vertex AI Agent Engine  

---

# 🙌 Acknowledgements

This project was built as part of the **Kaggle x Google Developers – Agent Development Kit Capstone**.  
Special thanks to:

- Google ADK Team  
- Kaggle Community  
- Open-source contributors  
- Everyone working toward reducing food waste  

---

# 📜 License

This project is open for educational and research purposes.  
You are free to fork, improve, and extend the system.



