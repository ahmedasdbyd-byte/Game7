from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>لعبة تخمين الرقم</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background-color: #f0f0f0; padding: 50px; }
            h1 { color: #333; }
            input { padding: 10px; font-size: 16px; }
            button { padding: 10px 20px; font-size: 16px; background-color: #28a745; color: white; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>أهلاً بك في لعبة تخمين الرقم!</h1>
        <p>حاول تخمين الرقم بين 1 و 10</p>
        <form method="POST" action="/guess">
            <input type="number" name="number" min="1" max="10" required>
            <button type="submit">تخمين</button>
        </form>
    </body>
    </html>
    ''')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = request.form.get('number')
    correct_number = "7"  # الرقم الصحيح
    if user_guess == correct_number:
        message = "مبروك! التخمين صحيح 🎉"
    else:
        message = "للأسف، حاول مرة أخرى ❌"
    
    return f"<h1>{message}</h1><br><a href='/'>ارجع للعبة</a>"

if __name__ == '__main__':
    app.run(debug=True)
  
