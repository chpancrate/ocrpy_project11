import json
import sys
from datetime import datetime
from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   flash,
                   url_for,
                   abort)


def loadClubs():
    try:
        with open('clubs.json') as clubs_file:
            list_of_clubs = json.load(clubs_file)['clubs']
    except FileNotFoundError:
        list_of_clubs = []
    except json.JSONDecodeError:
        list_of_clubs = []

    return list_of_clubs


def loadCompetitions():
    try:
        with open('competitions.json') as competitions_file:
            list_of_competitions = json.load(competitions_file)['competitions']
    except FileNotFoundError:
        list_of_competitions = []
    except json.JSONDecodeError:
        list_of_competitions = []
    return list_of_competitions


app = Flask(__name__)
import errors
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    if clubs == [] or competitions == []:
        abort(500, description="json files missing or empty")
    return render_template('index.html', clubs=clubs)


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email']
                == request.form['email']][0]
        print("XXX-today", datetime.now())

        for competition in competitions:
            competition_date = datetime.strptime(competition['date'],
                                                 "%Y-%m-%d %H:%M:%S")
            print("XXX-comp date", competition_date)
            competition['is_not_in_past'] = datetime.now() < competition_date

        return render_template('welcome.html',
                               club=club,
                               competitions=competitions)
    except IndexError:
        flash("Unknown email")
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
    except IndexError:
        # if not found we raise a page not found error
        abort(404)

    try:
        foundCompetition = [c for c in competitions if c['name']
                            == competition][0]
    except IndexError:
        # if not found we raise a page not found error
        abort(404)

    if foundClub and foundCompetition:
        return render_template('booking.html',
                               club=foundClub,
                               competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html',
                               club=club,
                               competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    try:
        competition = [c for c in competitions if c['name']
                       == request.form['competition']][0]
    except IndexError:
        # if not found we raise an internal server error
        abort(500)

    try:
        club = [c for c in clubs if c['name'] == request.form['club']][0]
    except IndexError:
        # if not found we raise an internal server error
        abort(500)

    places_required = int(request.form['places'])
    places_available = int(competition['numberOfPlaces'])
    club_points = int(club['points'])

    if places_required > club_points:
        flash("You do not have enough points.")
        return render_template('booking.html',
                               club=club,
                               competition=competition)
    elif places_required > 12:
        flash("You cannot book more than 12 places.")
        return render_template('booking.html',
                               club=club,
                               competition=competition)
    elif places_required > places_available:
        flash("There is not enough places in the competition.")
        return render_template('booking.html',
                               club=club,
                               competition=competition)

    competition['numberOfPlaces'] = (int(competition['numberOfPlaces'])
                                     - places_required)
    club['points'] = int(club['points']) - places_required
    flash('Great-booking complete!')

    return render_template('welcome.html',
                           club=club,
                           competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
