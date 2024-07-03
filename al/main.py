from g4f.client import Client

client = Client()

print("Начинаем сеанс общения с моделью GPT-4. Введите 'exit' для завершения.")

while True:
    user_input = input("Вы: ")
    print("Ожидание ответа...")

    if user_input.lower() == 'exit':
        print("Завершение сеанса.")
        break

    response = client.chat.completions.create(model="gpt-4o", messages=[{"content": user_input}]).choices[0].message.content

    print("GPT-4: " + response)