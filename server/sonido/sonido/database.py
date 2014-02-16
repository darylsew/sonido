def returnAll():
    allThings = collection.find()
    things = []
    for current in allThings:
        x = [current['long'],current['lat'],current['amp'],current['freq']]
        if things == None:
            things = [x]
            things.append(x)
    return things
