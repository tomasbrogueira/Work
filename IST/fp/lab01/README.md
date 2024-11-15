---
author:
- Pedro Reis dos Santos
---

# Git (controlo de versões)

![image](octocat.jpg)

Perder o trabalho já realizado é um problema que tem preocupado os
programadores.
Em especial quando a versão de ontem, ou de há uma semana, já tinha isto ou
aquilo a funcionar.
Já para não falar quando, por uma razão ou por outra, o trabalho é apagado
e a última cópia que existe é tão antiga que nem vale a pena usar,
mais vale começar do início.

O **gitlab.rnl.tecnico.ulisboa..pt** é um serviço
de *Web Hosting Colaborativo*
(*collaborative software development*) para
projetos que usam o **git** como ferramenta de controlo de versões
distribuídas (*distributed revision control*),
permitindo a gestão do código (*source code management* ou SCM)
através de um navegador *web* (*web browser*).
No **github.com** os repositórios públicos (onde qualquer pessoa
tem acesso) são gratuitos, enquanto o repositórios privados são pagos.
Outros serviços, como **bitbucket.org** ou o **gitlab.com**,
permitem repositórios públicos e privados gratuitos, mas introduzem outras
limitações.
Estes serviços oferecem funcionalidades de uma rede social adaptada ao
desenvolvimento de código (*social coding*), como *wiki*,
seguidores, grupos (equipas), *issues*, *clipboard*
(Gists ou snippets) com uma interface gráfica em rede.

## Configuração

A configuração do **git** baseia-se em pares nome-valor, onde o nome é
representado por uma ou mais componentes separadas por pontos (.).

O **git** utiliza três níveis de configuração: `git config  --system`
aplica-se a todos os utilizadores do computador e localiza-se em
`/etc/gitconfig` (em UNIX); `git config  --global`
aplica-se ao utilizador individual e localiza-se em `~/.gitconfig`
ou `~/.config/git/config` (onde '`~`' representa a diretoria
principal do utilizador ou \$HOME); `git config --local`, ou apenas
`git config` aplica-se ao repositório específico e localiza-se em
`.git/config` a partir da diretoria base do repositório.
Estes três níveis são processados sequencialmente pela ordem acima,
sendo utilizado o último valor associado a cada nome.

Antes de se iniciar a utilização do **git** é necessário definir, para
cada utilizador, o nome com que cada salvaguarda ficará registado e
respetivo endereço de correio eletrónico:
```
    git config --global user.name "Rui Silva"
    git config --global user.email ist99999@tecnico.ulisboa.pt
```
Notar que são estes valores que serão considerados quando o repositório
é envidado para o servidor *web* (por exemplo, **github.com**).

É ainda aconselhado definir o editor de texto usado para a mensagem nas
salvaguardadas, pois caso a opção **-m** seja omitida, o editor é
automaticamente invocado:
```
    git config --global core.editor /usr/bin/nano
```
Como o repositório disponibilizado para o projeto é privado, o seu
acesso requer a identificação do membro da equipa associada ao projeto.
Esta identificação pode ser realizada por pares
`gitname:password` ou `gitname:token`. Este par pode ser guardado num
ficheiro local ao computador com:
```
    git config --global credential.helper store
```
neste caso, a informação fica legível no ficheiro `~/.git-credentials`.
Alternativas à introdução da password, sem a deixarem visível, incluem a
utilização da *cache*, por exemplo
```
    git config --global credential.helper "cache --timeout 900"
```
evita a re-introdução da password nos `900` segundos após a sua primeira
introdução. A utilização de um *key-manager* (por exemplo, osxkeychain
em **MacOS-X**, wincred em **windows**, gnome-keyring ou KWallet em
**linux**) delega o armazenamento da password no *key-manager*, devendo
ser configurado com
```
    git config --global credential.helper nome-do-key-manager
```

Para repor o comportamento anterior à definição do *credential.helper*
usar
```
    git config --unset credential.helper
```

## Clonagem de um repositório

