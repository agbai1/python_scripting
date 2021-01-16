def party_planner(cookies, people):
    num_of_cookies = None
    cookies_left = None

    try:
        num_of_cookies = cookies // people
        cookies_left = cookies % people

    except ZeroDivisionError:
        print("More than 0 people needs to be attending the party")
        print("Plese enter number of attendees fort the party again")

    return ("Each person gets {} cookies and there will be {} cookies left over").format(num_of_cookies,cookies_left)

print(party_planner(170,0))
