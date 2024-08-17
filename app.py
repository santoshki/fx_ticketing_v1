from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('homepage.html')


@app.route('/handle-request', methods=['POST'])
def handle_buttons():
    if 'ticket_queue_button' in request.form:
        print("Loading ticket queue...")
        return "Loading ticket queue!"
    elif 'create_new_ticket_button' in request.form:
        print("New ticket to be created!")
        return render_template('new_ticket_page.html')
    else:
        return "No button was pressed!"


if __name__ == '__main__':
    app.run(debug=True)
