from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from models import db, Hotel, User
from forms import SignupForm

# Define Blueprint for main routes
main_routes = Blueprint('main_routes', __name__)

# Route for home page showing all hotels
@main_routes.route('/')
def index():
    hotels = Hotel.query.all()
    return render_template('index.html', hotels=hotels)

# Route for hotel details
@main_routes.route('/hotel/<int:hotel_id>')
def hotel_details(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    return render_template('hotel_details.html', hotel=hotel)

# Route for hotel booking
@main_routes.route('/booking/<int:hotel_id>', methods=['GET', 'POST'])
def booking(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    if request.method == 'POST':
        # Handle booking logic
        # You can save booking details here if needed
        return redirect(url_for('main_routes.index'))
    return render_template('booking.html', hotel=hotel)

# Route for user signup
from forms import SignupForm

@main_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()  # Initialize the form

    if form.validate_on_submit():
        # Get form data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Check if the email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please use a different one.', 'error')
            return redirect(url_for('main_routes.signup'))

        # Hash the password and create new user
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Signup successful! You can now log in.', 'success')
        return redirect(url_for('main_routes.index'))  # Redirect after successful signup
    else:
        print("failure")

    return render_template('signup.html', form=form)  # Pass the form object to the template




@main_routes.route("/home")
def base():
    return redirect('base.html')