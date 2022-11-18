""" This is a module docstring """
import json
import dataclasses
from werkzeug.datastructures import MultiDict
from flask_cors import CORS
from flask import Flask, request
from flask_cors import CORS
from pages.login import Login
from pages.mainpage import MainPage
from dataholders.mainpage_get import GetRequestType, GetRequestParams

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
    action = GetRequestType(
        args.get("search", default=False, type=bool),
        args.get("populate", default=False, type=bool),
        args.get("review", default=False, type=bool),
        args.get("pictures", default=False, type=bool),
    )

    param = GetRequestParams(
        args.get("numApts", type=int),
        args.get("aptId", type=int),
        args.get("searchQuery", type=str),
        args.get("priceSort", type=int),
        args.get("ratingSort", type=int),
    )

    return mainpage_process_get(mainpage_obj, action, param)


def mainpage_process_get(
    mainpage_obj: MainPage, action: GetRequestType, param: GetRequestParams
):
    """Process the get requests"""
    query_result = ""
    if action.is_search is True and param.search_query is not None:
        apts = mainpage_obj.search_apartments(param.search_query)
        query_result = dataclasses_into_json(apts)

    elif action.is_populate is True and param.num_apts is not None:
        apts = []
        price_sort = 0
        rating_sort = 0
        apt_id = -1
        if param.price_sort is not None:
            price_sort = param.price_sort

        if param.rating_sort is not None:
            rating_sort = param.rating_sort

        if param.apt_id is not None:
            apt_id = param.apt_id
        apts = mainpage_obj.populate_apartments(
            param.num_apts, price_sort, rating_sort, apt_id
        )
        query_result = dataclasses_into_json(apts)

    elif action.is_review is True and param.apt_id is not None:
        reviews = mainpage_obj.get_apartments_reviews(param.apt_id)
        query_result = dataclasses_into_json(reviews)

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

    is_delete = request.args.get("delete", default=False, type=bool)

    if isinstance(json_form, dict):
        if not is_delete:
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
                reviews = mainpage_obj.write_apartment_review(
                    apt_id, username, comment, vote
                )
                return dataclasses_into_json(reviews), 201
        else:
            apt_id = json_form.get("apt_id")
            username = json_form.get("username")
            if apt_id is not None and username is not None:
                reviews = mainpage_obj.delete_apartment_review(apt_id, username)
                return dataclasses_into_json(reviews), 201
    return "", 400


def dataclasses_into_json(data_sequence: list):
    """Process dataclasses into json strings"""
    data_dict = [dataclasses.asdict(data) for data in data_sequence]
    query_result = json.dumps(data_dict)
    return query_result


if __name__ == "__main__":
    app.run(debug=True)  # pragma: no cover
