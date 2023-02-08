import time as tm


spams = {}
msgs = 6 # Messages in
_max = 60 # Seconds
ban = 600 # Seconds


def is_spam(user_id):
    try:
        usr = spams[user_id]
        usr["messages"] += 1
    except:
        spams[user_id] = {"next_time": int(tm.time()) + _max, "messages": 1, "banned": 0}
        usr = spams[user_id]
    if usr["banned"] >= int(tm.time()):
        return True
    else:
        if usr["next_time"] >= int(tm.time()):
            if usr["messages"] >= msgs:
                spams[user_id]["banned"] = tm.time() + ban
                return True
        else:
            spams[user_id]["messages"] = 1
            spams[user_id]["next_time"] = int(tm.time()) + _max
    return False


def if_id_in_file(id):
    with open('users_list.txt', mode='r') as f:
        file = f.readlines()
        for string in file:
            strok = string.replace('\n', '').split()
            if strok[0][3:] == str(id):
                return False
        return True
