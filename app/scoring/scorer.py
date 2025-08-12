from typing import List, Dict
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Scorer:
    def __init__(self):
        # Download required NLTK resources
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('corpora/stopwords')
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('punkt')
            nltk.download('stopwords')
            nltk.download('wordnet')
        
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.tfidf_vectorizer = TfidfVectorizer()
    
    def preprocess_text(self, text: str) -> str:
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters
        text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stop words and lemmatize
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        
        # Join tokens back into text
        preprocessed_text = ' '.join(tokens)
        
        return preprocessed_text

    def calculate_score(self, job_description: str, resume: str) -> float:
        # Preprocess texts
        job_processed = self.preprocess_text(job_description)
        resume_processed = self.preprocess_text(resume)
        
        # Create TF-IDF vectors
        tfidf_matrix = self.tfidf_vectorizer.fit_transform([job_processed, resume_processed])
        
        # Calculate cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        
        # Scale to percentage
        score = similarity * 100
        
        return score

    def extract_skills(self, text: str, skill_keywords: List[str]) -> List[str]:
        """Extract skills from text based on a predefined list of skill keywords"""
        found_skills = []
        text_lower = text.lower()
        
        for skill in skill_keywords:
            if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text_lower):
                found_skills.append(skill)
        
        return found_skills

    def score_by_category(self, job_description: str, resume: str, categories: Dict[str, List[str]]) -> Dict[str, float]:
        """Score resume against job description by category (skills, education, experience)"""
        category_scores = {}
        
        for category, keywords in categories.items():
            category_matches = 0
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword.lower()) + r'\b', resume.lower()):
                    category_matches += 1
            
            category_score = (category_matches / len(keywords)) * 100 if keywords else 0
            category_scores[category] = category_score
        
        return category_scores

    def score_candidates(self, job_description: str, resumes: List[str]) -> Dict[int, float]:
        scores = {}
        for i, resume in enumerate(resumes):
            score = self.calculate_score(job_description, resume)
            scores[i] = score
        return scores