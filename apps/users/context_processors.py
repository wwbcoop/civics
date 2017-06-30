from apps.models.models import Initiative
from django.urls import reverse

# current_user_initiative_name_processor

def current_user_hello(request):
    """Injects into global context the name of the Initiative related to the user"""

    current_user = request.user
    current_user_hello = None

    if current_user.is_staff:
        current_user_hello = "<a href='" + reverse('modelforms:create_initiative') + "'>Crea una iniciativa</a>"
    elif current_user.is_authenticated:
        current_user_initiative = Initiative.objects.filter(user=request.user).first()
        current_user_hello = "Hola, "
        if current_user_initiative:
            current_user_hello += "<a href='" + reverse('users:dashboard') + "'>" + current_user_initiative.name + "</a>"
        else:
            current_user_hello = "Hola, <a href='" + reverse('modelforms:create_initiative') + "'>¿creaste tu iniciativa</a>?"

    return { 'current_user_hello' : current_user_hello }
