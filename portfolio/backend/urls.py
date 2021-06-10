from django.urls import path
from .views import AllUsersView, BasicUserCRView, BasicUserRUDView, \
                    EmployeeCRView, EmployeeRUDView, DirectorCRView, \
                    DirectorRUDView, CEOCRView, CEORUDView

app_name = 'backend'

urlpatterns = [
    path('view-users', AllUsersView.as_view()),
    path('user', BasicUserCRView.as_view()),
    path('user/<int:pk>', BasicUserRUDView.as_view()),
    path('user/employee', EmployeeCRView.as_view()),
    path('user/employee/<int:pk>', EmployeeRUDView.as_view()),
    path('user/employee/director', DirectorCRView.as_view()),
    path('user/employee/director/<int:pk>', DirectorRUDView.as_view()),
    path('user/employee/ceo', CEOCRView.as_view()),
    path('user/employee/ceo/<int:pk>', CEORUDView.as_view())
]
