from g4f.client import Client

client = Client()
def rdeFile(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "fl null"
    except Exception as e:
        return f"err: {e}"

completions = client.chat.completions.create(model="gpt-4o", messages=[{"content": rdeFile("request.txt")}])
print(completions.choices[0].message.content)