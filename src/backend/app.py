""" This is a module docstring """
import json
import dataclasses
from collections import namedtuple
from werkzeug.datastructures import MultiDict
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
    mainpage_obj = MainPage()
    if request.method == "POST":
        return mainpage_post(mainpage_obj)

    args = request.args
    return mainpage_get(mainpage_obj, args)


def mainpage_get(mainpage_obj: MainPage, args: MultiDict):
    """Helper for mainpage get requests"""
    action_type = namedtuple(
        "action_type", ["is_search", "is_populate", "is_review", "is_pictures"]
    )
    action = action_type(
        args.get("search"),
        args.get("populate"),
        args.get("review"),
        args.get("pictures"),
    )

    params = namedtuple(
        "params", ["num_apts", "apt_id", "search_query", "price_sort", "rating_sort"]
    )
    param = params(
        args.get("numApts", type=int),
        args.get("aptId", type=int),
        args.get("searchQuery", type=str),
        args.get("priceSort", type=int),
        args.get("ratingSort", type=int),
    )

    query_result = ""
    if action.is_search is not None and param.search_query is not None:
        query_result = json.dumps(mainpage_obj.search_apartments(param.search_query))

    elif action.is_populate is not None and param.num_apts is not None:
        apts = []
        if param.price_sort is not None and param.rating_sort is not None:
            apts = mainpage_obj.apartments_sorted(
                param.num_apts, param.price_sort, param.rating_sort
            )
        else:
            apts = mainpage_obj.apartments_default(param.num_apts)
        apts_dict = [dataclasses.asdict(apt) for apt in apts]
        query_result = json.dumps(apts_dict)

    elif action.is_review is not None and param.apt_id is not None:
        reviews = mainpage_obj.get_apartments_reviews(param.apt_id)
        reviews_dict = [dataclasses.asdict(review) for review in reviews]
        query_result = json.dumps(reviews_dict)

    elif action.is_pictures is not None and param.apt_id is not None:
        query_result = json.dumps(mainpage_obj.get_apartments_pictures(param.apt_id))

    if len(query_result) != 0:
        return query_result, 200
    return "", 400


def mainpage_post(mainpage_obj: MainPage):
    """Helper for mainpage post requests"""
    json_form = request.get_json(force=True)

    if json_form is not None:
        apt_id = json_form.get("apt_id")
        username = json_form.get("username")
        comment = json_form.get("comment")
        vote = json_form.get("vote")
        if None not in (apt_id, username, comment, vote):
            query_result = ""
            reviews = mainpage_obj.write_apartment_review(
                apt_id, username, comment, vote
            )
            reviews_dict = [dataclasses.asdict(review) for review in reviews]
            query_result = json.dumps(reviews_dict)
            return query_result, 201
    return "", 400


if __name__ == "__main__":
    app.run(debug=True)  # pragma: no cover
