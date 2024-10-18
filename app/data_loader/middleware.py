from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class LoginRequiredMiddleware:
    """
    Middleware que requer que todos os usuários estejam autenticados para acessar qualquer página,
    exceto a página de login, página de registro, e outras URLs definidas como isentas.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL
        # URLs que não requerem login
        self.exempt_urls = [
            reverse('login'),
            reverse('admin:login'),
            # Adicione outras URLs que não devem requerer autenticação
            # Exemplo: reverse('signup'), reverse('password_reset'),
        ]

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info
            if not any(path.startswith(url) for url in self.exempt_urls):
                return redirect(f"{self.login_url}?next={path}")
        return self.get_response(request)
