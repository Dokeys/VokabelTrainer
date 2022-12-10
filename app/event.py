# for the observer pattern
subscribers = dict()


def subscribe(event_type: str, fn):  # fn ist die Funktion die aufgerufen werden soll
    if not event_type in subscribers:
        subscribers[event_type] = []  # Falls Event nicht vorhanden erzeugen
    subscribers[event_type].append(fn)  # Funktion zu Event hinzufügen


def post_event(event_type: str, *data):
    if not event_type in subscribers:  # falls sich niemand angemeldet hat
        return
    for fn in subscribers[event_type]:
        if data:
            fn(*data)
        else:
            fn()