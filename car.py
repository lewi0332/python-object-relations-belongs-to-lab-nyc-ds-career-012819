class Car:

    _all = []

    def __init__(self, makes, models, years, owners):
        self._make = makes
        self._model = models
        self._year = years
        self._owner = owners
        Car._all.append(self)
        
    @property    
    def make(self):
        return self._make
    
    @make.setter
    def make(self, makes):
        self._make = makes
    
    @make.deleter
    def make(self):
        del self._make
        
    @property    
    def model(self):
        return self._model
    
    @model.setter
    def model(self, models):
        self._model = models
    
    @model.deleter
    def model(self):
        del self._model
        
    @property    
    def year(self):
        return self._year
    
    @year.setter
    def year(self, years):
        self._year = years
        
    @year.deleter
    def year(self):
        del self._year
    
    @property    
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owners):
        self._owner = owners
        
    @owner.deleter
    def owner(self):
        del self._owner
        
    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def cars_driven_by(cls, occupation):
        cars = []
        for car in cls.all():
            if car.owner.occupation == occupation:
                cars.append(car)
        return cars
