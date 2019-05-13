from rest_framework import serializers
from computer.models import Computer
from computer_status.models import ComputerStatus
from computer_events.models import ComputerEvents

class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Computer
        fields = ('id', 'name', )


class ComputerStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerStatus
        fields = ('id', 'nome', 'codigo', )


class ComputerEventsSerializer(serializers.Serializer):
    computador = serializers.IntegerField(allow_null=False)
    codigo = serializers.IntegerField(allow_null=False)

    def save(self, **kwargs):
        event = self.data
        try:
            status = ComputerStatus.objects.get(codigo=event.get('codigo'))
            computer_event = ComputerEvents.objects.create(computer_id=event.get('computador'), status=status)
            return {"event": computer_event.pk}
        except Exception as e:
            raise Exception(e)


