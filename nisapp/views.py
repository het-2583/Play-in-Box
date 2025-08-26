from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView
from nisapp.form import LoginForm,SignUpForm
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import addGround
from .models import booking
from .models import UserModel
from .models import tournament
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from nisapp.form import TeamForm


# Create your views here.



def home(request):
    return render(request,'homepage.html')

def organizer_dashboard(request):
    return render(request,'organizer_dashboard.html')

def owner_dashboard(request):
    return render(request,'owner_dashboard.html')

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new user account
            user = form.save()

            # Set the 'type' field to 'organizer'
            user.type = 'organizer'
            user.save()

            # Log in the user
            login(request, user)

            return render(request,'homepage.html')  # Redirect to the user's profile page after successful registration
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

# class owner_SignUp(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'register_owner.html'
#     def form_valid(self, form):
#         # Call the parent class's form_valid method to save the user instance
#         response = super().form_valid(form)

#         # Add the 'type' field to the user instance
#         self.object.type = 'owner'
#         self.object.save()

#         # Return the response
#         return response


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.type=="organizer":
                login(request, user)
                return redirect('organizer_dashboard')
            elif user is not None and user.type=="owner":
                login(request, user)
                return redirect('owner_dashboard')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def viewCategory(request):
#dictionary for initial data with
#field names as keys
 context={}
#add the dictionary during initialization
 context["categories"]=CategoryModel.objects.all()
 return render(request,"view.html",context)       


def view_ground(request):
#dictionary for initial data with
#field names as keys
 context={}
#add the dictionary during initialization
 context["grounds"]=addGround.objects.all()
 return render(request,"view_grounds.html",context)   


def addCategory(request):
    #dictionary for initial data with
    #field names as keys
    context={}
    #add the dictionary during initailization
    form=CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,'Successfully Created.')
        return redirect("viewCategory")
    context['form']=form
    return render(request,"add.html",context)

def deleteCategory(request, id):
    #dictionary for initial data with
    #field names as keys
    context ={}
    #fetch the object related to passed id
    obj=get_object_or_404(CategoryModel,id= id)
    obj.delete()
    return redirect("viewCategory")

def updateCategory(request, id):
    context={}
    #fetch the object related to passed id
    obj = get_object_or_404(CategoryModel, id = id)
    #pass te object as instance form
    form = CategoryForm(request.POST or None,
                        instance= obj)
    #save the data from the form and redirect to detailed view
    if form.is_valid():
        form.save()
        return redirect("viewCategory")
    #add form dictionary to context
    context["form"] = form
    return render(request, "edit.html", context)

def bulk_upload(request):
     return render(request,"bulkUpload.html")

def upload_csv(request):
     
     if("GET" == request.method):
          return HttpResponse("Not Valid method")
     
     csv_file=request.FILES["csv_file"]
     if not csv_file.name.endswith('.csv'):
          return HttpResponse("File not valid")
     if csv_file.multiple_chunks():
          return HttpResponse("Uploaded file is big")
     file_data = csv_file.read().decode("utf-8")
     lines = file_data.split("\n")
     c=len(lines)
     #return Httpresponse(lines[0])
     for i in range(0,c-1):
          feilds = lines[i].split(",")
          data_dict = {}
          data_dict["title"] = feilds[0]
          data_dict["description"] = feilds[1]

          cform=CategoryForm(data_dict)
          if cform.is_valid():
               cform.save()

     return redirect("viewCategory")



def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="category.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Title', 'Description'])  # Use writer.writerow(), not writer.writerrow()

    for data in CategoryModel.objects.all():
        writer.writerow([data.title, data.description])

        return response



def add_ground(request,user_id):
    if request.method == 'POST':
        user_instance = get_object_or_404(UserModel, id=user_id)
        box_name = request.POST.get('box_name')
        location = request.POST.get('location')
        timings  = request.POST.get('timings')
        image    = request.FILES['image']

        # Save the donation to the database (RestaurantDonation model)
        addGround.objects.create(
            owner_id=user_instance,
            box_name=box_name,
            location=location,
            timings=timings,
            image=image
        )
    return render(request,'add_ground.html')



def book_ground(request,user_id,gid):
    if request.method == 'POST':
        user_instance = get_object_or_404(UserModel, id=user_id)
        ground_instance = get_object_or_404(addGround, id=gid)
        sports    = request.POST.get('sports')
        day       = request.POST.get('day')
        time      = request.POST.get('time')
        hours     = request.POST.get('hours')

        # Save the donation to the database (RestaurantDonation model)
        booking.objects.create(
             user_id=user_instance,  # Assign the user_id argument
             ground_id=ground_instance,
             sports=sports,
             day=day,
             time=time,
             hours=hours
        )
    return render(request,'book.html')

def profile(request):
   return render(request,"profile.html",)


def ground_details(request, id):

    #fetch the object related to passed id
    details = addGround.objects.get(id=id)
    context = {
        'details': details,  # Pass the ground object to the template
    }
    #save the data from the form and redirect to detailed view
 
    return render(request, "details.html", context)


def add_tournament(request, user_id):
    if request.method == 'POST':
        user_instance = get_object_or_404(UserModel, id=user_id)

        # Check if 'image' key exists in request.FILES
        if 'image' in request.FILES:
            logo_image = request.FILES['image']
            tournament_name = request.POST.get('tournament_name')
            city = request.POST.get('city')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            category = request.POST.get('category')
            ball_type = request.POST.get('ball_type')
            pitch_type = request.POST.get('pitch_type')

            # Save the tournament to the database
            tournament.objects.create(
                user_id=user_instance,
                logo=logo_image,
                tournament_name=tournament_name,
                city=city,
                start_date=start_date,
                end_date=end_date,
                category=category,
                ball_type=ball_type,
                pitch_type=pitch_type,
            )

    return render(request, 'add_tournament.html')






def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizer_dashboard')  # Redirect to a list of teams or a success page
    else:
        form = TeamForm()
    
    return render(request, 'add_team.html', {'form': form})
