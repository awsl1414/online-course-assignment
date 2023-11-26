def get_computer_room_floor(db: Session, computerRoom: Optional[str] = Query(None)):
    query = db.query(Floors).all()
    floor_set = set()
    c_set = set()
    floor_dict = {}
    for item in query:
        if computerRoom:
            if item[0][:1] == computerRoom[:1]:
                floor_set.add(item[0])
                floor_dict.update({f"{item[0][:1]}": f"{list(floor_set)}"})
        else:
            if item[0][:1] == "B":
                floor_set.add(item[0])
                floor_dict.update({f"{item[0][:1]}": f"{list(floor_set)}"})
            if item[0][:1] == "C":
                c_set.add(item[0])
                floor_dict.update({f"{item[0][:1]}": f"{list(c_set)}"})

    return floor_dict
