from flask import Flask, render_template
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(__name__)

def create_plot():
    tips = sns.load_dataset("tips")
    sns_plot = sns.relplot(x="total_bill", y="tip", data=tips)
    sns_plot.savefig('static/plot.png')

@app.route('/')
def home():
    message="Ivan Sergio Lopez"
    return render_template('index.html',message=message)

if __name__ == '__main__':
    create_plot()
    app.run(debug=True)

