from rest_framework import serializers

def genericSerializer(model_class):

    """
        Crea un serializador genérico para un modelo Django especificado.

        Esta función genera un serializador de Django REST Framework para el modelo especificado. 
        El serializador incluirá automáticamente todos los campos del modelo.

        Parámetros:
        - model_class (Django Model): La clase del modelo Django para la cual se creará el serializador.

        Retorna:
        - GenericSerializer (serializers.ModelSerializer): Una clase de serializador genérico que incluye todos los campos del modelo especificado.
    """

    class GenericSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_class
            fields = '__all__'

    return GenericSerializer