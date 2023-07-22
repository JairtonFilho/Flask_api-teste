class CourseEntity:
    def __init__(self, name, description, publication_date, formation):
        self.name = name
        self.description = description
        self.publication_date = publication_date
        self.formation = formation

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
    def publication_date(self):
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        self._publication_date = publication_date

    @property
    def formation(self):
        return self._formation

    @formation.setter
    def formation(self, formation):
        self._formation = formation
