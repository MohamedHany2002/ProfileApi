from rest_framework import serializers
from django.contrib.auth.models import User
from .models import feedItem



class profile(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class profileSerializer(serializers.ModelSerializer):
    # password2=serializers.CharField(write_obly=True)
    class Meta:
        model=User
        fields=['username','email','password']
        extra_kwargs={'password':{'write_only':True}}

        def create(self,validated_data):
            user=User.objects.create(username=validated_data['username'],email=validated_data['email'],password=validated_data['password'])
            # user=User(username=validated_data['username'],email=validated_data['email'])
            # user.set_password(validated_data['password'])
            # user.save()
            return user


class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedItem
        fields=['id','user','text','created']
        extra_kwargs={'user':{'read_only':True}}


        # def create(self):
        #     item=self.save(user,self.validated_data['user'])
        #     return item
