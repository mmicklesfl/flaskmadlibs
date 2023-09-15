from flask import Flask, render_template, request
from stories import story, frankenstein, trick_or_treat, haunted_house

app = Flask(__name__)

stories = {
    'original': story,
    'frankenstein': frankenstein,
    'trick_or_treat': trick_or_treat,
    'haunted_house': haunted_house
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        story_type = request.form['story_type']
        selected_story = stories[story_type]
        answers = {key: request.form[key] for key in selected_story.prompts}
        return render_template('story.html', text=selected_story.generate(answers))
    return render_template('form.html', stories=stories)

@app.route('/select-story', methods=['POST'])
def select_story():
    story_type = request.form['story_type']
    selected_story = stories[story_type]
    return render_template('form.html', stories=stories, selected_story=selected_story, selected_story_key=story_type)

if __name__ == '__main__':
    app.run(debug=True)
