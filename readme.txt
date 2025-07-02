📄 README.txt – Projeto de Jogo com Pygame

Nome do Jogo: Corra, Atire e Fuja  
Desenvolvido por: Michele Taverna, RU: 4027867
Base do projeto: Código fornecido pelo professor como estrutura inicial.

---

🎮 Descrição

"Corra, Atire e Fuja" é um jogo 2D de ação desenvolvido em Python com a biblioteca Pygame. A ideia central do jogo gira em torno de 
personagens que precisam se mover pelo cenário, atirar em inimigos e fugir de ameaças constantes.

O projeto foi criado a partir da base fornecida pelo professor, mas todas as decisões de layout, tema, personagens e interações 
foram desenvolvidas por mim.

---

🧩 Funcionalidades adicionadas

✅ Alteração completa do **tema** e dos **planos de fundo**.  
✅ Inclusão de **novos personagens** com sprites personalizados.  
✅ Implementação de **movimento de caminhar** nos personagens.  
✅ Ação de **atirar** com animação e **som personalizado**.  
✅ Layout personalizado para o **menu inicial**, **tela de pontuação** e **legendas**.  
✅ Sons e imagens coletados da internet.  
✅ Pontuação salva e recuperada com **banco de dados SQLite**.

---

🧠 Tecnologias utilizadas

- Python 3
- Pygame
- SQLite

---

📁 Estrutura do Projeto

Corra Atire e Fuja
│
├── asset/ # Contém imagens, sons, fontes, etc.
├── code/ # Módulos do jogo
│ ├── Background.py
│ ├── Const.py
│ ├── DBProxy.py
│ ├── Enemy.py
│ ├── EnemyShot.py
│ ├── Entity.py
│ ├── EntityFactory.py
│ ├── EntityMediator.py
│ ├── Game.py
│ ├── Level.py
│ ├── Menu.py
│ ├── Player.py
│ ├── PlayerShot.py
│ ├── Score.py
│ └── init.py
├── DBScore # Banco de dados com pontuação
├── main.py # Arquivo principal para execução do jogo
└── README.txt

---

⚠️ Observações

- Embora o projeto tenha partido de uma base inicial fornecida, **todo o código foi reescrito ou modificado por mim** de acordo com 
o novo tema.
- Nenhum código foi copiado de projetos prontos da internet.
- Os assets de imagem e som foram obtidos de fontes abertas e estão organizados na pasta `asset/`.

---

📌 Créditos (opcional)

- Sons e sprites utilizados foram retirados de repositórios de uso livre:
  - https://freesound.org/
  - https://craftpix.net/  


