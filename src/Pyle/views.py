from flask import (
    Blueprint,
    current_app,
    render_template
    )

from .forms import NewVehicleForm

app_view = Blueprint('views', __name__)

'''
Main Menu page
'''
@app_view.route('/')
@app_view.route('/index')
@app_view.route('/main')
@app_view.route('/home')
def index():
    return render_template(
        'index.html',
        title=f'{current_app.config['APP_NAME']} - Main'
        )

'''
Vehicle Details page
'''
@app_view.route('/details', methods=['GET', 'POST'])
def details():
    return render_template(
        'details.html',
        title=f'{current_app.config['APP_NAME']} - Details'
    )

'''
Vehicle History page
'''
@app_view.route('/history', methods=['GET', 'POST'])
def history():
    return render_template(
        'history.html',
        title=f'{current_app.config['APP_NAME']} - History'
    )

'''
Vehicle Status page
'''
@app_view.route('/status', methods=['GET', 'POST'])
def status():
    return render_template(
        'status.html',
        title=f'{current_app.config['APP_NAME']} - Status'
    )

'''
Add Vehicle page
'''
@app_view.route('/add_vehicle', methods=['GET', 'POST'])
def add_vehicle():
    form = NewVehicleForm()
    return render_template(
        'add_vehicle.html',
        title=f'{current_app.config['APP_NAME']} - New Vehicle Profile',
        form=form
        )