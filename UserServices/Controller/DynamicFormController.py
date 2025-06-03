from rest_framework.views import APIView    # type: ignore
from rest_framework.response import Response    # type: ignore
from rest_framework import status   # type: ignore
from EcommerceInventory.Helpers import getDynamicFormFields, getDynamicFormModels   
from django.apps import apps    # type: ignore
from rest_framework.permissions import IsAuthenticated        # type: ignore
from rest_framework_simplejwt.authentication import JWTAuthentication      # type: ignore


class DynamicFormController(APIView):
    authentication_classes = [JWTAuthentication]  # No authentication required for this endpoint
    permission_classes = [IsAuthenticated]  # No permission required for this endpoint
    def get(self, request, modelName):
        if modelName not in getDynamicFormModels():
            return Response({'error': 'Model not found'}, status=404)

        model = getDynamicFormModels()[modelName]
        model_class = apps.get_model(model)

        if model_class is None:
            return Response({'error': 'Model class not found'}, status=404)
        
        model_instance = model_class()
        fields = getDynamicFormFields(model_instance, request.user.domain_user_id)
        return Response({'data': fields, 'message': 'Dynamic form fields retrieved successfully'}, status=status.HTTP_200_OK)