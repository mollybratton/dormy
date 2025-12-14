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
    return render_template("index.html", title = "Dormy")



@app.route("/building_results")
def display_building_results():
    """Arguments: None
    Return value: Dorms for specifed building
    Purpose: Looks through data to find the dorms in a specified building, and returns the dorms sorted by area
    """
    building = str(request.args["buildingname"])
    dorms = data.areaByBuilding(building)
    return render_template(
    "building_results.html",
    building_searched = building,
    dorms_from_building = dorms,
    )

    # datatype = str(request.args["data_type"])
    # if datatype == "SES":
    #     socioeconomic = data.getSESByCounty(county)
    #     return render_template(
    #     "county_results_ses.html",
    #     county_searched=county,
    #     socioeconomic_for_county=socioeconomic,
    # )
    
    # elif datatype == "Scores":
    #     score = data.getScoresByCounty(county)
    #     return render_template(
    #     "county_results_scores.html",
    #     county_searched=county,
    #     score_for_county=score,
    # )

    # elif datatype == "Both":
    #     score = data.getScoresByCounty(county)
    #     socioeconomic = data.getSESByCounty(county)
    #     return render_template(
    #     "county_results_both.html",
    #     county_searched=county,
    #     score_for_county=score,
    #     socioeconomic_for_county=socioeconomic,
    #     )

@app.route("/dataset")
def dataset_info():
    """Arguments: None
    Return value: Page with information about the data source for the website
    Purpose: Display the data source links"""
    return render_template("dataset_info.html")


@app.route("/searchpage")
def search_page():
    """Arguments: None
    Return value: Page where you can search dorms by building
    Purpose: Display the buildings that you can choose from"""
    dorms = data.getAllBuildingNames()
    return render_template("searchpage.html", dorms=dorms)
 

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
    app.run(host='0.0.0.0', port=5205)
    
if __name__ == '__main__':
# Debugging, remove after testing
   main()