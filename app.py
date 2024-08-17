from flask import Flask, render_template, request, redirect, url_for

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


@app.route('/new_create_ticket', methods=['POST'])
def new_create_ticket():
    if "submit" in request.form:
        ticket_title = request.form.get("ticket_title")
        ticket_description = request.form.get("ticket_description")
        ticket_priority = request.form.get("ticket_priority")
        ticket_assignment_group = request.form.get("ticket_assignment_group")
        ticket_creation_date = request.form.get("ticket_creation_date")
        ticket_created_by = request.form.get("ticket_created_by")

        print("Ticket title:", ticket_title)
        print("Ticket Description:", ticket_description)
        print("Ticket priority:", ticket_priority)
        print("Ticket Assignment group:", ticket_assignment_group)
        print("Ticket Creation Date:", ticket_creation_date)
        print("Ticket created by:", ticket_created_by)
        return redirect(url_for('home'))
    return render_template('new_ticket_page.html')



if __name__ == '__main__':
    app.run(debug=True)