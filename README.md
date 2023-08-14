# ti_shop_backend

Você pode criar e gerenciar um ambiente virtual no Python usando a ferramenta venv. Aqui estão os passos para criar um ambiente virtual utilizando venv:

Abra o terminal ou prompt de comando.

Navegue até o diretório onde deseja criar o ambiente virtual.

Execute o seguinte comando para criar um novo ambiente virtual chamado "myenv" (você pode substituir "myenv" pelo nome que preferir):

bash
Copy code
(python -m venv myenv)
Isso criará uma pasta chamada "myenv" no diretório atual, contendo os componentes do ambiente virtual.

Para ativar o ambiente virtual, execute o comando apropriado para o seu sistema operacional:
No Windows:
bash
Copy code
(myenv\Scripts\activate)
No macOS e Linux:
bash
Copy code
(source myenv/bin/activate)
Após ativar o ambiente virtual, seu terminal mostrará o nome do ambiente virtual no prompt, indicando que você está trabalhando dentro dele.

Agora você pode instalar pacotes e bibliotecas específicas para este ambiente virtual, incluindo o Django e outras dependências listadas no requirements.txt.
(pip install -r requirements.txt)

Quando terminar de trabalhar no ambiente virtual, você pode desativá-lo usando o seguinte comando:

bash
Copy code
deactivate
Lembrando que o nome do ambiente virtual (no exemplo acima, "myenv") é personalizável e você pode escolher o que preferir. Certifique-se de usar o ambiente virtual apropriado sempre que estiver trabalhando em um projeto específico.

Após seguir todos os passos, utilize o comando (python manage.py runserver) para rodar o servidor 
