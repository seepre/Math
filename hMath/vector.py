class Vector:
    def __init__(self,lst):
        self._values = lst

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values[item]

    def __repr__(self):
        return "Vector:({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

