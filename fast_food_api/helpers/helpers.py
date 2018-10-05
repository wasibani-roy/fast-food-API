from flask import redirect, url_for, logging, jsonify
def check_admin(current_user):
    if current_user == 5:
        return True
    else:
        return jsonify("Unauthorised Access")