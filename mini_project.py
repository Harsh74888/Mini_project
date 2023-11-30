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
            for time_slot in self.time_slots:
                professors_list = list(self.professors.keys())
                random.shuffle(professors_list)
                for professor in professors_list:
                    if not ("1:00 PM - 2:00 PM" in time_slot and "Lunch" not in self.professors[professor]):
                        subjects = self.professors[professor]
                        subject = self.get_subject_for_professor(professor, subjects)
                        room = self.get_available_room(day, time_slot, subject)
                        if room:
                            key = (day, time_slot)
                            self.timetable[key] = (day, subject, professor, room)

    def get_subject_for_professor(self, professor, subjects):
        if professor == "Nemi sir" and "Python" in subjects:
            return "Python"
        return random.choice(subjects)

    def get_available_room(self, day, time_slot, subject):
        if subject.startswith("Lab"):
            available_rooms = self.laboratories
        else:
            available_rooms = self.classrooms

        assigned_rooms = set(r for (_, _, _, r) in self.timetable.values() if _ == day and _ == time_slot)
        available_rooms = list(set(available_rooms) - assigned_rooms)

        return random.choice(available_rooms) if available_rooms else None

    def display_timetable(self):
        print("Complete Timetable:")
        for day in self.days_of_week:
            print(f"\n{day}:")
            for time_slot in self.time_slots:
                key = (day, time_slot)
                if key in self.timetable:
                    _, subject, professor, room = self.timetable[key]
                    print(f"{time_slot}: Professor {professor} - Subject {subject} - Room {room}")

# Example usage
professors = {
    "Nemi sir": ["Python", "IKS"],
    "Piyush sir": ["HVPE", "AI", "Maths"],
    "Jaynath sir": ["DAA"]
}

classrooms = ["218", "219"]
laboratories = ["Lab1"]

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_slots = ["10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM", "12:00 PM - 1:00 PM",
              "1:00 PM - 2:00 PM", "2:00 PM - 3:00 PM", "3:00 PM - 4:00 PM"]

generator = TimetableGenerator(professors, classrooms, laboratories, days_of_week, time_slots)
generator.generate_timetable()
generator.display_timetable()
