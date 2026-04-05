import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

class SecureFlowAIModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.features = [
            'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
            'Fwd Packet Length Max', 'Fwd Packet Length Min', 'Bwd Packet Length Max',
            'Flow Bytes/s', 'Flow Packets/s', 'Flow IAT Mean', 'Fwd IAT Total'
        ]

    def generate_dummy_data(self, samples=1000):
        """Generates synthetic data for demonstration since CSV is not yet provided."""
        np.random.seed(42)
        data = pd.DataFrame(np.random.rand(samples, len(self.features)), columns=self.features)
        
        # Simple logical rules for labels to make it learnable
        # Normal traffic: short duration, low packet count
        # Malicious: high duration or high volume
        data['Label'] = 0 # Benign
        data.loc[(data['Flow Duration'] > 0.8) | (data['Total Fwd Packets'] > 0.8), 'Label'] = 1 # Malicious
        
        return data

    def train(self, data=None):
        if data is None:
            print("No data provided. Generating synthetic training data...")
            data = self.generate_dummy_data()
        
        X = data[self.features]
        y = data['Label']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print(f"Training on {len(X_train)} samples...")
        self.model.fit(X_train, y_train)
        
        y_pred = self.model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"Model Training Complete. Accuracy: {acc * 100:.2f}%")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        # Save model
        joblib.dump(self.model, 'secureflow_model.pkl')
        print("Model saved to secureflow_model.pkl")

    def predict(self, feature_values):
        """
        Predict traffic type.
        feature_values: list or numpy array of values matching self.features
        """
        if not os.path.exists('secureflow_model.pkl'):
            self.train()
            
        model = joblib.load('secureflow_model.pkl')
        prediction = model.predict([feature_values])
        return "Malicious" if prediction[0] == 1 else "Benign"

if __name__ == "__main__":
    sf_ai = SecureFlowAIModel()
    sf_ai.train()
    
    # Test a sample prediction
    sample_input = [0.9, 0.5, 0.2, 0.8, 0.1, 0.9, 0.5, 0.2, 0.1, 0.9] # Likely malicious
    result = sf_ai.predict(sample_input)
    print(f"\nSample Prediction for High Flow Input: {result}")
