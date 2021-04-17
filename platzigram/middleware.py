''' Instagram middleware catalog'''

# Django
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout


class ProfileCompletitionMiddleware:
    ''' Profile completition middleware. 
    
        Ensures that every user that is interacting with the platform
        has its profile picture and biography.'''
    
    def __init__(self,get_response):
        '''Middleware initialization'''
        self.get_response = get_response

    def __call__(self, request):
        '''Code to be executed for each request before the view is called.'''
        if not request.user.is_anonymous:
            try:
                if request.user.is_staff: 
                    profile = request.user.profile
                    if not profile.picture or not profile.biography:
                        if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                            return redirect('users:update_profile')
            except:
                print('No profile')
                logout(request)
                return render(request, 'users/login.html', {'error': 'User has no profile'})

        response = self.get_response(request)
        return response