
from django.shortcuts import render
from .forms import DetailsForm
from .models import StudentDetails


def details_form(request):
    if request.method == "POST":
        form = DetailsForm(request.POST)

        if form.is_valid():
            rollno = form.cleaned_data["rollno"]

            if StudentDetails.objects.filter(rollno=rollno).exists():
                form.add_error(
                    "rollno",
                    "This Roll No is already registered."
                )
            else:
                StudentDetails.objects.create(
                    rollno=rollno,
                    name=form.cleaned_data["name"],
                    email=form.cleaned_data["email"],
                    phone=form.cleaned_data["phone"],
                    address=form.cleaned_data["address"],
                    course=form.cleaned_data["course"],
                )

                return render(request, "details/success.html")
    else:
        form = DetailsForm()

    return render(
        request,
        "details/details_form.html",
        {"form": form},
    )
