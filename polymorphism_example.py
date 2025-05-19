class Tools:
    def use_tool(self):
        print("Tools")

class Screwdriver:
    def use_tool(self):
        print("For tightening screw")

class Hammer:
    def use_tool(self):
        print("Hammer")

choice = int(input("Enter number (1 for Screwdriver, 2 for Hammer): "))
tools=None
if choice == 1:
    tool = Screwdriver()
    tool.use_tool()
elif choice == 2:
    tool = Hammer()
    tool.use_tool()
else:
    print("None")

if tool:
    tool.use_tool()