Para obter uma cópia no disco local, ou *clone*, de um repositório
existente podem ser utilizados dois protocolos: *https* ou *ssh*.
Ambas as soluções requerem configuração específica.

Para interagir com o servidor por *https* é necessário obter um **token**
de acesso. Este **token** vai substituir a password nos acessos ao repositório
através da ferramenta **git**. Notar que o acesso através do *browser*
continua a utilizar a *password*.

Para criar um **token** deve aceder à sua área no servidor **git** com o *browser* e
em *settings* ou *preferências* escolher *tokens de acesso* (*Access Tokens*).
O **token** é criado com um nome, duração (eventualmente indefinida) e um conjunto
de privilégios: pelo menos leitura e escrita no repositório para os objetivos desta
disciplina. Após a criação é-lhe apresentada uma cadeia de carateres de visualização
única, ou seja, deve copiar e guardar algures, pois não pode ser re-visualizada,
apenas apagada. Esta cadeia de carateres, ou **token**, deverá ser indicada sempre
que a ferramenta **git** lhe pedir uma *password*.

Para aceder aos servidores por **ssh** é necessário enviar previamente
uma chave pública SSH para o servidor. Se já criou anteriormente uma chave SSH,
da qual conhece a palavra passe, basta adicionar o conteúdo do ficheiro
que contém a parte pública, por exemplo `~/.ssh/id_rsa.pub`, nas seções
das configurações da sua conta em *SSH Keys*. Para criar uma chave SSH deve
executar o comando `ssh-keygen`, indicando uma palavra passe que deve
memorizar, sendo criados dois ficheiros contendo a parte privada e a
parte pública da chave SSH, em geral `~/.ssh/id_rsa` e `~/.ssh/id_rsa.pub`
respetivamente. Só a parte pública deve ser revelada a terceiros.

Pode criar chaves distintas em computadores diferentes
(com a mesma palavra passe
ou com palavras passe distintas) ou copiar a chave privada
para o respetivo diretório (`~/.ssh/`) dos **seus** computadores.
Sempre que criar uma nova chave, com a qual pretenda aceder ao servidor
de *git*, deve colocar a parte pública na sua conta do servidor **git**.

A clonagem do repositório da disciplina pode agora ser efetuada por *https*:
```
    git clone https://gitlab.rnl.tecnico.ulisboa.pt/fp22left/fp22info
```
onde o username é o mesmo do fénix (*ist1xxxxxx*) e a *password* é o **token**
criado acima.

Para clonar por *ssh* pode usar:
```
    git clone git@gitlab.rnl.tecnico.ulisboa.pt:fp22left/fp22info
```
neste caso deve indicar a palavra passe que utilizou quando criou a chave.

## Criação de um repositório

A criação de um repositório local pode ser realizada através do
comando `git init` num diretório vazio. Este repositório pode ser
posteriormente associado a um repositório remoto.

A criação de um repositório remoto realiza-se através de *browser*,
acedendo à conta do respetivo servidor, por exemplo:

- gitlab.rnl.tecnico.ulisboa.pt
- github.com
- bitbucket.org
- gitlab.com
- ...

O repositório `gitlab.rnl.tecnico.ulisboa.pt` pode ser acedido pelos
alunos e docentes com as credenciais do fénix
enquanto nos restantes é necessário criar uma
conta (endereço de email, username e password).

Depois de criar o repositório remoto pode criar uma cópia local com
o comando `git clone` seguido do endereço do repositório, por exemplo:
```
    git clone https://gitlab.rnl.tecnico.ulisboa.pt/ist1xxxxxx/exemplo
```
onde `ist1xxxxxx` é o *istID* do utilizador e `exemplo` o nome do
repositório criado.
Após a execução do comando `git clone` é criado um diretório com
o nome do repositório, que pode ser depois alterado para outro
nome (não altera o nome do repositório remoto).

