# I import three views generic ready: ListView (shows a list the obj), CreateView (show the process a form the create), DetailView (generic view what show the details a object), UpdateView the view generic what show process a form.
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

# I import cars models in Car, The view need use model.
from cars.models import Car, Brand

# I import the form CarModelForm, what created from model Car
from cars.forms import CarModelForm


# I create class CarsListView: Inherit  the ListView make django fetch it obj and put together the list on my own
class CarListView(ListView):
    # I specify which model the list will display
    model = Car
    # I specify which HTML template will be used to display the list
    template_name = "cars.html"
    context_object_name = "cars"
    # I specify the name of the variable that the HTML will receive (the {% for car in cars %} uses this name)
    paginate_by = 6

    # I overrode get_queryset, which is the method that decides WHICH cars are included in the list
    def get_queryset(self):
        # I call the original get_queryset (which returns all cars) using super() and sort by model (A to Z)
        cars = super().get_queryset()
        # I retrieve the search, brand and order text from the URL; within the class, the request is stored in self.request
        search = self.request.GET.get("search")
        brand = self.request.GET.get("brand")
        order = self.request.GET.get("order")
        # I verific if exists some text the search
        if search:
            # I filter the list is which already order, ignored MAX and MIN
            cars = cars.filter(model__icontains=search)
        if brand:
            cars = cars.filter(brand_id=brand)

        allowed_orders = {
            "model": "model",
            "value_asc": "value",
            "value_desc": "-value",
            "year_desc": "-factory_year",
        }
        cars = cars.order_by(allowed_orders.get(order, "model"))
        # I return the list end the cras
        return cars

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all().order_by("name")
        return context


# I create a class CarDetailView: Inherit the DetaiView do the django search a car in bank and send for template
class CarDetailView(DetailView):
    # I specify which model will search
    model = Car
    # I say which template HTML show the details car.
    template_name = "car_detail.html"


# I aplicate protection in class int: the name="dispatch" to do decorate to apply for any type for order (GET, POST...)
# The login_url="login" it says, if the person not is logged in, she is routed to the path nicknamed "login"
@method_decorator(login_required(login_url="login"), name="dispatch")
# I create the class NewCreateView: Inherit the CreateView aready the django to take car alone
class NewCarCreateView(CreateView):
    # I specify which model is to go create.
    model = Car
    # I specify which form used
    form_class = CarModelForm
    # I specify which HTML template will be form
    template_name = "new_car.html"
    # I specify for from the person will be after save with sucess
    success_url = "/cars/"


@method_decorator(login_required(login_url="login"), name="dispatch")
# I create class CarUpdateView: Inherit the UpdateView do the django search car, to fill in form with he date and save the alt.
class CarUpdateView(UpdateView):
    # I say which model to go is edit.
    model = Car
    # I say which form use
    form_class = CarModelForm
    # I say which tempalte HTML show.
    template_name = "car_update.html"
    # I say for where person to go after the save with sucess.
    success_url = "/cars/"

    # I create the get_success_url, what django calls late the to know save for where take the person.
    def get_success_url(self):
        # I to take person for the page details car what finished edit. self.object is car adited and the pk he is the id what route need.
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url="login"), name="dispatch")
# I create the class CarDeleteView: Inherit DeleteView do the djando search car, show page the comfirm and delete which person confirm.
class CarDeleteView(DeleteView):
    # I say what model to go is delete
    model = Car
    # I say which template HTML show
    template_name = "car_delete.html"
    # I say for where the person to go after the delete.
    success_url = "/cars/"
