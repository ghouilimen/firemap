
from rest_framework import serializers
from authentication.models import Users

   
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Users
        fields=['username','first_name','last_name','email','password']
    
   
    

    