Para introduzir um ficheiro no repositório remoto deve primeiro criar
o ficheiro no diretório local do repositório e depois submetê-lo
(`git push`) ao repositório remoto, por exemplo:
```
    cd exemplo/
    echo "print('hello world')" > hello.py
    git add hello.py
    git commit -am "hello em python"
    git push
```
Pode verificar as alterações introduzidas refrescando a página do *browser*
com o endereço do repositório.
Os mesmos comandos `git` devem ser executados sempre que um ficheiro é
posteriormente alterado.
Para obter no repositório local as alterações introduzidas no repositório remoto,
por exemplo por outro utilizador ou a partir de outra conta do mesmo utilizador,
deve executar o comando `git pull` dentro do diretório local do repositório.

Para criar uma cópia do repositório da disciplina que contenha as alterações que
entretanto vá realizando deve clonar (`git clone`) o repositório da disciplina
(*info*) e associá-lo a um repositório remoto privado (*previamente criado num
servidor*, por exemplo `gitlab.rnl.tecnico.ulisboa.pt`), aqui designado por *copia*,
executando no repositório local (*clone* do repositório *info*) o comando:
```
git remote set-url --push origin git@gitlab.rnl.tecnico.ulisboa.pt:ist1xxxxxx/copia.git
```
A partir deste momento as alterações ao repositório da disciplina podem ser
obtidos com `git pull` e as alterações enviadas para o repositório privado com
`git push`.

***Nota***: não deve criar ou clonar um repositório git dentro de outros repositórios git,
podendo colocar os vários repositórios num mesmo diretório, por exemplo.

## Criação de três versões

Este exemplo cria um projeto desde a origem e produz três versões de um
só ficheiro. Os comandos **status**, **log** e **show** são apresentados
para se compreender a evolução do projeto e não são necessários para a
criação das três versões do ficheiro. Após o segundo **commit** o
projeto terá um aspeto semelhante ao das três árvores, apresentado
acima. Para referência futura vamos considerar que as chaves das três
versões são *f263d08*, *3c78a9e* e *c5a5028*, respetivamente, embora cada
execução do exemplo produza chaves distintas.
```
     echo "V0 initial" >> file.txt 
     git status
     git add file.txt 
     git status
     git commit -m initial
     git status
     git log
     echo "V1 first change" >> file.txt 
     git status
     git add file.txt 
     git commit -m "first change"
     git log
     echo "V2 2nd change to the file" >> file.txt 
     git add file.txt 
     git commit -m 2nd_change
```

### Etiquetar versões

A introdução de etiquetas permite referir uma salvaguarda com um nome
simples em vez de uma chave SHA-1 ou uma data (um *post-it*). Em **git**
existem etiquetas leves (*lighweight*) e anotadas (**-a**), elas
próprias identificadas com uma chave SHA-1 e representadas como um
ficheiro em `.git/refs/tags`. Nas etiquetas leves a chave aponta
diretamente para o **commit** e são mais apropriadas para uso individual
do programador

Uma etiqueta anotada é um objeto do tipo **tag** e inclui uma mensagem
(**-m**), que pode ser impressa com o comando **show**, e contém um
criador e uma data que pode ser distinta da do **commit** que refere.
São as etiquetas anotadas que devem ser partilhadas com os restantes
membros da equipa, podendo ser assinadas. Ao assinar uma etiqueta
anotada é garantida a identidade do signatário com uma chave PGP (opções
**-s** ou **-u key-id**), o que permite detetar distribuições
fraudulentas quando o repositório é copiado.
```
     git log
     git tag -a v1.2 -m prs-1.4 # tag this version
     git show v1.2
     git tag
     git log
     git status
     git log --pretty=oneline
     git tag -a v1.0 f263d08 -m original # tag a previous version
```

Para mover uma etiqueta para uma salvaguarda mais recente basta
acrescentar a opção **-f** (*force*) às anteriores. Alternativamente, a
etiqueta pode ser removida com a opção **-d** e depois inserida com o
comando acima. No entanto, se a etiqueta já tiver sido empurrada
(**push**) para um servidor remoto, deve ser primeiro removida
remotamente (`git push origin :refs/tags/\<tagname\>`) e, uma vez movida
localmente, novamente empurrada a etiqueta para o servidor
(`git push origin master --tags`).

## Recuperar versões anteriores

