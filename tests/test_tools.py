from backend.tools.tool_manager import ToolManager

tool = ToolManager()

while True:

    user = input("Perintah : ")

    if user == "exit":
        break

    result = tool.execute(user)

    print(result)