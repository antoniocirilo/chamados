<h3 align="center">

TI - Chamados é um sistema em **Django** para o setor de TI verificar os seus chamados. 

</h3>

## **:rocket: OBJETIVO**

O projeto tem como propósito melhorar a organização e agilizar os chamados de TI.

## **:computer: TECNOLOGIAS**


#### **Website** ([Django][Django] + [Python][Python])

  - **[Django][Django]**
  - **[HTML][HTML]**
  - **[CSS][CSS]**

  \* Veja o arquivo <kbd>[package.json](./sources/website/package.json)</kbd>



## **:wine_glass: COMO UTILIZAR**

### Configurações Iniciais

Primeiro, você precisa ter o <kbd>[Python](https://www.python.org/downloads/)</kbd> instalado na sua máquina. 

Se você estiver utilizando o **Linux**, você pode optar por instalar o **Python** através do site oficial da linguagem <kbd>[Python](https://www.python.org/downloads/)</kbd>.

Após ter o **Python** instalado, instale um ambiente virtual(virtualenv) no site <kbd>[Virtualenv](https://pypi.org/project/virtualenv/#files)</kbd>.
Logo após, crie o ambiente virtual e de um nome a ele (Windows/Linux):
```sh
$ virtualenv ambiente
```
Depois, ative, utilizando os comandos: <br />
Ativando a venv no linux:
```sh
$ source ambiente/bin/activate
```
Ativando a venv no Windows:
```sh
$ ambiente\Scripts\activate
```

Logo pois, entre no diretório do projeto e instale as dependências contidas nos arquivos `requirements.txt` que se encontram na raíz do repositório
(para o gerenciamento de commits).
Para instalar as dependências, basta abrir o terminal no diretório e digitar o comando:

```sh
$ pip install -r requirements.txt

```

Veja os arquivos **`requirements.txt`** do <kbd>[commitlint](./requirements.txt)</kbd>

Depois, entre no diretório da aplicação chamada **TI** e digita o seguinte comando:
```sh
$ python manage.py runserver
```
Logo depois, entre no seu navegador coloque na url:
```sh 
http://localhost:8000/
```

## **:books: REFERÊNCIAS**

- [Django](https://www.djangoproject.com/)

- [Python](https://www.python.org/)
- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/)
- [Java Script](https://www.w3schools.com/js/)

## **:page_with_curl: LICENÇA**

Esse repositório está licenciado pela **MIT LICENSE**. Para mais informações detalhadas, leia o arquivo [LICENSE](./LICENSE) contido nesse repositório. 

<h2 align="center">:checkered_flag: Feito por  <a href="https://www.linkedin.com/in/antonio-cirilo-997bab17b/">Antonio Cirilo</a> & <a href="https://www.linkedin.com/in/jeffesson-gomes-2b36911aa/">Jeffesson Gomes</a></h2>


<!-- Techs -->

[Django]: https://www.djangoproject.com/

[HTML]: https://www.w3schools.com/html/

[CSS]: https://www.w3schools.com/w3css/defaulT.asp
[Python]: https://www.python.org/
