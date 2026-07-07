from flask import Flask, render_template, request, jsonify, session
from agents.advisor import AdvisorAgent
from agents.crop_analysis import CropAnalysisAgent
from agents.planner import PlannerAgent
from agents.research import ResearchAgent
import os
import json
import webbrowser
import threading
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Initialize agents
advisor = AdvisorAgent()
crop_analyzer = CropAnalysisAgent()
planner = PlannerAgent()
researcher = ResearchAgent()

# History storage (in production, use a database)
if not os.path.exists('history.json'):
    with open('history.json', 'w') as f:
        json.dump([], f)

def save_to_history(query_type, query, response):
    """Save queries to history"""
    history = []
    try:
        with open('history.json', 'r') as f:
            history = json.load(f)
    except:
        pass
    
    history.append({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'type': query_type,
        'query': query,
        'response': response[:200] + '...' if len(response) > 200 else response
    })
    
    with open('history.json', 'w') as f:
        json.dump(history[-50:], f)  # Keep last 50 entries

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crop-analysis', methods=['GET', 'POST'])
def crop_analysis():
    if request.method == 'POST':
        crop = request.form.get('crop')
        soil = request.form.get('soil')
        location = request.form.get('location')
        season = request.form.get('season')
        
        if not all([crop, soil, location, season]):
            return jsonify({'error': 'Please fill all fields'}), 400
        
        response = crop_analyzer.analyze(crop, soil, location, season)
        
        # Save to history
        save_to_history('crop_analysis', 
                       f'Crop: {crop}, Soil: {soil}, Location: {location}, Season: {season}', 
                       response)
        
        return render_template('crop_analysis.html', response=response, 
                              crop=crop, soil=soil, location=location, season=season)
    
    return render_template('crop_analysis.html')

@app.route('/advisor', methods=['GET', 'POST'])
def advisor_page():
    if request.method == 'POST':
        crop = request.form.get('crop')
        problem = request.form.get('problem')
        
        if not all([crop, problem]):
            return jsonify({'error': 'Please fill all fields'}), 400
        
        response = advisor.diagnose(crop, problem)
        
        # Save to history
        save_to_history('advisor', f'Crop: {crop}, Problem: {problem}', response)
        
        return render_template('advisor.html', response=response, 
                              crop=crop, problem=problem)
    
    return render_template('advisor.html')

@app.route('/planner', methods=['GET', 'POST'])
def planner_page():
    if request.method == 'POST':
        goal = request.form.get('goal')
        
        if not goal:
            return jsonify({'error': 'Please describe your goal'}), 400
        
        response = planner.create_plan(goal)
        
        # Save to history
        save_to_history('planner', f'Goal: {goal}', response)
        
        return render_template('planner.html', response=response, goal=goal)
    
    return render_template('planner.html')

@app.route('/research', methods=['GET', 'POST'])
def research_page():
    if request.method == 'POST':
        question = request.form.get('question')
        
        if not question:
            return jsonify({'error': 'Please enter a question'}), 400
        
        response = researcher.research(question)
        
        # Save to history
        save_to_history('research', f'Question: {question}', response)
        
        return render_template('research.html', response=response, question=question)
    
    return render_template('research.html')

@app.route('/history')
def history():
    history = []
    try:
        with open('history.json', 'r') as f:
            history = json.load(f)
    except:
        pass
    return render_template('history.html', history=history)

@app.route('/clear-history', methods=['POST'])
def clear_history():
    with open('history.json', 'w') as f:
        json.dump([], f)
    return jsonify({'success': True})

# Function to open browser
def open_browser():
    """Open browser after server starts"""
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Open browser after 1.5 seconds
    threading.Timer(1.5, open_browser).start()
    
    # Run the app
    app.run(debug=True, host='127.0.0.1', port=5000)