Uma das vantagens de um sistema de controlo de versões consiste na
possibilidade de recuperar versões anteriores dos ficheiros
salvaguardados. O comando **checkout** quando inclui uma versão e uma
lista de ficheiros, por nome, copia essas versões para a área de
trabalho, perdendo-se quaisquer alterações locais não salvaguardadas
(**commit**) entretanto efetuadas. Por exemplo, um ficheiro apagado por
engano (`rm file.txt`) pode ser recuperado com
(`git checkout HEAD file.txt`).
Caso se trate da versão corrente (`HEAD`) esta pode ser omitida
(`git checkout file.txt`).

O comando **reset** permite copiar um ou mais ficheiros de uma versão
para a área de espera e, com a opção **--hard**, da versão para a área
de espera e para a área de trabalho. Neste último caso (**--hard**)
perdem-se todas as alterações locais, caso não tenham sido
salvaguardadas previamente. Por exemplo, `git reset HEAD~2 file.txt`
coloca na área de espera o ficheiro de há duas versões atrás.

O comando **reset** pode ainda ser invocado sem a indicação de qualquer
ficheiro, por exemplo `git reset HEAD~2`, mas neste caso recua-se duas
versões (HEAD e **master**). Um posterior **commit** empurra os dois
commits recuados para um ramo auxiliar que pode ser posteriormente
eliminado. A utilização de **revert** em vez de **reset**, caso em que é
criado um novo **commit** depois do atual com o mesmo conteúdo do
indicado `HEAD~2`, mantém os **commit**s recuados na sua posição
inicial.

## Desenvolvimento paralelo

De nada serve guardar as diversas versões de um projeto se não for
possível inspecioná-las. O comando **checkout** permite saltar entre as
diversas versões do projeto. O argumento é uma chave de salvaguarda
(SHA-1) ou uma etiqueta. Para recuperar por data é necessário obter a
chave correspondente, por exemplo
`git rev-list -n 1 --before=\"2016-02-16 10:01\" master`.
As etiquetas móveis `HEAD` e
**master** podem ser utilizadas, bem como referências relativas `HEAD~2`
(duas salvaguardas acima da `HEAD`).

Notar que `HEAD` e **master** não são a mesma coisa, embora `HEAD` possa
apontar para **master** em certas alturas. A `HEAD` é a minha posição
atual, enquanto o **master** representa a linha principal de
desenvolvimento, aquela onde os restantes utilizadores estão ligados. Se
devido a alterações de outros utlizadores, ou por distração, o
**master** ficar perdido no meio do grafo, pode ser puxado com `git
checkout master` seguido de *merge* para a *versão* pretendida `git merge
versão`. Se o **master** estiver na mesma linha de desenvolvimento do
local de destino, não são necessárias alterações, logo não é necessário
nenhum **commit**, e designa-se por *fast-forward merge*.

O comando **branch** permite criar um ramo para desenvolvimento
paralelo. Este ramo permite fazer experiências que podem, ou não, vir a
ser úteis, independentemente do número de salvaguardas efetuadas no
ramo. O comando **branch** e o respetivo **checkout** podem ser
condensados, e a versão de partida omitida for `HEAD`, em
`git checkout -b first\_fork`.
```
     cat file.txt 
     git checkout 3c78a9e
     cat file.txt 
     git branch fork_first 3c78a9e
     git checkout first_fork
     echo "V1.1 from forked first" >> file.txt 
     git add file.txt
     git commit -m first_fork # SHA-1 = 4ffd0ea
     git log --graph --oneline --decorate --all
```

Com a introdução do desenvolvimento paralelo, a opção `--graph` do comando
**log** permite ter uma representação rudimentar do grafo de versões no
repositório. Para simplificar a invocação deste comando para **git
graph**, incluir-se na secção do ficheiro de configuração `~/.gitconfig`
a definição\
```
graph = !"git log --graph --oneline --decorate --all"
```

