from flask import Flask, render_template_string, request, render_template, abort,send_file, g, jsonify
import subprocess
import sqlite3, os


app = Flask(__name__, static_url_path='/static')
app.database = "app.db"

#---------------------------------SSTI and XSS VULNERABILITY 
@app.route("/contact")
def contact():
    
    blacklist = [".","[","]","_","join","init","flag"]
    email = request.args.get('email') or None

    template = '''
    <html>
        <head>
        <!-- Basic -->
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <!-- Mobile Metas -->
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <!-- Site Metas -->
        <link rel="icon" href="{{ url_for('static', filename='images/fevicon.png') }}" type="image/gif" />
        <meta name="keywords" content="" />
        <meta name="description" content="" />
        <meta name="author" content="" />

        <title>Hostit</title>


        <!-- bootstrap core css -->
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/bootstrap.css') }}" />

        <!-- fonts style -->
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap" rel="stylesheet">

        <!-- font awesome style -->
        <link href="{{ url_for('static', filename='css/font-awesome.min.css') }}" rel="stylesheet" />

        <!-- Custom styles for this template -->
        <link href="{{ url_for('static', filename='css/style.css') }}" rel="stylesheet" />
        <!-- responsive style -->
        <link href="{{ url_for('static', filename='css/responsive.css') }}" rel="stylesheet" />

        </head>

        <body class="sub_page">
        <div class="hero_area">
            <!-- header section strats -->
            <header class="header_section">
            <div class="container-fluid">
                <nav class="navbar navbar-expand-lg custom_nav-container ">
                <a class="navbar-brand" href="{{ url_for('home') }}">
                    <span>Hostit</span>
                </a>

                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class=""> </span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav  ml-auto">
                    <li class="nav-item ">
                        <a class="nav-link" href="{{ url_for('home') }}">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item active">
                        <a class="nav-link" href="{{ url_for('about') }}"> About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('service') }}">Services</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('price') }}">Pricing</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('contact') }}">Contact</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('login') }}">Admin</a>
                    </li>
                    </ul>
                    <div class="quote_btn-container">
                    <form style="margin: 0!important;" class="form-inline">
                        <button class="btn   nav_search-btn" type="submit">
                        <i class="fa fa-search" aria-hidden="true"></i>
                        </button>
                    </form>
                    <a href="">
                        <i class="fa fa-phone" aria-hidden="true"></i>
                        <span>
                        Call : +01 123455678990
                        </span>
                    </a>
                    </div>
                </div>
                </nav>
            </div>
            </header>
            <!-- end header section -->
        </div>

        <!-- jQery -->
        <script src="{{ url_for('static', filename='js/jquery-3.4.1.min.js') }}"></script>
        <!-- bootstrap js -->
        <script src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
        <!-- custom js -->
        <script src="{{ url_for('static', filename='js/custom.js') }}"></script>
        </body>
        </html>
    '''

    footer = '''
     <!-- footer section -->
        <footer class="footer_section">
            <div class="container">
        
            </div>
        </footer>
        <!-- footer section -->
    '''

    if email == None:
        template = template + '''
        <!-- Contact section -->
        <section class="contact_section layout_padding">
            <div class="container">
            <div class="heading_container heading_center">
                <h2>
                Contact Form
                </h2>
            </div>
            <div class="row">
                <div class="col-md-8 col-lg-6 mx-auto">
                <div class="form_container">
                    <form action="">
                    <div>
                        <input name="email" type="text" value="Send your email" />
                    </div>
                
                    <div class="btn_box ">
                        <button type="submit">
                        SEND
                        </button>
                    </div>
                    </form>
                </div>
                </div>
            </div>
            </div>
        </section>
        <!-- end contact section -->

        <!-- info section -->

        <section class="info_section layout_padding2">
            <div class="container">
            <div class="row">
                <div class="col-md-3">
                <div class="info_contact">
                    <h4>
                    Address
                    </h4>
                    <div class="contact_link_box">
                    <a href="">
                        <i class="fa fa-map-marker" aria-hidden="true"></i>
                        <span>
                        Location
                        </span>
                    </a>
                    <a href="">
                        <i class="fa fa-phone" aria-hidden="true"></i>
                        <span>
                        Call +01 1234567890
                        </span>
                    </a>
                    <a href="">
                        <i class="fa fa-envelope" aria-hidden="true"></i>
                        <span>
                        demo@gmail.com
                        </span>
                    </a>
                    </div>
                </div>
                <div class="info_social">
                    <a href="">
                    <i class="fa fa-facebook" aria-hidden="true"></i>
                    </a>
                    <a href="">
                    <i class="fa fa-twitter" aria-hidden="true"></i>
                    </a>
                    <a href="">
                    <i class="fa fa-linkedin" aria-hidden="true"></i>
                    </a>
                    <a href="">
                    <i class="fa fa-instagram" aria-hidden="true"></i>
                    </a>
                </div>
                </div>
                <div class="col-md-3">
                <div class="info_link_box">
                    <h4>
                    Links
                    </h4>
                    <div class="info_links">
                    <a class="" href="{{ url_for('home') }}">
                        <img src="{{ url_for('static', filename='images/nav-bullet.png') }}" alt="">
                        Home
                    </a>
                    <a class="" href="{{ url_for('about') }}">
                        <img src="{{ url_for('static', filename='images/nav-bullet.png') }}" alt="">
                        About
                    </a>
                    <a class="" href="{{ url_for('service') }}">
                        <img src="{{ url_for('static', filename='images/nav-bullet.png') }}" alt="">
                        Services
                    </a>
                    <a class="" href="{{ url_for('price') }}">
                        <img src="{{ url_for('static', filename='images/nav-bullet.png') }}" alt="">
                        Pricing
                    </a>
                    <a class="active" href="{{ url_for('contact') }}">
                        <img src="{{ url_for('static', filename='images/nav-bullet.png') }}" alt="">
                        Contact
                    </a>
                     <a class="active" href="{{ url_for('login') }}">
                        <img src="{{ url_for('static', filename='images/nav-bullet.png') }}" alt="">
                        Admin
                    </a>
                    </div>
                </div>
                </div>
                <div class="col-md-3">
                <div class="info_detail">
                    <h4>
                    Info
                    </h4>
                    <p>
                    necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful
                    </p>
                </div>
                </div>
                <div class="col-md-3 mb-0">
                <h4>
                    Subscribe
                </h4>
                <form>
                    <input type="text" placeholder="Enter email" />
                    <button type="submit">
                    Subscribe
                    </button>
                </form>
                </div>
            </div>
            </div>
        </section>

        <!-- end info section -->
     
        ''' + footer
    else:
        for char in blacklist:
            if char in email:
                return render_template('alert.html')

        template = template + '''
        <div style="padding:150px 0 150px 150px;"><h1>Email was sent successfully {}</h1>
        Welcome to the HOSTIT!<br></div>
      
          <!-- info section -->

        <section class="info_section layout_padding2">
            <div class="container">
            <div class="row">
                <div class="col-md-3">
                <div class="info_contact">
                    <h4>
                    Address
                    </h4>
                    <div class="contact_link_box">
                    <a href="">
                        <i class="fa fa-map-marker" aria-hidden="true"></i>
                        <span>
                        Location
                        </span>
                    </a>
                    <a href="">
                        <i class="fa fa-phone" aria-hidden="true"></i>
                        <span>
                        Call +01 1234567890
                        </span>
                    </a>
                    <a href="">
                        <i class="fa fa-envelope" aria-hidden="true"></i>
                        <span>
                        demo@gmail.com
                        </span>
                    </a>
                    </div>
                </div>
                <div class="info_social">
                    <a href="">
                    <i class="fa fa-facebook" aria-hidden="true"></i>
                    </a>
                    <a href="">
                    <i class="fa fa-twitter" aria-hidden="true"></i>
                    </a>
                    <a href="">
                    <i class="fa fa-linkedin" aria-hidden="true"></i>
                    </a>
                    <a href="">
                    <i class="fa fa-instagram" aria-hidden="true"></i>
                    </a>
                </div>
                </div>
                <div class="col-md-3">
                <div class="info_link_box">
                    <h4>
                    Links
                    </h4>
                    <div class="info_links">
                    <a class="" href="{{ url_for('home') }}">
                        <img src="{{ url_for('static', filename='images/nav-bullet.png') }}" alt="">
                        Home
                    </a>
                    <a class="" href="{{ url_for('about') }}">
                        <img src="{{ url_for('static', filename='images/nav-bullet.png') }}" alt="">
                        About
                    </a>
                    <a class="" href="{{ url_for('service') }}">
                        <img src="{{ url_for('static', filename='images/nav-bullet.png') }}" alt="">
                        Services
                    </a>
                    <a class="" href="{{ url_for('price') }}">
                        <img src="{{ url_for('static', filename='images/nav-bullet.png') }}" alt="">
                        Pricing
                    </a>
                    <a class="active" href="{{ url_for('contact') }}">
                        <img src="{{ url_for('static', filename='images/nav-bullet.png') }}" alt="">
                        Contact
                    </a>
                    </div>
                </div>
                </div>
                <div class="col-md-3">
                <div class="info_detail">
                    <h4>
                    Info
                    </h4>
                    <p>
                    necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful
                    </p>
                </div>
                </div>
                <div class="col-md-3 mb-0">
                <h4>
                    Subscribe
                </h4>
                <form action="#">
                    <input type="text" placeholder="Enter email" />
                    <button type="submit">
                    Subscribe
                    </button>
                </form>
                </div>
            </div>
            </div>
        </section>

        <!-- end info section -->
	'''.format(email) + footer
    
    return render_template_string(template)
