from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def home(request):
	try:
		print("home...")
		if request.method == 'POST':
			print("request -- ", request.POST)

			first_name = request.POST.get("firstname")
			last_name = request.POST.get("lastname")
			username = request.POST.get("username")
			email = request.POST.get("email")
			contact = request.POST.get("contact")
			myfile = request.FILES['profileimage']
			password = request.POST.get("password")

			# fs = FileSystemStorage()
			# filename = fs.save(myfile.name, myfile)
			user = User.objects.create_user(username, email, password)
			print("$$$", user.id)
			user_obj = user.save()
			print("user_obj", user_obj)
			profile = Profile(user,user.id, myfile.name, contact)
			# print("###",profile)
			profile.save()
		return render(request, 'index.html')
	except Exception as ex:
		print(ex)
		return render(request, 'index.html')



