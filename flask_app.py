from flask import Flask, render_template, request
from ProductionCode.datasource import *
import csv


app = Flask(__name__)

data = DataSource()


@app.route('/')
def homepage():
    '''
    Arguments: None
    Return value: str (HTML response)
    Purpose: To display the homepage with instructions on how to interact with the app withinthe httml tags.
    Provides information on available routes and how to use them to retrieve data.
    '''
    return render_template("index.html", title = "Minnesota Education Gap Project")


@app.route('/ses/<county_name>', strict_slashes=False)
def ses_by_county_page(county_name):
    '''
    Arguments: 
        county_name (str) - The name of the county to look up
    Return value: str - The SES value for the specified county.
    Purpose: To retrieve and display the socioeconomic status (SES) for a given county
    by calling the helper function 'get_ses_by_county'.
    '''
    ses = data.getSESByCounty(county_name) 
    return f"The socioeconomic status (SES) of {county_name} is: {ses}"

@app.route('/scores/<county_name>', strict_slashes=False)
def scores_by_county_page(county_name):
    '''
    Arguments:
        county_name (str) - The name of the county to look up
    Return value: str - The test scores for the specified county.
    Purpose: To retrieve and displays the test scores for a given county
    by calling the helper function 'get_scores_by_county'.
    '''
    scores = data.getScoresByCounty(county_name)  # Call the function from helper_functions
    return f"The test scores of {county_name} are: {scores}"

@app.route("/displaycountyresults")
def display_county_results():
    """Arguments: None
    Return value: Test scores and socioeconomic measure for a specific county or None
    Purpose: Looks through data to see if there is a matching county, and returns the relevant test scores and socioeconomic measure
    """
    county = str(request.args["countyname"])
    datatype = str(request.args["data_type"])
    if datatype == "SES":
        socioeconomic = data.getSESByCounty(county)
        return render_template(
        "county_results_ses.html",
        county_searched=county,
        socioeconomic_for_county=socioeconomic,
    )
    
    elif datatype == "Scores":
        score = data.getScoresByCounty(county)
        return render_template(
        "county_results_scores.html",
        county_searched=county,
        score_for_county=score,
    )

    elif datatype == "Both":
        score = data.getScoresByCounty(county)
        socioeconomic = data.getSESByCounty(county)
        return render_template(
        "county_results_both.html",
        county_searched=county,
        score_for_county=score,
        socioeconomic_for_county=socioeconomic,
        )

@app.route("/dataset")
def dataset_info():
    """Arguments: None
    Return value: Page with information about the data source for the website
    Purpose: Display the data source links"""
    return render_template("dataset_info.html")

@app.route("/definitions")
def definitions():
    """Arguments: None
    Return value: Page with information about the data source for the website
    Purpose: Display the data source links"""
    return render_template("definitions.html")

@app.route("/searchpage")
def search_page():
    """Arguments: None
    Return value: Page with information about the data source for the website
    Purpose: Display the data source links"""
    counties = data.getAllCountyNames()
    return render_template("searchpage.html", counties=counties)
 

@app.route('/Bug/', strict_slashes=False)
def bug_page():
    '''
    Arguments: None
    Return value: None
    Purpose: To test if our 500 works by giving it a bug.
    '''
    return 10


@app.errorhandler(404)
def page_not_found(e):
    '''Arguments: e
    Return value: Message with instructions about how to use the website and states page was not found
    Purpose: Displays a page not found message with info about how to use the website'''
    return render_template("404.html")

@app.errorhandler(500)
def python_bug(e):
    '''Arguments: None
    Return value: Message that states there is an error in the code (internal error)
    Purpose: Displays a message regarding an internal error'''
    return "Bug in the code...time to debug"

def main():
    ''' Arguments: None
    Return Value: None
    Purpose: Run the app
    '''
    app.run(host='0.0.0.0', port=5241)
    
if __name__ == '__main__':
# Debugging, remove after testing
   main()