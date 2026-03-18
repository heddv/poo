from grid import Grid
import random
from config import *
from elements import *



class PlanetAlpha(Grid):

    NORTH, EAST, SOUTH, WEST = (-1, 0), (0, 1), (1, 0), (0, 1)
    NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST = (-1, 1), (1, 1),(1, -1),(-1, -1) 
    CARDINAL_POINTS = (NORTH, EAST, SOUTH, WEST)
    WIND_ROSE = (NORTH,NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST,NORTH_WEST)

    def __init__ (self,name,longitude_cells_count, latitude_cells_count, ground):
        self.__name=name
        grid_init = [[ground] * longitude_cells_count for _ in range(latitude_cells_count)]
        Grid.__init__(self, grid_init)
        self.__current_animals_count = 0
        self.__ground = ground


    def get_name(self):
        return self.__name
    
    def get_current_animals_count(self):
        return self.__current_animals_count

    def incr_current_animals_count(self):
        self.__current_animals_count+=1

    def decr_current_animals_count(self):
        self.__current_animals_count-=1

    def get_ground(self):
        return self.__ground

    def is_free_place(self, cell_number):
        if self.get_cell(cell_number)==None :
            return True
        else : return False
        
    def get_random_free__place(self):
        for i in range(self.columns_count*self.lines_count-1):
            x=random.randint(0,self.columns_count*self.lines_count-1)
            if self.is_free_place(x):
                return x
        return -1

    def place_resources(self, list):
        for el in list:
            x=self.get_random_free__place()
            if x>0:
                self.set_cell(x,el)

    def place_animals(self,list):
        for el in list:
            x=self.get_random_free__place()
            if x>0:
                self.set_cell(x,el)

    def get_grid_char_repr(self):
        grid_char= [[Ground()] * PLANET_LONGITUDE_CELLS_COUNT for _ in range(PLANET_LATITUDE_CELLS_COUNT)]
        for lat in range(PLANET_LATITUDE_CELLS_COUNT):
            for lon in range(PLANET_LONGITUDE_CELLS_COUNT):
                grid_el=self.get_cell_number_from_coordinates(lat,lon)
                grid_char[lat][lon]=(grid_el.get_char_repr())
        return grid_char


    def get_count(self, value):
        pass

    def has_equal_values(self, value):
        pass

    def get_same_value_cell_numbers(self, value):
        pass

    def get_line_str(self, line_number, separator):
        pass

    def draw_with_turtle(self, cell_size, margin, show_values):
        pass











    
