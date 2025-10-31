from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Hello from Azure App Service! Your deployment works."

if __name__ == '__main__':
    app.run()
