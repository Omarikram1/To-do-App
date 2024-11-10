from todoapp.list.models import Tasks
from django.http import JsonResponse


def writetasks(request):
    if request == 'POST':
        data = request.POST
        task = Tasks.object.create(
            user = request.user,
            title = data['title'],
            description = data['description']

        )
        return JsonResponse({'message' : 'Task completed'},status = 201)
    

def readtask(request):
    if request == 'POST':
        data = Tasks.objects.filter(user = request.user)
        return JsonResponse({
        'title' : data['title'],
        'description' : data['description'],
           
        }) #Agar nai logic smaj ati to chatgpt wala use krlo
    
def updatetask(request):
    if request == 'POST':
        data = request.POST
        user =  Tasks.objects.filter(user = request.user)
        user.title = data['title']
        user.description = data['description']

        user.save
        return JsonResponse({'message': 'Task updated successfully'},status = 201)
    
def deletetask(request):
    if request == 'POST':
        Tasks.objects.delete(user = request.user)
        return JsonResponse({'message': 'Task deleted successfully'},status = 201)



        