import tkinter as tk

class event():
    def __init__(self, events, window):
        assert type(events) == dict, 'events must be a dictionary containing the key \n and function which does something when the key is pressed, \nexample: \nevents = {\n"Up", onkeyup\n}'
        for event in events:
            window.bind(f"<{event}>", events[event])
