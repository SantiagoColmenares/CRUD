from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author


# Create your views here.
def index(request):
  posts = Post.objects.all()

  for obj in posts:
    print(obj.titulo, obj.cuerpo)

  return HttpResponse(f"Lista de posts")


def storageA(request, nombre_A, correo):
  autor = Author(nombre_A = nombre_A, correo = correo)
  autor.save()
  return HttpResponse("Se guardaron los datos del autor")

def storage(request, titulo, cuerpo, autor):
  post = Post(titulo = titulo,cuerpo = cuerpo, autor = Author)
  post.save()
  return HttpResponse("Guardamos los datos")

def consultar(request, id):
  post = Post.objects.get(id=id)
  print(post)
  print(post, post.titulo, post.cuerpo, post.fecha)
  return HttpResponse(f"Nombre: {post.titulo}  Cuerpo: {post.cuerpo}  Fecha: {post.fecha}")

def modificar(request,titulo, id):
  post = Post.objects.get(id=id)
  post.titulo = titulo
  post.save()
  return HttpResponse("hola")

def eliminar(request, id):
  post = Post.objects.get(id=id)
  post.delete()
  return HttpResponse("Se elimino")


