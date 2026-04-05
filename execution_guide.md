# 🚀 Execution Guide: SecureFlow AI

To execute and interact with the **AI-Driven Encrypted Traffic Classifier**, follow the steps below based on which part of the system you'd like to use.

---

## 🎨 1. How to View the SOC Dashboard (Web UI)
The dashboard displays real-time monitoring and security alerts in your browser.

1.  **Open the Workspace**: Navigate to the folder:  
    `c:\Users\Vanjikumar\OneDrive\Desktop\tools docx\projects\AI-Driven Encrypted Traffic Classifier\`
2.  **Launch the Dashboard**: Double-click on the `index.html` file to open it in your web browser (Chrome, Edge, or Firefox).
3.  **Interaction**:
    *   **Live Traffic**: Monitor the scrolling traffic chart.
    *   **Alert Selection**: Click any row in the **"Recent Security Alerts"** table to view detailed flow forensics in the **"Threat Inspection"** panel.
    *   **Sidebar**: Toggle between Dashboard, Live Traffic, and Alerts views.

---

## 🧠 2. How to Run the AI Classifier (Machine Learning)
You can train and test the model using the Python backend script.

### 📋 Prerequisites
Ensure the following Python libraries are installed:
```powershell
pip install pandas numpy scikit-learn joblib
```

### ⚙️ Running the Model
Open a terminal in the project directory and run:
```powershell
python train_model.py
```

### 📊 Expected Output
When you run the command, the system will:
1.  **Generate Synthetic Data**: Create flow metadata like Flow Duration, Packet Counts, and IAT.
2.  **Train the Model**: Use a Random Forest classifier.
3.  **Display Accuracy**: View the classification report (Accuracy is typically ~99%).
4.  **Save the Model**: Output a `secureflow_model.pkl` file (this stores the "brain" of the AI).
5.  **Test Prediction**: Show a live sample classification of a suspicious encrypted flow.

---

## 📂 Project Structure Overview
-   **`index.html`**: The UI entry point.
-   **`style.css`**: The enterprise-grade dark theme styles.
-   **`main.js`**: Controls dashboard dynamics.
-   **`train_model.py`**: The AI training and prediction engine.
-   **`secureflow_model.pkl`**: The trained AI weight file (generated after running the script).

> [!NOTE]
> The current system uses a synthetic traffic generator for demonstration. In a production environment, you would feed real PCAP files or CSV metadata (like CIC-IDS2017) into the `train_model.py` script.
