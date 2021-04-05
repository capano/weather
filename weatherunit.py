# Programa para requisição e análise dos dados da API weather


import requests


def main():
    print('######################')
    print('### Consulta Tempo ###')
    print('######################')
    print()

    city_input = input('Digite a chave/cidade para a consulta: ')


    # request = requests.get('https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=2d92472a453a1eebe622a647e2e4f882'.format(city_input))
    request = requests.get('http://192.168.100.15:9000/weather/' + city_input)
    # request = requests.get('http://191.19.147.14:9003/weather/' + city_input)

    # previsao&cidade=campinas
    # pesquisa&cidade=campinas

    return_data = request.json()
    print(return_data)
    print('---------------------------------')


    ##########################
    # fim teste
    exit()
    ##########################

if __name__ == '__main__':
    main()
