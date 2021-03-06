from flask import Flask, render_template, session, redirect, request
from friends import Friend


app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                                     # Main Page
def index():
    print("**** in index ****")
    all_friends = Friend.get_all()
    print(all_friends)

    # for idx in range(len(all_friends)):
    #     print(all_friends[idx].first_name,all_friends[idx].last_name, all_friends[idx].occupation)

    return render_template("index.html", all_friends = all_friends)

@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["fname"],
        "last_name" : request.form["lname"],
        "occupation" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

# @app.route('/increment_by', methods=['POST'])
# def increment_by():

#     return redirect("/")

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)    