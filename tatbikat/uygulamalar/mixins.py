from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class MumtazMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return self.request.user.mumtaz