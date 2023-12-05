# from flask import Flask
# from src.controller import books_bp

# app = Flask(__name__)

# # Register blueprints
# app.register_blueprint(books_bp)

# # Run the application
# if __name__ == '__main__':
#     app.run(debug=True)
import os

# Get the current working directory
current_directory = os.getcwd()

print("Current working directory:", current_directory)