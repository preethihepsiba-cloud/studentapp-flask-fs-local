📘 Student Management System – Flask + Firestore

Cloud-based CRUD application built using:

🐍 Flask
🔥 Google Cloud Firestore (Native Mode)
☁️ Google Cloud Platform

📌 Repository
https://github.com/preethihepsiba-cloud/studentapp-flask-fs-local

🚀 Run in Google Cloud Shell (Step-by-Step)
1️⃣ Open Cloud Shell

Go to:
Google Cloud Console → Click Cloud Shell icon (top-right)

2️⃣ Initialize gcloud
Run:
gcloud init

Follow prompts:
Select correct account
Select your project
Choose default region (if asked)

Verify:
gcloud config list

Make sure correct project is set.

3️⃣ Clone the Repository
git clone https://github.com/preethihepsiba-cloud/studentapp-flask-fs-local.git

Go inside project:
cd studentapp-flask-fs-local

4️⃣ Create Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate

5️⃣ Install Dependencies

pip install -r requirements.txt


6️⃣ Ensure Firestore Is Ready

Go to Firestore
Make sure database is created in Native Mode
Collection name should match with the name in app.py

7️⃣ Run Locally in Cloud Shell


python app.py

You will see:
Running on http://127.0.0.1:5000

📂 Project Structure
studentapp-flask-fs-local/
│
├── app.py
├── requirements.txt
└── templates/
    ├── index.html
    ├── register.html
    └── edit.html

Open:

gcloud app browse
