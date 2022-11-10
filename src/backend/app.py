""" This is a module docstring """
import json
import dataclasses
from collections import namedtuple
from werkzeug.datastructures import MultiDict
from flask_cors import CORS
from flask import Flask, request
from flask_cors import CORS
from pages.login import Login
from pages.mainpage import MainPage

# from logging import FileHandler, WARNING
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/login", methods=["POST", "GET"])
def login():
    """Handles login routing"""
    user_login = Login()
    json_form = request.get_json(force=True)

    if isinstance(json_form, dict):
        user = json_form.get("user", "")
        password = json_form.get("password", "")
        if user_login.login(user, password):
            return f"welcome {user}", 200
        return "User not found, please try again", 401
    return "", 400


@app.route("/register", methods=["POST", "GET"])
def register():
    """Handles register routing"""
    user_login = Login()
    json_form = request.get_json(force=True)

    if isinstance(json_form, dict):
        username = json_form.get("username", "")
        email = json_form.get("email", "")
        password = json_form.get("password", "")
        phone = json_form.get("phone", "")
        result = user_login.register(username, email, password, phone)
        if not result.status:
            return result.message, 400
        return result.message, 201
    return "", 400


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
    """
    Helper for mainpage get requests
    Actions that use get requests:
    - Searching apartments
    - Populating the mainpage with apartments
    - Getting reviews of an apartment
    - Getting pictures of an apartment
    """
    action_type = namedtuple(
        "action_type", ["is_search", "is_populate", "is_review", "is_pictures"]
    )
    action = action_type(
        args.get("search", default=False, type=bool),
        args.get("populate", default=False, type=bool),
        args.get("review", default=False, type=bool),
        args.get("pictures", default=False, type=bool),
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
    if action.is_search is True and param.search_query is not None:
        apts = mainpage_obj.search_apartments(param.search_query)
        apts_dict = [dataclasses.asdict(apt) for apt in apts]
        query_result = json.dumps(apts_dict)

    elif action.is_populate is True and param.num_apts is not None:
        apts = []
        price_sort = 0
        rating_sort = 0
        if param.price_sort is not None:
            price_sort = param.price_sort

        if param.rating_sort is not None:
            rating_sort = param.rating_sort
        apts = mainpage_obj.populate_apartments(param.num_apts, price_sort, rating_sort)
        apts_dict = [dataclasses.asdict(apt) for apt in apts]
        query_result = json.dumps(apts_dict)

    elif action.is_review is True and param.apt_id is not None:
        reviews = mainpage_obj.get_apartments_reviews(param.apt_id)
        reviews_dict = [dataclasses.asdict(review) for review in reviews]
        query_result = json.dumps(reviews_dict)

    elif action.is_pictures is True and param.apt_id is not None:
        query_result = json.dumps(mainpage_obj.get_apartments_pictures(param.apt_id))

    if len(query_result) != 0:
        return query_result, 200
    return "", 400


def mainpage_post(mainpage_obj: MainPage):
    """
    Helper for mainpage post requests
    Actions that use post request:
    - Writing a review to an apartment
    """
    json_form = request.get_json(force=True)

    if isinstance(json_form, dict):
        apt_id = json_form.get("apt_id")
        username = json_form.get("username")
        comment = json_form.get("comment")
        vote = json_form.get("vote")
        if (
            apt_id is not None
            and username is not None
            and comment is not None
            and vote is not None
        ):
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
