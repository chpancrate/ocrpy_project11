import json
from datetime import datetime
from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   flash,
                   url_for,
                   abort)
import copy


CLUBS_JSON_FILE_NAME = 'clubs.json'
COMPETITIONS_JSON_FILE_NAME = 'competitions.json'


def loadClubs():
    try:
        with open(CLUBS_JSON_FILE_NAME) as clubs_file:
            list_of_clubs = json.load(clubs_file)['clubs']
    except FileNotFoundError:
        list_of_clubs = []
    except json.JSONDecodeError:
        list_of_clubs = []

    return list_of_clubs


def loadCompetitions():
    try:
        with open(COMPETITIONS_JSON_FILE_NAME) as competitions_file:
            list_of_competitions = json.load(competitions_file)['competitions']
    except FileNotFoundError:
        list_of_competitions = []
    except json.JSONDecodeError:
        list_of_competitions = []
    return list_of_competitions


def save_clubs(clubs_list):
    try:
        with open(CLUBS_JSON_FILE_NAME, 'w') as club_file:
            clubs_file_content = {}
            clubs_file_content["clubs"] = clubs_list
            json.dump(clubs_file_content, club_file)
    except Exception:
        abort(500, description="cannot write clubs file")


def save_competitions(competitions_list):
    try:
        with open(COMPETITIONS_JSON_FILE_NAME, 'w') as competitions_file:
            competitions_file_content = {}
            competitions_file_content["competitions"] = competitions_list
            json.dump(competitions_file_content, competitions_file)
    except Exception:
        abort(500, description="cannot write competitions file")


def competitions_list_rework(competitions_param):

    competitions_list = copy.deepcopy(competitions_param)
    # add a flag to tell that the competition is in the past
    sorted_competitions = sorted(competitions_list,
                                 key=lambda x: x['date'],
                                 reverse=True)
    for competition in sorted_competitions:
        competition_date = datetime.strptime(competition['date'],
                                             "%Y-%m-%d %H:%M:%S")
        competition['is_not_in_past'] = (
            datetime.now() < competition_date)
        competition['date'] = competition_date.strftime("%d %B %Y, %H:%M")

    return sorted_competitions


competitions = loadCompetitions()
clubs = loadClubs()


def create_app():

    app = Flask(__name__)
    app.config.from_object("config")

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        custom_message = error.description
        return render_template('500.html', custom_message=custom_message), 500

    @app.route('/')
    def index():
        if clubs == [] or competitions == []:
            abort(500, description="json files missing or empty")
        sorted_clubs = sorted(clubs, key=lambda x: x['name'])
        clubs_mini_board = sorted_clubs[:10]
        return render_template('index.html', clubs=clubs_mini_board)

    @app.route('/showSummary', methods=['POST'])
    def showSummary():
        try:
            club = [club for club in clubs if club['email']
                    == request.form['email']][0]

            sorted_competitions = competitions_list_rework(competitions)

            return render_template('welcome.html',
                                   club=club,
                                   competitions=sorted_competitions)
        except IndexError:
            flash("Unknown email")
            return redirect(url_for('index'))

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

        reservations = foundClub['reservations']
        try:
            club_reservation = [resa for resa in reservations
                                if resa['competition'] == competition][0]
            reserved_places = int(club_reservation['places'])
        except IndexError:
            reserved_places = 0

        return render_template('booking.html',
                               club=foundClub,
                               competition=foundCompetition,
                               reserved_places=reserved_places)

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

        reservations = club['reservations']
        try:
            club_reservation = [resa for resa in reservations
                                if (resa['competition']
                                    == competition['name'])][0]
            reserved_places = int(club_reservation['places'])
            already_reserved = True
        except IndexError:
            reserved_places = 0
            already_reserved = False

        places_required = int(request.form['places'])
        places_available = int(competition['numberOfPlaces'])
        club_points = int(club['points'])

        total_places = places_required + reserved_places

        if places_required > club_points:
            flash("You do not have enough points.")
            return render_template('booking.html',
                                   club=club,
                                   competition=competition,
                                   reserved_places=reserved_places)
        elif total_places > 12:
            flash("You cannot book more than 12 places.")
            return render_template('booking.html',
                                   club=club,
                                   competition=competition,
                                   reserved_places=reserved_places)
        elif places_required > places_available:
            flash("There is not enough places in the competition.")
            return render_template('booking.html',
                                   club=club,
                                   competition=competition,
                                   reserved_places=reserved_places)

        competition['numberOfPlaces'] = (int(competition['numberOfPlaces'])
                                         - places_required)
        club['points'] = int(club['points']) - places_required

        if already_reserved:
            # if places were already reserved we update the record
            club_reservation['places'] = total_places
        else:
            # else we create a record
            reservations.append({
                "competition": competition['name'],
                "places": total_places
            })

        save_clubs(clubs)
        save_competitions(competitions)

        flash('Great-booking complete!')

        sorted_competitions = competitions_list_rework(competitions)

        return render_template('welcome.html',
                               club=club,
                               competitions=sorted_competitions)

    @app.route('/board')
    def board():
        if clubs == [] or competitions == []:
            abort(500, description="json files missing or empty")
        sorted_clubs = sorted(clubs, key=lambda x: x['name'])
        return render_template('board.html', clubs=sorted_clubs)

    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
