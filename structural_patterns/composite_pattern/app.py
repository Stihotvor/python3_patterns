# Widget gives You an ability to safe couple of code lines when we have to provide empty return in numerous classes
class Widget:
    def children(self):
        return []


# Frame has children and provide them once called
class Frame(Widget):
    def __init__(self, child_widgets):
        self.child_widgets = child_widgets

    def children(self):
        return self.child_widgets


# Label has no children in code implementation, but symmetrically returns empty list aka "no children"
class Label:
    def __init__(self, text):
        self.text = text