Caso o trabalho desenvolvido no ramo seja positivo deve ser integrado na
linha principal de desenvolvimento (**master**). Os ramos que não
desenvolveram trabalho útil ficam com as pontas soltas, embora possam
ser recuperados em qualquer momento. Para remover definitivamente o
ramo, usa-se a opção **-d** (`git branch -d name`). O comando **merge**
permite integrar as alterações do ramo corrente (`HEAD`) no ramo
pretendido, em geral **master** (`git merge master`). Se não surgirem
conflitos, alterações diferentes para uma mesma linha de código, o
comando conclui com sucesso. Um conflito surje quando a mesma linha de
um mesmo ficheiro tem dois conteúdos distintos. Neste caso, a terceira
linha do ficheiro contém um texto diferente entre a terceira versão
(c5a5028 ou **master**) e a versão do first\_fork (`4ffd0ea` ou `HEAD`). Ao
executar o comando `git merge master` é detetado o conflito e invocado
o editor anteriormente configurado. Caso este ficheiro seja escrito tal
qual é fornecido (sem alterações), os conflitos são assinalados nos
respetivos ficheiros com as marcas `<<<<<<<`, `=======` e `>>>>>>>`.
Compete ao programador decidir qual o aspeto final do ficheiro, ou seja
qual das duas modificações (ou composição destas) sobrevive. Cuidado,
pois se os ficheiros que incluem conflitos não forem todos corrigidos, a
versão final irá incluir as marcas acima como definitivas, o que não é
uma sequência válida em qualquer linguagem. Um **commit** permite
concluir o **merge**, tornando definitivas as alterações. A opção **-a**
efetua implicitamente o **git add** dos ficheiros modificados e o **git
rm** dos ficheiros removidos antes do **commit**.
```
     git merge master
     git status # show conflicts
     edit file.txt 
     git commit -am "conclude merge" # SHA-1 = 9b3ce96
     git log --graph --oneline --decorate --all
     git checkout master
     git merge fork_first # move master to fork_first
```

O desenvolvimento paralelo com **branch** e **merge** é simples e não
destrutivo, no sentido em que todas as alterações efetuadas são mantidas
imutáveis. Este facto é importante quando for necessário descobrir a
origem de um problema passado. Contudo, numa equipa grande, com muitos
ramos simultaneamente ativos, o grafo pode tornar-se complexo e
incompreensível.

## Repositórios remotos

A ferramenta **git** inclui comandos para interagir com o servidor de
**git**, de **github.com**, **bitbucket.org** ou outro. A salvaguarda
das alterações (*commits*) para o servidor (*push*) permite que estas
fiquem visíveis para os outros utilizadores. Notar que todas as
alterações locais são enviadas e não apenas a última. Inversamente,
podem-se obter (*fetch*) todas as alterações registadas no servidor por
forma a posteriormente efetuar a fusão (*merge*) da versão de trabalho
com uma das versões registadas, em geral a última.

A abordagem de desenvolvimento colaborativo depende da publicação das
salvaguardas locais do projeto (**commit**) num repositório remoto, para
poder ser obtido ou atualizado por outros. Repositórios remotos, geridos
por servidores, são versões do projeto. Cada projeto pode ter vários
repositórios remotos. Os repositórios são identificados e acedidos por
URL, podendo ser acedidos por **https** ou **ssh**, por exemplo:
```
https://github.com/user/repo.git

git@github.com:user/repo.git
```

O **git** associa ao URL remoto um nome simbólico, mais simples que um
endereço completo, frequentemente designado por **origin** (ver `git
remote`).

Para criar os repositórios remotos pode usar o *browser* com a sua conta em
```
https://gitlab.rnl.tecnico.ulisboa.pt/ist1xxxxx
```
onde `xxxxx`é o seu número mecanográfico do *IST*, utilizando a password
do *fénix* na identificação.

### Os primeiros passos

Primeiro deve criar uma conta no **github.com**, devendo indicar o
endereço de *email* que indicou no `git config`. É quanto basta para
aceder ao servidor via http (e https).

