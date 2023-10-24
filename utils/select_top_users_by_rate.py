def select_top_users_by_rate(users, top_size):
    sorted_users = sorted(users, key=lambda user: user.rating, reverse=True)
    return sorted_users[:top_size]
