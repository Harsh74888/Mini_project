# Build Time-table Generator for generating time-table of your class.
# Take into account the availability of professors, classrooms and
# laboratory.
import random

class TimetableGenerator:
    def __init__(self, professors, classrooms, laboratories, days_of_week, time_slots):
        self.professors = professors
        self.classrooms = classrooms
        self.laboratories = laboratories
        self.days_of_week = days_of_week
        self.time_slots = time_slots
        self.timetable = {}

    def generate_timetable(self):
        for day in self.days_of_week:
            for professor, subjects in self.professors.items():
                for subject in subjects:
                    for time_slot in self.time_slots:
                        # Skip lunch break time slot
                        if "1:00 PM - 2:00 PM" in time_slot and "Lunch" not in subjects:
                            continue

                        room = self.get_available_room(subject)
                        if room:
                            key = (day, time_slot)
                            self.timetable[key] = (professor, subject, room)

    def get_available_room(self, subject):
        if "Lab" in subject:
            available_rooms = self.laboratories
        else:
            available_rooms = self.classrooms

        random.shuffle(available_rooms)

        for room in available_rooms:
            if self.is_room_available(room):
                return room

        return None

    def is_room_available(self, room):
        return room not in [r for (_, _, r) in self.timetable.values()]

    def display_timetable(self):
        print("Complete Timetable:")
        for day in self.days_of_week:
            print(f"\n{day}:")
            for time_slot in self.time_slots:
                key = (day, time_slot)
                if key in self.timetable:
                    professor, subject, room = self.timetable[key]
                    print(f"{time_slot}: Professor {professor} - Subject {subject} - Room {room}")


professors = {
    "Nemi sir": ["Python", "IKS" ],
    "Piyush sir": ["HVPE", "AI", "Maths"],
    "jaynath sir": ["DAA" ]
}

classrooms = ["218", "219"]
laboratories = [" Lab1"]

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_slots = ["10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM", "12:00 PM - 1:00 PM",
              "1:00 PM - 2:00 PM", "2:00 PM - 3:00 PM", "3:00 PM - 4:00 PM"]

generator = TimetableGenerator(professors, classrooms, laboratories, days_of_week, time_slots)
generator.generate_timetable()
generator.display_timetable()



