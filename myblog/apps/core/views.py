from django.shortcuts import redirect
from django.views.generic import FormView

from core.forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = '/'

    @staticmethod
    def send_email(email, message):
        pass

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            fake_field = form.cleaned_data.get('subject_1', '')
            # Check if the fake field is filled or not to detect bot.
            if len(fake_field) == 0:
                self.send_email(
                    email=form.cleaned_data.get('email_alt'),
                    message=form.cleaned_data.get('message')
                )

            else:
                pass
        else:
            pass

        # This will prevent blank form submission on page refresh.
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
