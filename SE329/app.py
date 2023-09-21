from flask import Flask, render_template

app = Flask(__name__)

# Define routes for the home page and individual service pages
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/services/paid/venue_rental')
def venue_rental():
    return render_template('venue_rental.html')

@app.route('/services/paid/catering')
def catering():
    return render_template('catering.html')

@app.route('/services/free/spanish')
def spanish():
    return render_template('spanish.html')

@app.route('/services/external/home_care')
def home_care():
    return render_template('home_care.html')

# Add more routes for other services as needed
@app.route('/services/paid/venue_rental/weddings')
def weddings():
    return render_template('weddings.html')

@app.route('/services/paid/venue_rental/community_meetings')
def community_meetings():
    return render_template('community_meetings.html')

@app.route('/services/paid/venue_rental/funerals')
def funerals():
    return render_template('funerals.html')

@app.route('/services/free/arts_and_crafts')
def arts_and_crafts():
    return render_template('arts_and_crafts.html')

@app.route('/services/free/painting_classes')
def painting_classes():
    return render_template('painting_classes.html')

@app.route('/services/external/home_care/elderly_and_handicapped')
def elderly_and_handicapped():
    return render_template('elderly_and_handicapped.html')


if __name__ == '__main__':
    app.run(debug=True)
