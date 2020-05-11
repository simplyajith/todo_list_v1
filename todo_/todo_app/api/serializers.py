from rest_framework import serializers
from todo_app.models import Todo, TodoStatus

class TodoStatusSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = TodoStatus
        fields = "__all__"


class TodoSerializer(serializers.ModelSerializer):
    status_text = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = "__all__"
    
    def get_status_text(self,obj):

        if obj.id:
            state_data = Todo.objects.filter(id =obj.id)
            state_serializer = TodoStatusSerializer(state_data,many=True)
            return state_serializer.data[0]["status"]

    







# class ProfileSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(read_only=True)
#     avatar = serializers.ImageField(read_only=True)

#     # profile_status = ProfileStatusSerializer()

#     class Meta:
#         model = Profile
#         fields = "__all__"

# class ProfileAvatarSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Profile
#         fields = ("avatar",)


# class ProfileStatusSerializer(serializers.ModelSerializer):
#     user_profile = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = ProfileStatus
#         fields = "__all__"

# class StateSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = State
#         fields = "__all__"

# class AddressSerializer(serializers.ModelSerializer):
#     state_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Address
#         fields = '__all__'
#         # exclude =("state",)

#     def get_state_name(self,obj):
#         print(obj.state_id)
#         if obj.state_id:
#             state_data = State.objects.filter(id =obj.state_id)
#             state_serializer = StateSerializer(state_data,many=True)
#             # print(state_serializer.data)
#             return state_serializer.data[0]["name"]
    

        # state_serializer = StateSerializer(state_data[0])
        # print(state_serializer.data)

        # state_details = State.objects.filter(state_id=obj.state_id)
        # print(state_details)
        # print(obj.state.id)
        # state_details = State.objects.filter(state_id=obj.state.id)
        # serialized_activities = StateSerializer(state_details,
        #                                                 context={'request': self.context.get('request')})
        # print(serialized_activities.data)
        # return serialized_activities.data
