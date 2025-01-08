from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

class SkillRecommender:
    def __init__(self, data_path):
        # Read the CSV file
        self.df = pd.read_csv(data_path)
        
        # Create TF-IDF vectorizer for skill similarity
        self.vectorizer = TfidfVectorizer(stop_words='english')
        
        # Combine all text columns for better similarity matching
        self.df['combined_features'] = self.df['Skill'] + ' ' + \
                                       self.df['Related Skills'] + ' ' + \
                                       self.df['Explanation'] + ' ' + \
                                       self.df['Industry Focus']
        
        # Create TF-IDF matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['combined_features'])
        
        # Calculate similarity matrix
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

    def get_recommendations(self, input_skill):
        """Get recommendations based on input skill"""
        try:
            skill_idx = self.df[self.df['Skill'].str.lower() == input_skill.lower()].index[0]
        except IndexError:
            return "Skill not found in database"

        similarity_scores = self.similarity_matrix[skill_idx]
        similar_indices = similarity_scores.argsort()[::-1][1:4]  # Get top 3 similar skills
        
        recommendations = []
        for idx in similar_indices:
            recommendations.append({
                'Skill': self.df.iloc[idx]['Skill'],
                'Related_Skills': self.df.iloc[idx]['Related Skills'],
                'Explanation': self.df.iloc[idx]['Explanation'],
                'Popularity_Trend': self.df.iloc[idx]['Popularity Trend'],
                'Industry_Focus': self.df.iloc[idx]['Industry Focus'],
                'Resources': self.df.iloc[idx]['Resources'],
                'Similarity_Score': f"{similarity_scores[idx]:.2f}"
            })
            
        return recommendations

# Initialize the recommender
recommender = SkillRecommender('hack.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    input_skill = request.form.get('skill')
    results = recommender.get_recommendations(input_skill)
    
    if isinstance(results, str):
        return jsonify({'error': results})
    
    return jsonify({'recommendations': results})

if __name__ == '__main__':
    app.run(debug=True)
