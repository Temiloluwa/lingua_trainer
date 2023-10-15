class BasePrompter:
    def __init__(self, **variables):
        self.variables = variables

    def generate_dictionary(self, role, content):
        return {"role": role, "content": content}

    def receive_content(self, role, content):
        return self.generate_dictionary(role, content)

    def __call__(self, content):
        for variable, value in self.variables.items():
            content = content.replace(f"{{{variable}}}", str(value))
        return self.receive_content(self.role, content)

class SystemPrompter(BasePrompter):
    def __init__(self, **variables):
        super().__init__(**variables)
        self.role = "system"

class UserPrompter(BasePrompter):
    def __init__(self, **variables):
        super().__init__(**variables)
        self.role = "user"

class AssistantPrompter(BasePrompter):
    def __init__(self, **variables):
        super().__init__(**variables)
        self.role = "assistant"
