# Model
class FilmMode:
    def __init__(self):
        self.films = []

    def add_film(self, title, genre, author, year, duration, studio, actors):
        film = {
            "title": title,
            "genre": genre,
            "author": author,
            "year": year,
            "duration": duration,
            "studio": studio,
            "actors": actors
        }
        self.films.append(film)
        return film

    def check_list(self):
        return self.films

    def get_film_by_title(self, title):
        for film in self.films:
            if film['title'].lower == title.lower: # Непонятно почему не работает (222)
                return film
            return None

    def delete_film(self, title):
        film = self.get_film_by_title(title)
        if film:
            self.films.remove(film)
            return True
        return False



class FilmView:
    def display_film(self, film):
        if film:
            print(f"Информация о фильме: \n"
                  f"Название: {film['title']}\n"
                  f"Жанр: {film['genre']}\n"
                  f"Режисёр: {film['author']}\n"
                  f"Год выпуска: {film['year']}\n"
                  f"Длительноть: {film['duration']}\n"
                  f"Студия: {film['studio']}\n"
                  f"Актёры: {film['actors']}\n")
            for actrs in film['actors']:
                print(f"{actrs}")

    def display_all_films(self, films):
        print("Список всех фильмов: ")
        for i, film in enumerate(films):
            print(f"{i}, {film['title']} {film['year']}")

    def display_massage(self, massage):
        print(massage)



# Controller
class FilmController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_film(self, title, genre, author, year, duration, studio, actors):
        film = self.model.add_film(title, genre, author, year, duration, studio, actors)
        self.view.display_massage(f"Фильм {title} добавлен успешно")

    def show_all_films(self):
        films = self.model.get_all_films()
        self.view.display_all_films()

    def show_film(self, title):
        film = self.model.get_film_by_title(title)
        self.view.display_film(film)

    def delete_film(self, title):
        result = self.model.delete_film(title)
        if result:
            self.view.display_massage(f"Фильм {title} удалён")
        else:
            self.view.display_massage(f"Фильм {title} не найден")

# if __name__ == "__main__":
#     model = FilmMode()
#     view = FilmView()
#     controller = FilmController(model, view)
#
#     controller.add_film("Дикий дик", "2", "3", "4", "5", "6", "7")
#     controller.add_film("Семёрка", "8", "9", "10", "11", "12", "13")
#
#     controller.show_film("дикий дик")



# # Плохой код
# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def save_ti_db(self):
#         print(f"Save {self.name} in DB")
#
#     def sand_email(self):
#         print(f"Sand wail {self.name}")
#
# # Правильный код
# class User1:
#     def __init__(self, name):
#         self.name = name
#
# class UserDB:
#     def save(self, user):
#         print(f"Saved {user.name} in DB")
#
# class EmailSander:
#     def send(self, user):
#         print(f"Sand mail {user.name} in DB")



# # Плохой код
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# class AreaCulc:
#     def calculate(self, shape):
#         if isinstance(shape, Rectangle):
#             return shape.width * shape.height
#
# # Хороший код
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Rectangle1(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.1415 * self.radius**2



# # Плохой код
# class Bird:
#     def fly(self):
#         print("Bird is fly")
#
# class Penguin(Bird):
#     def fly(self):
#         raise Exception("Pinguin is can not fly")

# # Хороший код
# class Bird:
#     pass
#
# class FlyingBird(Bird):
#     def fly(self):
#         print("Bird is fly")
#
# class Penguin(Bird):
#     def swim(self):
#         print("Penguin is swim now")



# # Плохой код
# class Worker:
#     def work(self):
#         print("Worker")
#
#     def eat(self):
#         print("Eating")
#
# class Robot(Worker):
#     def eat(self):
#         raise Exception("Robots do not need to eat")
#
# # Хороший код
# class Workable:
#     def work(self):
#         pass
#
# class Eateable:
#     def eat(self):
#         pass
#
# class Human(Workable, Eateable):
#     def work(self):
#         print("Human is worked")
#
#     def eat(self):
#         print("Human is eat now")
#
# class Robot1(Workable):
#     def work(self):
#         print("Robot is worked")



# # Плохой код
# class LigthBlub:
#     def turn_on(self):
#         print("Light is on")
#
# class Switch:
#     def __init__(self):
#         self.blub = LigthBlub()
#
#     def operator(self):
#         self.blub.turn_on()
#
# # Хороший код
# from abc import ABC, abstractmethod
# class Switchable(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass
#
# class LightBlub1(Switchable):
#     def turn_on(self):
#         print("Blub is on")
#
# class Fan(Switchable):
#     def turn_on(self):
#         print("Fan is spin now")
#
# class Switch1:
#     def __init__(self, device:Switchable):
#         self.device = device
#
#     def operator(self):
#         self.device.turn_on()
#
# blub = LightBlub1()
# switchBlub = Switch1(blub)
#
# switchBlub.operator()
#
# fan = Fan()
# switchFan = Switch1(fan)
#
# switchFan.operator()