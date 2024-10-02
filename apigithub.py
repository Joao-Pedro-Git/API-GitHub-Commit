import requests
import matplotlib.pyplot as plt

# Substitua pelo seu token
token = 'SUA_KEY or YOU KEY'
username = 'Joao-Pedro-Git'  # Seu nome de usuário do GitHub

# URL da API para obter os repositórios
repos_url = f'https://api.github.com/users/{username}/repos'
headers = {'Authorization': f'token {token}'}

print("Obtendo repositórios...")  # Mensagem de depuração
response = requests.get(repos_url, headers=headers)

if response.status_code == 200:
    repos = response.json()
    public_commits = 0
    private_commits = 0
    repo_names = []

    for repo in repos:
        # Contar commits em todos os repositórios
        commits_url = f"https://api.github.com/repos/{username}/{repo['name']}/commits"
        print(f"Contando commits no repositório: {repo['name']}")  # Mensagem de depuração
        commits_response = requests.get(commits_url, headers=headers)

        if commits_response.status_code == 200:
            commits_count = len(commits_response.json())
            repo_names.append(repo['name'])
            
            if repo['private']:
                private_commits += commits_count
            else:
                public_commits += commits_count
        else:
            print(f"Erro ao obter commits para {repo['name']}: {commits_response.status_code}")

    # Exibindo total de commits
    print(f'Total de commits públicos: {public_commits}')
    print(f'Total de commits privados: {private_commits}')

    # Criando gráfico
    labels = ['Públicos', 'Privados']
    sizes = [public_commits, private_commits]
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FF5733'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    plt.title('Distribuição de Commits (Públicos vs Privados)')
    plt.show()
else:
    print(f"Erro ao obter repositórios: {response.status_code}")
