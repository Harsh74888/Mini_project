# Build Time-table Generator for generating time-table of your class.
# Take into account the availability of professors, classrooms and
# laboratory.
import random

class TimetableGenerator:
    def __init__(self, professors, classrooms, labs, days, periods_per_day):
        self.professors = professors
        self.classrooms = classrooms
        self.labs = labs
        self.days = days
        self.periods_per_day = periods_per_day
        self.timetable = {}

    def generate_timetable(self):
        for day in range(1, self.days + 1):
            for period in range(1, self.periods_per_day + 1):
                professor = random.choice(self.professors)
                classroom = random.choice(self.classrooms)
                lab = random.choice(self.labs)

                if not self.is_slot_available(day, period, professor, classroom, lab):
                    # Retry with a different combination
                    continue

                self.timetable[(day, period)] = {
                    'professor': professor,
                    'classroom': classroom,
                    'lab': lab
                }

    def is_slot_available(self, day, period, professor, classroom, lab):
        # Check if the chosen combination is available
        for (d, p), schedule in self.timetable.items():
            if (
                (d == day and p == period) or
                (schedule['professor'] == professor) or
                (schedule['classroom'] == classroom) or
                (schedule['lab'] == lab)
            ):
                return False
        return True

    def display_timetable(self):
        for (day, period), schedule in self.timetable.items():
            print(f"Day {day}, Period {period}:")
            print(f"Professor: {schedule['professor']}")
            print(f"Classroom: {schedule['classroom']}")
            print(f"Lab: {schedule['lab']}")
            print()

# Example usage:
professors = ['Prof A', 'Prof B', 'Prof C']
classrooms = ['Room 101', 'Room 102', 'Room 103']
labs = ['Lab 1', 'Lab 2']
days = 5  # Assuming 5 days in a week
periods_per_day = 4  # Assuming 4 periods in a day

generator = TimetableGenerator(professors, classrooms, labs, days, periods_per_day)
generator.generate_timetable()
generator.display_timetable()
