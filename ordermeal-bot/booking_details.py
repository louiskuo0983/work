# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


class BookingDetails:
    def __init__(
        self,
        destination: str = None,
        origin: str = None,
        travel_date: str = None,
        leave_date: str = None,
        meal: str = None,
        drink: str = None,
        payment: str = None,
            unsupported_airports=None,
    ):
        if unsupported_airports is None:
            unsupported_airports = []
        self.destination = destination
        self.origin = origin
        self.travel_date = travel_date
        self.leave_date = leave_date
        self.meal = meal
        self.drink = drink
        self.payment = payment
        self.unsupported_airports = unsupported_airports
