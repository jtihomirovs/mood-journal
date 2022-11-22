from django.contrib.auth import get_user_model, login, logout

from rest_framework import generics, views, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view


from authentication.serializers import UserSerializer, LoginSerializer, UserProfileSerializer

from django.views.decorators.csrf import csrf_exempt


class UserCreate(generics.CreateAPIView):
    # This view is for user registration
    # This view should be accessible also for unauthenticated users.
    permission_classes = (AllowAny,)

    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data, context={
                                     'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name': user.first_name,
            'last_name': user.last_name,
        }, status=status.HTTP_202_ACCEPTED)


class LogoutView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


@api_view(('GET',))
def check_user_authenticated(request):
    if request.user.is_authenticated:
        return Response(None, status=status.HTTP_200_OK)
    else:
        # axios just get status in range 200-300
        # so in this case 204 is returned instead of 401
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class SessionCheckView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        if request.user.is_authenticated:
            return Response(None, status=status.HTTP_200_OK)
        else:
            # axios just get status in range 200-300
            # so in this case 204 is returned instead of 401
            return Response(None, status=status.HTTP_204_NO_CONTENT)
