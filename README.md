# ⚡ Smart Electricity Bill Predictor

An AI-powered web application that predicts monthly electricity bills using Machine Learning and Random Forest Regression.

---

# 📌 Project Overview

This project predicts electricity bills based on household appliance usage.

The application uses:

* Python
* Machine Learning
* Random Forest Regression
* Streamlit

Users can enter appliance usage details such as:

* Units consumed
* Lights
* Fans
* AC usage
* TV usage
* Fridge count
* Washing machine usage
* Inverter availability
* Geyser usage
* Season

The AI model predicts the estimated monthly electricity bill.

---

# 🚀 Features

✅ 5000 realistic dataset records
✅ Random Forest Machine Learning model
✅ Modern Streamlit web interface
✅ Multiple appliance support
✅ Seasonal electricity prediction
✅ Bill usage category detection
✅ Realistic Indian EB slab logic

---

# 🛠 Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| Pandas       | Data Processing      |
| NumPy        | Numerical Operations |
| Scikit-learn | Machine Learning     |
| Streamlit    | Web Application      |
| OpenPyXL     | Excel File Handling  |

---

# 🧠 Machine Learning Model

Algorithm Used:

## Random Forest Regressor

Type:

## Supervised Learning → Regression

The model learns electricity consumption patterns and predicts monthly electricity bills.

---

# 📂 Project Structure

```text
Smart_Electricity_Bill_Predictor
│
├── dataset.py
├── train_model.py
├── app.py
├── model.pkl
├── requirements.txt
└── electricity_bill_dataset_5000.xlsx
```

---

# ▶️ How to Run the Project

## 1. Install Libraries

```bash
pip install -r requirements.txt
```

---

## 2. Generate Dataset

```bash
python dataset.py
```

---

## 3. Train Model

```bash
python train_model.py
```

---

## 4. Run Streamlit App

```bash
streamlit run app.py
```

---

# 📊 Input Features

* Units Consumed
* Number of Lights
* Light Usage Hours
* Number of Fans
* Fan Usage Hours
* Number of ACs
* AC Usage Hours
* Fridge Count
* TV Count
* TV Usage Hours
* Washing Machine Count
* Washing Machine Usage Hours
* Inverter Availability
* Geyser Count
* Geyser Usage Hours
* Season

---

# 🎯 Output

The application predicts:

## Estimated Monthly Electricity Bill

It also classifies usage into:

* Low Usage
* Medium Usage
* High Usage

---

# 📈 Model Performance

* R² Score ≈ 0.93+
* MAE ≈ Low prediction error

---

# 🌐 Deployment

This project can be deployed using:

* GitHub
* Streamlit Community Cloud
* Google Colab

---

# 👨‍💻 Author

Hari Prakash

AI & Data Science Internship Project

---

# 📌 Future Improvements

* Real EB tariff integration
* Monthly usage charts
* PDF bill reports
* User authentication
* Database support
* Mobile responsive UI
* Dark mode

---

# 📜 License

This project is for educational and internship purposes.
