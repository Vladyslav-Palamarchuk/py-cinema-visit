from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_instances = []
    for c_dict in customers:
        customer_obj = Customer(name=c_dict["name"], food=c_dict["food"])
        customer_instances.append(customer_obj)

        CinemaBar.sell_product(product=customer_obj.food,
                               customer=customer_obj)
        cinema_hall = CinemaHall(hall_number=hall_number)
        cleaner_staff = Cleaner(name=cleaner)

        cinema_hall.movie_session(
            movi_name=movie,
            customers=customer_instances,
            cleaning_staff=cleaner_staff
        )
