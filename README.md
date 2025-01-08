# Skill-mate

SkillMate
SkillMate is a web-based skill recommendation system that helps users discover relevant skills based on their input. The project uses a Flask-based backend with a machine learning model for skill similarity and a simple HTML/CSS/JavaScript frontend.

Features
Search for a skill: Enter a skill name to get recommendations.
Skill similarity analysis: Uses TF-IDF and cosine similarity to find the most relevant skills.
Skill details: Displays related skills, explanations, industry focus, popularity trends, and recommended resources.
User-friendly interface: A minimalistic and responsive UI.
Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)
Machine Learning: Scikit-learn (TF-IDF, Cosine Similarity)
Data Storage: CSV file (hack.csv)
Installation
Prerequisites
Python 3.x
Flask
Pandas
Scikit-learn
Setup
Clone the repository:
git clone https://github.com/yourusername/SkillMate.git
cd SkillMate
Install dependencies:
pip install flask pandas scikit-learn
Run the application:
python app.py
Open your browser and go to:
http://127.0.0.1:5000/
Project Structure
SkillMate/
│-- static/              # CSS/JS files (if applicable)
│-- templates/
│   ├── index.html       # Frontend UI
│-- hack.csv             # Dataset containing skills information
│-- app.py               # Flask application
│-- README.md            # Project documentation
API Endpoint
/recommend (POST)
Request:
skill: The skill name entered by the user.
Response:
JSON containing top recommended skills and related information.
Example Usage
curl -X POST -d "skill=Data Science" http://127.0.0.1:5000/recommend
Future Improvements
Expand dataset for better recommendations.
Implement a database (SQLite or PostgreSQL) for scalability.
Improve frontend with React or Vue.js.
Add user authentication for personalized recommendations.
License
This project is licensed under the MIT License.

Contributing
Feel free to contribute by forking the repository and submitting pull requests! Add your details and information........
