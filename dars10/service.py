from db import commit
import db
import utils
import models


@commit
def login_user(username, password):
    user_data = db.get_user_by_username(username)
    user = models.User.from_tuple(user_data)
    if user.status == "BLOCKED":
        return utils.ResponseDate("Bad Credintials", False)
    if user.login_try_count >= 3:
        # INACTIVE user status
        return utils.ResponseDate("Bad Credintials user tried 3 times")
    if not utils.match_password(password, user.password):
        db.increase_user_try_count(username)
        return utils.ResponseDate("Bad Credintials password wrong")
    # login_try_count must be zero
    return utils.ResponseDate(user)