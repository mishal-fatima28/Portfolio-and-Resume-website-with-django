from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
	
	return render(request, 'index.html')

def contact(request):
	
	return render(request, 'contact.html')



def contact_form(request):

    if request.method == 'POST':
       
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']
        from_email= request.POST['email']
        to_email = 'drshamsulhaqphysio@gmail.com'

        send_mail(from_email, message, subject, [to_email])
        return render(request, 'index.html')


def portfolio(request):
	
	return render(request, 'portfolio.html')

def physio(request):
	
	return render(request, 'physiotherapy.html')

def teacher(request):
	
	return render(request, 'teacher.html')

def career(request):
	
	return render(request, 'career.html')

def camp(request):
	
	return render(request, 'camp.html')

def ac(request):
	
	return render(request, 'ac.html')

def achilles(request):
	
	return render(request, 'achilles.html')

def acl(request):
	
	return render(request, 'acl.html')

def ankle(request):
	
	return render(request, 'ankle.html')

def arthritis(request):
	
	return render(request, 'arthritis.html')

def arthroscopy(request):
	
	return render(request, 'arthroscopy.html')

def backpain(request):
	
	return render(request, 'backpain.html')

def bells(request):
	
	return render(request, 'bells.html')

def bursitis(request):
	
	return render(request, 'bursitis.html')

def carpel(request):
	
	return render(request, 'carpel.html')

def cerebral(request):
	
	return render(request, 'cerebral.html')

def cervicogenic(request):
	
	return render(request, 'cervicogenic.html')

def coccydynia(request):
	
	return render(request, 'coccydynia.html')

def concussion(request):
	
	return render(request, 'concussion.html')

def copd(request):
	
	return render(request, 'copd.html')

def dequervain(request):
	
	return render(request, 'de-quervain.html')

def discherniation(request):
	
	return render(request, 'disc-herniation.html')

def disc(request):
	
	return render(request, 'disc.html')

def dystonia(request):
	
	return render(request, 'dystonia.html')

def erbspalsy(request):
	
	return render(request, 'erbs-palsy.html')

def erectiledysfunction(request):
	
	return render(request, 'erectile-dysfunction.html')

def facetjoint(request):
	
	return render(request, 'facet-joint.html')

def fibromyalgia(request):
	
	return render(request, 'fibromyalgia.html')

def footpain(request):
	
	return render(request, 'foot-pain.html')

def fracture(request):
	
	return render(request, 'fracture.html')

def frozenshoulder(request):
	
	return render(request, 'frozen-shoulder.html')

def golferselbow(request):
	
	return render(request, 'golfers-elbow.html')

def groinstrain(request):
	
	return render(request, 'groin-strain.html')

def guillain(request):
	
	return render(request, 'guillain.html')

def headaches(request):
	
	return render(request, 'headaches.html')


def heartsurgery(request):
	
	return render(request, 'heart-surgery.html')

def heelpain(request):
	
	return render(request, 'heel-pain.html')

def hipreplacement(request):
	
	return render(request, 'hip-replacement.html')








# Create your views here.
