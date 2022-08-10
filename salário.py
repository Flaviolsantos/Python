if __name__ == '__main__':
    while True:
        ordenado = input('Qual o ordenado? ')
        ss = input('Quanto desconta para segurança social?')
        irs = input('Quanto desconta de IRS? ')
        sub_ref = input('Quantos dias de subsidio de refeição? ')
        alim_dia = input('Quanto de subsidio de alimentação por dia?')
        desconta = input('Desconta para ADSE?')
        desconta_sim = 3.5
          
        print(f'{ordenado} ordenado' )
        print(f'{ss} Desconto para seguraça social' )
        print(f'{irs} irs')

        sub_alim = float(sub_ref) * float(alim_dia)
        percentagem_ss = float(ordenado) * float(ss)/100
        percentagem_irs = float(ordenado)  * float(irs)/100
        percentagem_adse = float(ordenado) * float(desconta_sim)/100

        print(f'{percentagem_ss} %ss')
        print(f'{percentagem_irs} %irs')

        liquido = float(ordenado) - float(percentagem_ss) - float(percentagem_irs) + float(sub_alim)
        
        if desconta == 'sim':
            adse = liquido - percentagem_adse
            print(f'O ordenado liquido é {adse}')
        else:
            print(f'O ordenado liquido é {liquido}')

        x = input('Quer Repetir?(sim/não)')
        if x == 'sim':
            continue
        else:
            break
