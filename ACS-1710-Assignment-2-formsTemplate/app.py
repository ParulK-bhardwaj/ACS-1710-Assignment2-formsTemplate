from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))

# ------------------------------- Homepage ------------------------------- 
@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

# ------------------------------- FroYO ------------------------------- 
@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
        'users_froyo_flavor': request.args.get("flavor"),
        'users_toppings': request.args.get("toppings")
    }
    return render_template('froyo_results.html', **context)

# ------------------------------- Favorites ------------------------------- 
@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action='/favorites_results' method="GET">
       What is your favorite color? <br/>
       <input type="text" name="color"><br/>
       What is your favorite animal? <br/>
       <input type="text" name="animal"><br/>
       What is your favorite city? <br/>
       <input type="text" name="city"><br/>
       <input type="submit" value="Submit!">
     </form>
    """


@app.route("/favorites_results")
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_color = request.args.get("color")
    users_animal = request.args.get("animal")
    users_city = request.args.get("city")
    return f"Wow, I didn't know {users_color} {users_animal} lived in {users_city}!"

# ------------------------------- Secret Message ------------------------------- 
@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Please enter the secret message that you want to send: <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_message = request.form.get('message')
    return f"Here's your secret message!\n {sort_letters(users_message)}"

# ------------------------------- Calculator ------------------------------- 
@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    users_first_number = int(request.args.get('operand1'))
    users_second_number = int(request.args.get('operand2'))
    users_option = request.args.get('operation')

    if users_option == "add":
        result = users_first_number + users_second_number
        return f"You chose to {users_option} {users_first_number} and {users_second_number}. Your result is: {result}"
    elif users_option == "subtract":
        result = users_first_number - users_second_number
        return f"You chose to {users_option} {users_first_number} and {users_second_number}. Your result is: {result}"
    elif users_option == "multiply":
        result = users_first_number * users_second_number
        return f"You chose to {users_option} {users_first_number} and {users_second_number}. Your result is: {result}"
    elif users_option == "divide":
        result = users_first_number / users_second_number
        return f"You chose to {users_option} {users_first_number} and {users_second_number}. Your result is: {result}"
        
    context = {
        'operand1': users_first_number,
        'operand2' : users_second_number,
        'operation' : users_option,
        'result' : result
    }
    return render_template('calculator_results.html', **context)

# ------------------------------- Horoscope ------------------------------- 

HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""
    users_name = request.args.get('users_name')
    horoscope_sign = request.args.get('horoscope_sign')

    for sign in HOROSCOPE_PERSONALITIES:
        if sign == horoscope_sign:
            users_personality = (HOROSCOPE_PERSONALITIES[sign])

    lucky_number = 0
    lucky_number = random.randint(1,99)

    # added users_name to greet the user by name
    context = {
        'users_name': users_name,
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
