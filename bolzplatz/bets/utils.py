from django.http import HttpResponseRedirect


class BetFormValidMixin:

    def bet_valid(self, bet):
        self.object = bet.save(self.request)
        return HttpResponseRedirect(
            self.get_success_url())