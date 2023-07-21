def is_authorized(user, object_owner_id):
    return user.user_id == object_owner_id
