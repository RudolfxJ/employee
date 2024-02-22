from rest_framework import serializers

from .models import Employee, Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True, source="employee_skills", read_only=True)

    class Meta:
        model = Employee
        exclude = ("employee_code",)

    def validate(self, attrs):
        request = self.context.get("request")
        if request.data:
            data = request.data
        else:
            raise serializers.ValidationError({"request": "request object not found"})
        skills = data.get("skill")
        if skills:
            for skill in skills:
                if not skill["name"]:
                    raise serializers.ValidationError(
                        {"skill": "Please provide skill name."}
                    )
                if not skill["years_experience"]:
                    raise serializers.ValidationError(
                        {"skill": "Please provide number of years of experience."}
                    )
                if not skill["seniority_rating"]:
                    raise serializers.ValidationError(
                        {"skill": "Please provide seniority level"}
                    )

        return super().validate(attrs)

    def create(self, validated_data):
        return self.create_employee(validated_data)

    def update(self, instance, validated_data):
        return self.create_employee(validated_data, instance)

    def create_employee(self, validated_data, instance=None):
        if instance:
            employee = super().update(instance, validated_data)
        else:
            employee = super().create(validated_data)

        request = self.context.get("request")
        if request.data:
            data = request.data
        else:
            raise serializers.ValidationError({"server error": "no request passed"})

        if data.get('skill'):
            skills = data.pop("skill")
            Skill.objects.filter(employee=employee).delete() if instance else ""
            for skill in skills:
                skill["employee"] = employee.id
            serializer = SkillSerializer(data=skills, many=True)
            if serializer.is_valid():
                serializer.save()
            else:
                raise serializers.ValidationError(serializer.errors)
        return employee
