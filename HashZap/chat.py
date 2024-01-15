import flet as ft 

def main(page):
    # Itens da página
    Title = ft.Text("ChatZaP", size=24)
    user_name_text_camp = ft.TextField(label="Escreva seu nome aqui")


    campo_da_mensagem = ft.TextField(label="Digitar...")
    botao_enviar_msg = ft.ElevatedButton("Enviar")
    linha_de_mensagem = ft.Row([campo_da_mensagem, botao_enviar_msg])

    chat = ft.Column()

    # DEF para ENTRAR no chat #
        # Ao entrar no chat eu preciso que:
        # O pop-up se feche
        # O botão "Start Chat" suma
        # Ligue a estrutura do chat
            # Ligue o campo de enviar mensagem
            # Ligue o botão de enviar mensagem
    def join_in_chat(evento):
        page.dialog = pop_up
        pop_up.open = False
        page.remove(Start_Button)
        page.add(chat)
        page.add(linha_de_mensagem)
        page.update()
    
    # def para fechar o Pop-Up
    def close_popup(evento):
        page.dialog = pop_up
        pop_up.open = False
        page.update()

    pop_up = ft.AlertDialog(
    open=False,
    modal=True,
    title=ft.Text("Seja bem vindo ao ChatZaP"),
    content=user_name_text_camp,
    actions=[ft.ElevatedButton("Entrar", on_click=join_in_chat), ft.ElevatedButton("Sair", on_click=close_popup)]
    )
        
    def start_chat(evento):
        page.dialog = pop_up
        pop_up.open = True
        page.update()
        
    Start_Button = ft.ElevatedButton(
        "Start Chat",
        on_click=start_chat
        )


    page.add(Title)
    page.add(Start_Button)

ft.app(main)