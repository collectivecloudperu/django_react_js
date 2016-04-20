from django.shortcuts import render

# Vistas
 
def saludo(request):
	autor = "Collective Cloud Perú"
	web = "http://collectivecloudperu.com"
	blog = "http://blog.collectivecloudperu.com"
	titulo = "Entorno de Trabajo con Bootstrap, Django y React JS"
	titulo_video_youtube ="5G y Samsung cambiarán la tecnología móvil."
	video_youtube = "https://www.youtube.com/v/Bx3Xr7IeUmw"
	context = {    	
		'autor': autor,
		'web': web,
		'blog': blog,
		'titulo': titulo,
		'titulo_video_youtube': titulo_video_youtube,
		'video_youtube': video_youtube
	}
	# devolvemos los datos a la vista saludo.html para printarlos
	return render(request, 'index.py', context)