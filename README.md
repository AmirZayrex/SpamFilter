# 📧 Spam Message Detector

A machine learning-based spam detection web application built with **Naive Bayes** and **TF-IDF**.

---

## 🎯 Features
- Detects spam messages with **97% accuracy**
- Web-based user interface via **Flask**
- Real-time text analysis and result display
- Standalone executable (`exe`) available for **macOS (ARM64)**
- Clean, modular project architecture

---

## 🛠 Tech Stack
- **Language:** Python 3.10
- **Core Libraries:** scikit-learn, NLTK, Flask, pandas
- **Packaging:** PyInstaller
- **Model:** Multinomial Naive Bayes + TF-IDF
- **Web Deployment:** Liara (Iranian Cloud Platform)

---


📦 Executable File (End User)
Navigate to the dist/ folder.
Double-click SpamFilter.
Open your browser and go to http://127.0.0.1:8080.
Alternatively, double-click run_spamfilter.command from the project root.

---

📊 Model Evaluation
Accuracy: 97%
Precision (Spam): 100%
Recall (Spam): 77%
Confusion Matrix: [[966, 0], [34, 115]]

---

AmirHooshang Amirjani
AI Engineering Student