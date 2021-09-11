from core.forms import ContactForm


class ContactFormViewMixin:
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['form'] = ContactForm
        return context_data
