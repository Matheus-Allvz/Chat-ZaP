import flet as ft 

def main(page):
    # Itens da página
    Title = ft.Text("ChatZaP", size=24)

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
        chat.controls.append(ft.Text(f"{user_name_text_camp.value} entrou no ChatZaP."))
        page.add(linha_de_mensagem)
        page.update()
    user_name_text_camp = ft.TextField(label="Escreva seu nome aqui", on_submit=join_in_chat)

    # def para fechar o Pop-Up
    def close_popup(evento):
        page.dialog = pop_up
        pop_up.open = False
        user_name_text_camp.value = ""
        page.update()

    pop_up = ft.AlertDialog(
    open=False,
    modal=True,
    title=ft.Text("Seja bem vindo ao ChatZaP"),
    content=user_name_text_camp,
    actions=[ft.ElevatedButton("Entrar", on_click=join_in_chat), ft.ElevatedButton("Sair", on_click=close_popup)]
    )

    def enviar_msg(evento):
        msg_camp_text = f"{user_name_text_camp.value}: {campo_da_mensagem.value}"
        chat.controls.append(ft.Text(msg_camp_text))
        campo_da_mensagem.value = ""
        page.update()

    chat = ft.Column()
    campo_da_mensagem = ft.TextField(label="Digitar...", on_submit=enviar_msg)
    botao_enviar_msg = ft.ElevatedButton("Enviar", on_click=enviar_msg)
    linha_de_mensagem = ft.Row([campo_da_mensagem, botao_enviar_msg])


        
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