
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
                    if character.isalnum()
                )[:4]

                prefix = prefix or "USER"

                # Save the registration and generate a unique enrollment ID
                for _ in range(20):
                    enrollment_id = (
                        f"{prefix}{secrets.randbelow(9000) + 1000}"
                    )

                    try:
                        with transaction.atomic():
                            student = StudentDetails.objects.create(
                                rollno=rollno,
                                name=candidate_name,
                                email=form.cleaned_data["email"],
                                phone=form.cleaned_data["phone"],
                                address=form.cleaned_data["address"],
                                course=form.cleaned_data["course"],
                            )

                            # Requires enrollment_id field in your model
                            student.enrollment_id = enrollment_id
                            student.save(update_fields=["enrollment_id"])

                        break

                    except IntegrityError:
                        # Retry if the enrollment ID already exists
                        continue
                else:
                    form.add_error(
                        None,
                        "Unable to generate an enrollment ID. Please try again."
                    )

                if not form.errors:
                    return render(
                        request,
                        "details/success.html",
                        {
                            "enrollment_id": student.enrollment_id,
                        }
                    )

    else:
        form = DetailsForm()

    return render(
        request,
        "details/details_form.html",
        {"form": form},
    )
