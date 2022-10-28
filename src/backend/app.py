""" This is a module docstring """
import json
import dataclasses
from flask import Flask, request
from login import Login
from mainpage import MainPage
# from logging import FileHandler, WARNING

app = Flask(__name__)


@app.route("/login", methods=["POST", "GET"])
def login():
    """Handles login routing"""
    user_login = Login()
    user = request.json["user"]
    password = request.json["password"]
    if user_login.login(user, password):
        return f"welcome {user}", 200
    return "User not found, please try again", 404


@app.route("/register", methods=["POST", "GET"])
def register():
    """Handles register routing"""
    user_login = Login()
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]
    phone = request.json["phone"]
    result = user_login.register(username, email, password, phone)
    if not result.status:
        return result.message, 400
    return result.message, 200

@app.route("/", methods=["POST", "GET"])
@app.route("/main", methods=["POST", "GET"])
def mainpage():
    """Handle mainpage requests"""
    mainpage = MainPage()
    if request.method == "POST":
        apt_id = request.json["apt_id"]
        username = request.json["username"]
        comment = request.json["comment"]
        vote = request.json["vote"]
        query_result = ""
        if None not in (apt_id, username, comment, vote):
            reviews = mainpage.write_apartment_review(apt_id, username, comment, vote)
            reviews_dict = [dataclasses.asdict(review) for review in reviews]
            query_result = json.dumps(reviews_dict)
        return query_result, 201 if len(query_result) != 0 else query_result, 400
    
    args = request.args
    is_search = args.get("search")
    is_populate = args.get("populate")
    is_review = args.get("review")
    is_pictures = args.get("pictures")
    num_apts = args.get("numApts", type=int)
    apt_id = args.get("aptId", default=0, type=int)
    search_query = args.get("searchQuery", type=str)
    price_sort = args.get("priceSort", type=int)
    rating_sort = args.get("ratingSort", type=int)
    query_result = ""
    if is_search is not None and search_query is not None:
        query_result = json.dumps(mainpage.search_apartments(search_query))
    elif is_populate is not None and num_apts is not None:
        apts = []
        if price_sort is not None and rating_sort is not None:
            apts = mainpage.apartments_sorted(num_apts, price_sort, rating_sort)
        else:
            apts = mainpage.apartments_default(num_apts)
        apts_dict = [dataclasses.asdict(apt) for apt in apts]
        query_result = json.dumps(apts_dict)
    elif is_review is not None and apt_id is not None:
        reviews = mainpage.get_apartments_reviews(apt_id)
        reviews_dict = [dataclasses.asdict(review) for review in reviews]
        query_result = json.dumps(reviews_dict)
    elif is_pictures is not None and apt_id is not None:
        query_result = json.dumps(mainpage.get_apartments_pictures(apt_id))
    return query_result, 200 if len(query_result) != 0 else query_result, 400

if __name__ == "__main__":
    app.run(debug=True)  # pragma: no cover
