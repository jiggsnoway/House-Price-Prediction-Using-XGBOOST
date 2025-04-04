🏠 House Price Prediction API

A Machine Learning project to predict house prices using XGBoost, deployed with FastAPI.

The model was trained using a real-world housing dataset and provides predictions based on features like number of rooms, population, and location-based metrics.

📌 Project Overview
This project is divided into two major parts:

Model Training
Done using Python in Google Colab

Trained with XGBoost Regressor

File: house_price_model.ipynb

Output: trained_model.pkl

Model Deployment:
Built with FastAPI

Serves predictions via a simple API

File: main.py

📊 Dataset Features
The model takes the following input features:

Feature	Description:

MedInc

HouseAge

AveRooms

AveBedrms

Population

AveOccup

Latitude

Longitude	

🚀 How to Run Locally
1. Clone the Repository
git clone https://github.com/your_username/house-price-predictor.git
cd house-price-predictor

2. Install Dependencies
pip install -r requirements.txt

3. Run the FastAPI App
uvicorn main:app --reload

4. Try It Out 🚀
Visit the interactive Swagger UI at:
🔗 http://127.0.0.1:8000/docs

🔍 Example API Usage
Input (via Swagger or Python):

{
  "features": [4.0368, 52.0, 4.761658, 1.103627, 413.0, 2.139896, 37.85, -122.25]
}
Output:

{
  "predicted_price": 184569.87
}


📁 Project Structure

house-price-predictor/
│
├── main.py                  
├── trained_model.pkl        
├── requirements.txt         
├── README.md                
└── house_price_model.ipynb  


📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and share with credit.

🙋‍♀️ Author
Jigyashman Hazarika


Student | ML Enthusiast | FastAPI Learner


📫 Feel free to connect with me!
