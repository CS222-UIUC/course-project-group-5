""" Handles routing and HTTP Requests """
import json
import dataclasses
from werkzeug.datastructures import MultiDict
from flask import Flask, request, session
from flask_cors import CORS
from flask_session import Session
from pages.login import Login
from pages.mainpage import MainPage
from pages.userpage import UserPage
from dataholders.mainpage_get import GetRequestType, GetRequestParams

app = Flask(__name__)
SECRET_KEY = b"xe47Wxcdx86Wxac(mKlxa5xa2,xb3axc6xf1x86Fxc25x94xfc"
SESSION_TYPE = "filesystem"
app.config.from_object(__name__)
Session(app)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handles login routing"""
    user_login = Login()
    json_form = request.get_json(force=True)

    if isinstance(json_form, dict):
        username = json_form.get("user", "")
        password = json_form.get("password", "")
        if user_login.login(username, password):
            # session object makes User accessible in the backend
            session["username"] = username
            print(session.get("username"))
            return f"welcome {username}", 200
        return "User not found, please try again", 401
    return "", 400


@app.route("/register", methods=["GET", "POST"])
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
        session.pop("username", None)
        return result.message, 201
    return "", 400


@app.route("/user", methods=["GET", "POST"])
def userpage():
    """Handles userpage requests"""
    print(session.get("username"))
    if session.get("username") is None:
        return "user does not exist", 403
    name = session.get("username") or ""
    page = UserPage(name)
    if request.method == "POST":
        json_form = request.get_json(force=True) or {}  # deserialize data
        # see which field was True and therefore should be changed
        is_password = json_form.get("is_password", False)
        is_email = json_form.get("is_email", False)
        is_phone = json_form.get("is_phone", False)
        is_get_liked = json_form.get("is_get_liked", False)
        result = False
        if is_password:
            result = page.update_password(json_form.get("password") or "")
        elif is_email:
            result = page.update_email(json_form.get("email") or "")
        elif is_phone:
            result = page.update_phone(json_form.get("phone") or "")
        elif is_get_liked:
            liked_apts = page.get_liked(json_form.get("user_id") or 0)
            return dataclasses_into_json(liked_apts), 201
        if not result:
            return "invalid request", 400
        return "success", 201
    user = page.get_user(name)  # request.method == "GET"
    data_dict = dataclasses.asdict(user)
    return json.dumps(data_dict), 200


@app.route("/logout")
def logout():
    """Removes session object"""
    session.pop("username", None)  # remove session object
    return "", 201


@app.route("/api/whoami")
def whoami():
    """Shows whether a user is logged in and returns session username"""
    print(session.get("username"))
    if session.get("username") is None:
        return "user logged out", 403
    username = session.get("username", "")
    return str(username), 201


@app.route("/", methods=["GET", "POST"])
@app.route("/main", methods=["GET", "POST"])
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
