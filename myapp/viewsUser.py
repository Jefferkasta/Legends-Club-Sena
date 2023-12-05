from django.shortcuts import render, get_object_or_404, redirect
from loginUser.models import User
from .forms import UserForm


# def profileUser(request):  
#     return render(request, 'profileUser.html')


def detalle_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('detalle_usuario', usuario_id=usuario_id)
    else:
        form = UserForm(instance=usuario)
    
    return render(request, 'profileUser.html', {'form': form, 'usuario': usuario})