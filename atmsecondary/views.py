from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Instructor, Section, Course, Room, Department, MeetingTime
from . import forms
from .forms import CreateUserForm, AddBatch, AddSubject, TeacherForm, AddClassroom, AddDepartment, AddTimeslots
import random as rnd
import math

POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.05
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'error': "Username or Password is wrong!"
            }
            return render(request, 'login.html', context)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


def log_out(request):
    logout(request)
    return redirect('login')


def dashboard(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    return render(request, 'dashboard.html')


def add_teacher(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    form = TeacherForm()

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_teacher')

    context = {'form': form}
    return render(request, 'add-teacher.html', context=context)


def view_teacher(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    data = Instructor.objects.all()

    context = {
        'data': data,
    }
    return render(request, 'view-teacher-list.html', context=context)


def update_teacher(request, id):
    teacher = Instructor.objects.get(id=id)
    form = TeacherForm(instance=teacher)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('view_teacher')

    context = {'form': form}
    return render(request, 'update-teacher.html', context=context)


def delete_teacher(request, id):
    teacher = Instructor.objects.get(id=id)
    teacher.delete()
    return redirect('view_teacher')


def add_subject(request):
    user = None
    form = AddSubject()
    if request.user.is_authenticated:
        user = request.user

    if request.method == "POST":
        form = AddSubject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_subject')

    context = {"form": form}
    return render(request, 'add-subject.html', context)


def view_subject(request):
    user = None
    if request.user.is_authenticated:
        user = request.user

    data = Course.objects.all()
    context = {"data": data}
    return render(request, 'view-subject.html', context)


def update_subject(request, id):
    subject = Course.objects.get(course_number=id)
    form = AddSubject(instance=subject)

    if request.method == "POST":
        form = AddSubject(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('view_subject')

    context = {"form": form}
    return render(request, 'update-subject.html', context)


def delete_subject(request, id):
    subject = Course.objects.get(course_number=id)
    subject.delete()
    return redirect('view_subject')


def add_classroom(request):
    form = AddClassroom()

    if request.method == "POST":
        form = AddClassroom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_classroom')

    context = {"form": form}
    return render(request, 'add-classroom.html', context)


def view_classroom(request):
    user = None
    if request.user.is_authenticated:
        user = request.user

    data = Room.objects.all()
    context = {"data": data}
    return render(request, 'view-classroom.html', context)


def update_classroom(request, id):
    classroom = Room.objects.get(id=id)
    form = AddClassroom(instance=classroom)

    if request.method == "POST":
        form = AddClassroom(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return redirect('view_classroom')

    context = {"form": form}
    return render(request, 'update-classroom.html', context)


def delete_classroom(request, id):
    classroom = Room.objects.get(id=id)
    classroom.delete()
    return redirect('view_classroom')


def add_batches(request):
    form = AddBatch()

    if request.method == 'POST':
        form = AddBatch(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_batch')
    context = {
        'form': form
    }
    return render(request, 'add-batch.html', context)


def view_batches(request):
    user = None
    if request.user.is_authenticated:
        user = request.user

    data = Section.objects.all()
    context = {'data': data}
    return render(request, 'view-batch.html', context)


def update_batches(request, id):
    batch = Section.objects.get(section_id=id)
    form = forms.AddBatch(instance=batch)

    if request.method == 'POST':
        form = forms.AddBatch(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            return redirect('view_batch')

    context = {'form': form}
    return render(request, 'update-batches.html', context=context)


def delete_batches(request, id):
    batch = Section.objects.get(section_id=id)
    batch.delete()
    return redirect('view_batch')


def add_department(request):
    form = AddDepartment()

    if request.method == 'POST':
        form = AddDepartment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_department')

    context = {'form': form}
    return render(request, 'add-department.html', context)


def view_department(request):
    user = None
    if request.user.is_authenticated:
        user = request.user

    data = Department.objects.all()
    context = {'data': data}
    return render(request, 'view-department.html', context)


def update_department(request, id):
    department = Department.objects.get(id=id)
    form = AddDepartment(instance=department)

    if request.method == 'POST':
        form = AddDepartment(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('view_department')

    context = {'form': form}
    return render(request, 'update-department.html', context)


def delete_department(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    return redirect('view_department')


def add_timeslot(request):
    form = AddTimeslots()

    if request.method == 'POST':
        form = AddTimeslots(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_timeslots')

    context = {'form': form}
    return render(request, 'add-timeslot.html', context)


def view_timeslots(request):
    timeslots = MeetingTime.objects.all()
    context = {'data': timeslots}
    return render(request, 'view-timeslots.html', context)


def update_timeslot(request, id):
    timeslot = MeetingTime.objects.get(pid=id)
    form = AddTimeslots(instance=timeslot)

    if request.method == 'POST':
        form = AddTimeslots(request.POST, instance=timeslot)
        if form.is_valid():
            form.save()
            return redirect('view_timeslots')

    context = {'form': form}
    return render(request, 'update-timeslot.html', context)


def delete_timeslot(request, id):
    timeslot = MeetingTime.objects.get(pid=id)
    timeslot.delete()
    return redirect('view_timeslots')


class Data:
    def __init__(self):
        self._rooms = Room.objects.all()
        self._meetingTimes = MeetingTime.objects.all()
        self._instructors = Instructor.objects.all()
        self._courses = Course.objects.all()
        self._depts = Department.objects.all()

    def get_rooms(self): return self._rooms

    def get_instructors(self): return self._instructors

    def get_courses(self): return self._courses

    def get_depts(self): return self._depts

    def get_meetingTimes(self): return self._meetingTimes


class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numberOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self): return self._numberOfConflicts

    def get_fitness(self):
        if self._isFitnessChanged:
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        sections = Section.objects.all()
        for section in sections:
            dept = section.department
            n = section.num_class_in_week
            if n <= len(MeetingTime.objects.all()):
                courses = dept.courses.all()
                for course in courses:
                    for i in range(n // len(courses)):
                        crs_inst = course.instructors.all()
                        newClass = Class(self._classNumb, dept,
                                         section.section_id, course)
                        self._classNumb += 1
                        newClass.set_meetingTime(data.get_meetingTimes(
                        )[rnd.randrange(0, len(MeetingTime.objects.all()))])
                        newClass.set_room(
                            data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
                        newClass.set_instructor(
                            crs_inst[rnd.randrange(0, len(crs_inst))])
                        self._classes.append(newClass)
            else:
                n = len(MeetingTime.objects.all())
                courses = dept.courses.all()
                for course in courses:
                    for i in range(n // len(courses)):
                        crs_inst = course.instructors.all()
                        newClass = Class(self._classNumb, dept,
                                         section.section_id, course)
                        self._classNumb += 1
                        newClass.set_meetingTime(data.get_meetingTimes(
                        )[rnd.randrange(0, len(MeetingTime.objects.all()))])
                        newClass.set_room(
                            data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
                        newClass.set_instructor(
                            crs_inst[rnd.randrange(0, len(crs_inst))])
                        self._classes.append(newClass)

        return self

    def calculate_fitness(self):
        self._numberOfConflicts = 0
        classes = self.get_classes()
        for i in range(len(classes)):
            if classes[i].room.seating_capacity < int(classes[i].course.max_numb_students):
                self._numberOfConflicts += 1
            for j in range(len(classes)):
                if j >= i:
                    if (classes[i].meeting_time == classes[j].meeting_time) and \
                            (classes[i].section_id != classes[j].section_id) and (classes[i].section == classes[j].section):
                        if classes[i].room == classes[j].room:
                            self._numberOfConflicts += 1
                        if classes[i].instructor == classes[j].instructor:
                            self._numberOfConflicts += 1
        return 1 / (1.0 * self._numberOfConflicts + 1)


class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = [Schedule().initialize() for i in range(size)]

    def get_schedules(self):
        return self._schedules


class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[
                0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[
                0]
            crossover_pop.get_schedules().append(
                self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if rnd.random() > 0.5:
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(len(mutateSchedule.get_classes())):
            if MUTATION_RATE > rnd.random():
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(
                pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop


class Class:
    def __init__(self, id, dept, section, course):
        self.section_id = id
        self.department = dept
        self.course = course
        self.instructor = None
        self.meeting_time = None
        self.room = None
        self.section = section

    def get_id(self): return self.section_id

    def get_dept(self): return self.department

    def get_course(self): return self.course

    def get_instructor(self): return self.instructor

    def get_meetingTime(self): return self.meeting_time

    def get_room(self): return self.room

    def set_instructor(self, instructor): self.instructor = instructor

    def set_meetingTime(self, meetingTime): self.meeting_time = meetingTime

    def set_room(self, room): self.room = room


data = Data()


def context_manager(schedule):
    classes = schedule.get_classes()
    context = []
    cls = {}
    for i in range(len(classes)):
        cls["section"] = classes[i].section_id
        cls['dept'] = classes[i].department.dept_name
        cls['course'] = f'{classes[i].course.course_name} ({classes[i].course.course_number}, ' \
                        f'{classes[i].course.max_numb_students}'
        cls['room'] = f'{classes[i].room.r_number} ({classes[i].room.seating_capacity})'
        cls['instructor'] = f'{classes[i].instructor.name} ({classes[i].instructor.uid})'
        cls['meeting_time'] = [classes[i].meeting_time.pid,
                               classes[i].meeting_time.day, classes[i].meeting_time.time]
        context.append(cls)
    return context


def timetable(request):
    schedule = []
    population = Population(POPULATION_SIZE)
    generation_num = 0
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    geneticAlgorithm = GeneticAlgorithm()
    while population.get_schedules()[0].get_fitness() != 1.0:
        generation_num += 1
        print('\n> Generation #' + str(generation_num))
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        schedule = population.get_schedules()[0].get_classes()

    return render(request, 'gentimetable.html', {'schedule': schedule, 'sections': Section.objects.all(),
                                                 'times': MeetingTime.objects.all()})