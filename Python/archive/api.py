import requests

# Defina o nome de usuário do GitHub para o qual deseja buscar informações
username = "HughCoding"

# Faça uma solicitação GET para o endpoint da API
response = requests.get(f"https://api.github.com/users/{username}")

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Converta a resposta para JSON
    user_data = response.json()
    print(f"Nome do usuário: {user_data['login']}")
    print(f"Número de repositórios públicos: {user_data['public_repos']}")
else:
    print("Erro ao buscar informações do usuário.")
