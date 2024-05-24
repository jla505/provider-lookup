from flask import Flask, request, render_template

app = Flask(__name__)

# Sample data for healthcare providers
providers = [
    {'name': 'Dr. John Smith', 'specialty': 'Cardiologist', 'location': 'Vancouver'},
    {'name': 'Dr. Jane Doe', 'specialty': 'Dermatologist', 'location': 'Vancouver'},
    {'name': 'Dr. Emily Davis', 'specialty': 'Neurologist', 'location': 'Toronto'},
    {'name': 'Dr. Michael Brown', 'specialty': 'Pediatrician', 'location': 'Montreal'},
    {'name': 'Dr. Sarah Wilson', 'specialty': 'Orthopedic', 'location': 'Vancouver'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        name = request.form.get('name', '').lower()
        specialty = request.form.get('specialty', '').lower()
        location = request.form.get('location', '').lower()

        # Filter providers based on search criteria
        results = [
            provider for provider in providers
            if (name in provider['name'].lower() or not name) and
               (specialty in provider['specialty'].lower() or not specialty) and
               (location in provider['location'].lower() or not location)
        ]

        return render_template('results.html', providers=results)

    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
