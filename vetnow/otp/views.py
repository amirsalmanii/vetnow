from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView


class TokenList(ListAPIView):
    """
    send token list for next js front end
    """
    queryset = Token.objects.all()
    serializer_class = serializers.TokenListSerializer