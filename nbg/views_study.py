# -*- coding: utf-8 -*-

from datetime import date as datetime_date
from nbg.models import Campus, Building, RoomAvailability
from nbg.helpers import listify_int, json_response

@json_response
def building_list(request):
    campus_id = int(request.GET.get('campus_id', 0))

    try:
        campus = Campus.objects.get(pk=campus_id)
    except Campus.DoesNotExist:
        return {'error_code': 'CampusNotFound'}, 404

    buildings = campus.building_set.all()
    response = [{
        'id': building.id,
        'name': building.name,
        'location': {
            'latitude': float(building.latitude),
            'longitude': float(building.longitude),
        },
    } for building in buildings]
    return response

@json_response
def room_list(request, offset):
    # TODO: need optimizaiton
    building_id = int(offset)
    date = request.GET.get('date', datetime_date.today())

    try:
        building = Building.objects.get(pk=building_id)
    except Building.DoesNotExist:
        return {'error_code': 'BuildingNotFound'}, 404

    room_objs = building.room_set.all()
    response = []
    for room in room_objs:
        try:
            availability = listify_int(room.roomavailability_set.get(date=date).availability)
        except RoomAvailability.DoesNotExist:
            availability = []

        item = {
            'id': room.id,
            'name': room.name,
            'availability': availability,
        }
        response.append(item)
    return response

