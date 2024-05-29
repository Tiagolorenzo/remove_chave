# remove chave

pessoa = {
    'Nome':'Fulano',
'Idade':20,
'Profissão':'programador',
'Empresa':'SENAI',
'Genero':'Masculino',
'Cidade':'RJ'
}

# remove chave
del pessoa[input('Informe o nome da chave a ser deletada: ')]

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')

    
                   
