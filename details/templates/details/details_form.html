
from django.shortcuts import render
from django.db import IntegrityError, transaction
from .forms import DetailsForm
from .models import StudentDetails
import secrets


def details_form(request):
    if request.method == "POST":
        form = DetailsForm(request.POST)

        if form.is_valid():
            rollno = form.cleaned_data["rollno"]

            # Check for duplicate Roll Number
            if StudentDetails.objects.filter(rollno=rollno).exists():
                form.add_error(
                    "rollno",
                    "This Roll No is already registered."
                )

            else:
                candidate_name = form.cleaned_data["name"].strip()
                first_name = candidate_name.split()[0]

                # First four letters of the first name
                prefix = "".join(
                    character
                    for character in first_name.upper()
                    if character.isalpha()
                )[:4]

                # Handle names shorter than four letters
                prefix = prefix.ljust(4, "X")

                student = None

                # Generate and save a unique enrollment ID
                for _ in range(20):
                    digits = f"{secrets.randbelow(10000):04d}"
                    enrollment_id = f"{prefix}{digits}"

                    try:
                        with transaction.atomic():
                            student = StudentDetails.objects.create(
                                rollno=rollno,
                                name=candidate_name,
                                email=form.cleaned_data["email"],
                                phone=form.cleaned_data["phone"],
                                address=form.cleaned_data["address"],
                                course=form.cleaned_data["course"],
                                enrollment_id=enrollment_id,
                            )

                        break

                    except IntegrityError:
                        # Retry if the enrollment ID already exists
                        continue

                if student is not None:
                    return render(
                        request,
                        "details/success.html",
                        {
                            "enrollment_id": student.enrollment_id,
                        }
                    )

                form.add_error(
                    None,
                    "Unable to generate a unique enrollment ID. Please try again."
                )

    else:
        form = DetailsForm()

    return render(
        request,
        "details/details_form.html",
        {"form": form},
    )
