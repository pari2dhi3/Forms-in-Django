from django.shortcuts import render

def form_manual(request):
	data = {}
	if request.method == 'POST':
		data['movie'] = request.POST.get('movie','Movie not found')

	return render(request,'core/index.html', data)

# Create your views here.
