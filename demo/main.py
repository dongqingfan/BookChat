from zhipuaiv2 import ChatZhipuAI

llm = ChatZhipuAI(
    temperature=0.1, api_key="xx", model="glm-4"
)

print(llm.invoke("hello, what today is today?"))