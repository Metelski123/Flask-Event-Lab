from flask import render_template, request, redirect
from app import app
from app.models.event_list import events
from app.models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)


@app.route('/events', methods=['POST'])
def add_event():
    date = request.form["date"]
    name_of_event = request.form["name_of_event"]
    no_of_guests = request.form["no_of_guests"]
    room_location = request.form["room_location"]
    description = request.form["description"]
    recurring = request.form["recurring"]
    new_event = Event(date, name_of_event, no_of_guests, room_location, description, recurring)
    events.append(new_event)
    return redirect('/events')

