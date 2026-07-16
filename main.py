from app.agent import chat

print("=" * 50)
print("Local AI Agent")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    user = input("\nYou : ")

    if user.lower() == "exit":
        break

    response = chat(user)

    print("\nAgent :", response)