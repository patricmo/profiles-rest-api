from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serialize a name field to test our APIView"""

    name = serializers.CharField(max_length=10)

    # def __init__(self, arg):
    #     super(HelloSerializer, self).__init__()
    #     self.arg = arg
    #
