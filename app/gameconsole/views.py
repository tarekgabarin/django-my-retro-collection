from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from gameconsole.models import GameConsole
from gameconsole.serializers import GameConsoleSerializer
from rest_framework import status
from consolemaker.models import ConsoleMaker

class GameConsoleViewSet(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def list(self, request):
        queryset = GameConsole.objects.all()
        serializer = GameConsoleSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        data = request.data
        id_of_console_maker = data['console_maker_id']
        obj_of_console_maker = ConsoleMaker.objects.get(id=id_of_console_maker)
        created_console = GameConsole.objects.create(
            name=data['name'],
            name_code=['name_code'],
            maker_of_console=obj_of_console_maker
        )
        created_console.save()
        serializer = GameConsoleSerializer(created_console)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        data = request.data
        id_of_console_to_update = data['console_id'] 
        id_of_console_maker = data['console_maker_id']
        obj_of_console_maker = ConsoleMaker.objects.get(id=id_of_console_maker)
        console_to_update = GameConsole.objects.get(id=id_of_console_to_update)
        console_to_update.name = data['name']
        console_to_update.name_code = data['name_code']
        console_to_update.maker_of_console = obj_of_console_maker
        console_to_update.save()
        serializer = GameConsoleSerializer(console_to_update)
        return Response(serializer.data, status=status.HTTP_200_OK)