from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Student, Instruments


# Create your views here.
def show_all_students(request):
    students = Student.objects.all()
    context = {"students": students}

    return render(request, 'index.html', context=context)


def personal_student_data(request, pk):
    student = get_object_or_404(Student, pk= pk)
    instruments = Instruments.objects.all()
    # instrument = Student.instrument[student.instrument]
    context = {"student": student, 'instruments': instruments}

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.surname = request.POST.get('surname')
        student.age = request.POST.get('age')

        student.performance = request.POST.get('performance')
        if request.POST.get('has_paid') == 'Yes':
            student.has_paid = True
        else:
            student.has_paid = False

        student.instrument.clear()
        instruments = request.POST.getlist('instrument')  # get list of selected instruments
        for instrument in instruments:
            obj = Instruments.objects.get(name=instrument)
            student.instrument.add(obj)  # add selected instruments to student
        student.save()


    return render(request, 'personal_data.html', context=context)