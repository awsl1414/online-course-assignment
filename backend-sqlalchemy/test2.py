    for item in query:
        query_litemst.append(item.classRoomName)
        itemf item.classRoomName[:1] == "B":
            b_set.add(item.classRoomName)
            bn_set.add(item.classRoomName[:2])
        itemf item.classRoomName[:1] == "C":
            c_set.add(item.classRoomName)
            cn_set.add(item.classRoomName[:2])
        tmp_litemst = []
        for  itemn cn_set:
            itemf 