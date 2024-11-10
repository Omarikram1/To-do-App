from pyexpat.errors import messages
from urllib import request
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Tasks
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.contrib import messages
import datetime

# Create your views here.


from django.shortcuts import render

def landingpage(request):
    return render(request, 'landingpage.html')



def signuppage(request):
    
    
    if (request.method == 'POST'):
       
        email = request.POST.get('email')
        print(email)
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                print("hello")
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request,user)
                return redirect('home')
            except Exception as e:
                messages.error(request, f"Error: {e}")
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'signuppage.html')



def loginpage(request):
    
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password') 
        print (username) 
        print (password)  
        user = authenticate(request,username=username ,password = password)
       
        if user is not None:
        
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    
    return render(request, 'loginpage.html')
    







# def homepage(request):
#     user = request.user 
#     task = Tasks.objects.filter(user = user)
#     context = {
#         'user' : user,
#         'tasks' : task
#     }


#     return render(request,'homepage.html',context)



def homepage(request):
    # Get the query parameter 'show_incomplete' from the URL
    show_incomplete = request.GET.get('show_incomplete', 'false') == 'true'

    if show_incomplete:
        # If the checkbox is checked, filter tasks to show only incomplete ones
        tasks = Tasks.objects.filter(user=request.user, completed=False)
    else:
        # Otherwise, show all tasks
        tasks = Tasks.objects.filter(user=request.user)

    context = {
        'user': request.user,
        'tasks': tasks,
        'show_incomplete': show_incomplete,  # Pass the filter state to the template
    }

    return render(request, 'homepage.html', context)
  


def addtask(request):
    if (request.method == 'POST'):
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Tasks.objects.create(user=request.user, title=title, description=description)
        # task.save()
        print(task)
        print("saved")
        return redirect('home')  
    return render(request,'addtask.html')
  

def deletetask(request,task_id):
    
    task = get_object_or_404(Tasks, id=task_id, user=request.user)  # Ensure task belongs to the user
    task.delete()
    return redirect('home')


def updatetask(request, task_id):
    task = get_object_or_404(Tasks, id=task_id, user=request.user)

    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        current_date = datetime.date.today()  
        # Update the task with the new data
        task.title = new_title
        task.description = new_description
        task.created_at = current_date
        task.save()

        return redirect('home')  # Redirect back to the homepage after updating

    # If GET request, pre-fill the form with the current task data
    context = {
        'task': task
    }
    return render(request, 'updatetask.html', context)




def taskcompleted(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    
    if request.method == "POST":
        task = get_object_or_404(Tasks, id=task_id)
        task.completed = not task.completed
        task.save()
        print("Hello")
        return JsonResponse({'status': 'success', 'completed': task.completed})

    return JsonResponse({'status': 'failed'})