O projeto pode ser criado através da interface gráfica, podendo depois
associar os ficheiros do projeto a desenvolver de duas formas. Pode
optar por clonar o repositório e copiar para ele os ficheiros, que já
possui ou que vai criando:
```
       $ git clone https://github.com/user/proj.git
       $ cp myfiles proj
       $ cd proj
       $ git add . # mark all files to commit
       $ git commit -m "message" # commit to local repository
       $ git push # send to github
```

Alternativamente, pode associar um repositório local **git** com o
projeto **github** que acabou de criar:
```
       $ cd /path/to/my/repo
       $ git remote add origin https://github.com/user/proj.git
       $ git push -u origin master
```

Se o repositório já contiver etiquetas e referências, estas devem ser
enviadas separadamente:
```
       $ git push -u origin --all # pushes repo and refs (1st time)
       $ git push -u origin --tags # pushes any tags 
```

Caso se pretenda efetuar o acesso com **ssh** em vez de **https**, os
endereços devem ser substituídos por `git@github.com:user/repo.git`,
embora necessite da chave SSH em ambos os casos.

### Merge remoto

O desenvolvimento de software colaborativo (*collaborative software
development*) implica que as alterações efetuadas por uns utilizadores
vão influenciar o comportamento do código desenvolvidos por outros.
Assim, é de extrema importância executar testes ao software antes de
enviar alterações para o servidor (**github** ou outro).

Se as alterações efetuadas por dois, ou mais, utilizadores não afetarem
a mesma zona do ficheiro, em geral as mesmas linhas, a ferramenta
**git** consegue fundir as alterações. Isto não significa que ambas as
alterações funcionem corretamente em conjunto, mesmo que não apresentem
problemas cada uma por si só.

Notar que dois utilizadores pode referir-se a um só utilizador em duas
máquinas distintas, por exemplo um computador fixo e um portátil
(ou telemóvel).

Consideremos que dois utilizadores (**a** e **B**) obtêm cópias de um
mesmo repositório:
```
    a> git clone http://github.com/user/hello.git
    B> git clone http://github.com/user/hello.git
```

Para simplificar, este projeto tem um único ficheiro, tipo hello world,
que imprime a mensagem Olá pessoal.

O utilizador **a** resolve alterar a mensagem para Olé pessoal:
```
    a> cd hello/
    a> echo 'print("Olé pessoal!")' > hello.py
    a> git status
    a> git commit -am "pessoal"
    a> git push
```

e submente as alterações ao servidor sem problemas.

Enquanto isso, o utilizador **B** altera a mensagem para Olá touro:
```
    B> cd hello/
    B> echo 'print("Olá touro!")' > hello.py
    B> git commit -am "touro"
    B> git push
```

que ao submeter as alterações ao servidor recebe um erro, pois o
ficheiro já não está igual ao que ele foi buscar devido às alterações de
**a**. Consequentemente é necessário ir buscar as alterações no servidor
e unir (*merge*) com as alterações locais:
```
    B> git pull
```

Se houver alterações inconsistentes na mesma zona de código a união não
é realizada (`error: Failed to merge in the changes.`) e os ficheiros com
inconsistências são assinalados (Merge conflict in hello.java). Assim,
ele deverá editar o ficheiro, ou ficheiros, com conflitos e optar por
uma solução.
```
    <<<<<<< HEAD
                    print("Olé pessoal!");
    =======
                    print("Olá touro!");
    >>>>>>> touro
```

Notar que esta solução pode ser a que ele escreveu, a que o utilizador
**a** escreveu, ou uma solução alternativa que incorpore ambas as
alterações.
```
    B> git pull
    B> echo 'print("Olé touro")' > hello.py
    B> git commit -am "ole touro"
    B> git push
```

Caso as alterações sejam noutros ficheiros ou zonas de código, o comando
`git pull` já consegue fazer a união (*merge*) das duas versões sem
conflitos, pelo que basta enviar o código resultante para o servidor:
`git push`. Notar que antes de fazer qualquer `git push` deve testar o
código a enviar. Também depois de fazer um *merge*
ou *rebase*, mesmo que não ocorram conflitos, deve testar se o código
resultante da união ainda funciona.