#---------------------------------



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/price")
def price():
    return render_template("price.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/service")
def service():
    return render_template("service.html")


#---------------------------------OS COMMAND INJECTION
@app.route("/ping")
def index():
    return render_template("ping.html")

@app.route("/execute", methods=["POST"])
def execute():
    if request.method == "POST":
        address = request.form.get("address", "")

        try:
            # Уязвимое место: выполнение команды с использованием address
            command = f"ping -c 1 {address}"
            result = subprocess.check_output(command, shell=True, text=True, encoding='cp866')
            return render_template("result.html", result=result, command=command)
        except Exception as e:
            return render_template("result.html", result=f"Error: {str(e)}", command=f"ping -c 1 {address}")
     
#---------------------------------PATH TRAVERSAL VULNERABILITY  
@app.route("/view_file")
def view_file():
    filename = request.args.get("filename")

    if not filename:
        return "Filename not provided in the request", 400  # Bad Request

    try:
        return send_file(filename)
    except FileNotFoundError:
        abort(404)  # Not Found

#---------------------------------SQLI and Brute Force

@app.route('/login')
def login():
    return render_template('login.html')



#API routes
@app.route('/api/v1.0/storeLoginAPI/', methods=['POST'])
def loginAPI():
    if request.method == 'POST':
        uname,pword = (request.json['username'],request.json['password'])
        g.db = connect_db()
        cur = g.db.execute("SELECT * FROM employees WHERE username = '%s' AND password = '%s'" %(uname, pword))
        if cur.fetchone():
            result = {'status': 'success', 'user': uname}
        else:
            result = {'status': 'fail'}
        g.db.close()
        return jsonify(result)


#---------------------------------IDOR
@app.route('/admin-panel', methods=['GET'])
def admin_panel():
    user_param = request.args.get('user')

    if 'admin' in user_param:
        return render_template('admin_panel.html')
    elif 'wiener' in user_param:
        abort(403)
    else:
        abort(400)


def connect_db():
    return sqlite3.connect(app.database)
if __name__ == "__main__":
     #create database if it doesn't exist yet
    if not os.path.exists(app.database):
        with sqlite3.connect(app.database) as connection:
            c = connection.cursor()
            c.execute("""CREATE TABLE employees(username TEXT, password TEXT)""")
            c.execute('INSERT INTO employees VALUES("admin", "jasper")')
            c.execute('INSERT INTO employees VALUES("wiener", "password")')
            connection.commit()
            connection.close()

    app.run(debug=True, host='0.0.0.0', port=8089)

