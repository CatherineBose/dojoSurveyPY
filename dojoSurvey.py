from flask import Flask, render_template, request, redirect  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
global name 
global location       
global language        
global comment                  # are running the file directly or importing it as a module.
@app.route('/')    
        
def home_page():
  return render_template('index.html')    

@app.route('/result', methods=['POST'])
def about():
    print "Inside result method"
    name = request.form['name']
    location= request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print "name", name
    print "loc:", location
    print "language", language
    print "comment", comment
    return render_template('result.html',name=name,location=location,language=language, comment=comment)  
    return redirect ('/')

# @app.route('/resultStep1')
# def resultOP():
#     print "name", name
#     print "loc:", location
#     print "language", language
#     print "comment", comment
#     return render_template('result.html',name=name,location=location,language=language, comment=comment)  
app.run(debug=True)                             

