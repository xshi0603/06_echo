from flask import Flask, render_template, request

my_app = Flask(__name__)

@my_app.route('/', methods = ["POST", "GET"])
def root():
    if request.method == 'POST':
        return render_template('returned.html', title = "returned", retVal = request.form ['user'])
    else:
        return render_template('form.html', title = "Form")

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
