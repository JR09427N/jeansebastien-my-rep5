from flask import Flask, request, redirect, render_template

import json

def apartment():
    f = open('/home/jr09427n/data/apartments.json')
    apartments = json.load(f)
    f.close()

    search = request.args.get('search', '').lower()
    room = request.args.get('rooms', '').lower()
    sort = request.args.get('sort', '').lower()

    def filter_by_room(apartment, room_filter):
        if room_filter == 'any':
            return True
        elif room_filter == 'one':
            return apartment['bedrooms'] >= 1
        elif room_filter == 'two':
            return apartment['bedrooms'] >= 2
        else:
            return True


    def sort_results(apartments, sort_option):
        if sort_option == 'asc':
            return sorted(apartments, key=lambda x: x["monthly_rent"])
        elif sort_option == 'desc':
            return sorted(apartments, key=lambda x: x["monthly_rent"], reverse=True)
        else:
            return apartments

    result_list = []
    for apartment in apartments:
        title_match = search in apartment['title'].lower()
        description_match = search in apartment['description'].lower()
        room_match = filter_by_room(apartment, room)

        if (title_match or description_match) and room_match:
            result_list.append(apartment)

    sorted_result = sort_results(result_list, sort)
    return {'result': sorted_result}


def check_login():
    # return None

    return {'name':'Sebastien'}

def account():
    user = check_login()
    if user is None:
        return redirect('/')
    else:
        return 'Hello ' + user['name']

def find_course(number):
    number = number.lower()
    f = open('/home/jr09427n/data/courses.json')
    courses = json.load(f)
    f.close()

    for course in courses:
        if course['number'].lower() == number:
            return course

    return {}





















