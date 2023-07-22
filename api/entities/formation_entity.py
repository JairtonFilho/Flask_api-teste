class FormationEntity:
    def __init__(self, name, description, teachers):
        self.name = name
        self.description = description
        self.teachers = teachers

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def teachers(self):
        return self._teacher

    @teachers.setter
    def teachers(self, teacher):
        self._teacher = teacher
