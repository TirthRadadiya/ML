from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "CI CD is not that hard"


if __name__=="__main__":
    app.run(debug=True)

# 5becb856-f085-4632-af7c-64df98e447d0 - Heroku API Key
# mlregressions - Heroku App Name