import flet as ft

counter_value = 0

def main(page):
    page.title = 'Counter'
    github_repo = 'https://github.com/taaaf11/Counter-App'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'dark'
    
    def increment_counter(e):
        global counter_value
        counter_value += 1
        counter_label.value = str(counter_value)
        page.update()
    
    
    def reset_counter(e):
        global counter_value
        counter_value = 0
        counter_label.value = str(counter_value)
        page.update()
    
    
    def change_theme_mode(e):
        # acquire current theme modes, change theme, and colours of ui elements
        if page.theme_mode == 'dark':
            page.theme_mode = 'light'
            page.floating_action_button.icon = ft.icons.DARK_MODE_ROUNDED
            page.floating_action_button.bgcolor = '#fdfcff'
            
        elif page.theme_mode == 'light':
            page.theme_mode = 'dark'
            page.floating_action_button.icon = ft.icons.LIGHT_MODE_OUTLINED
            page.floating_action_button.bgcolor = '#1a1c1e'
        
        # and update the page at the end
        page.update()
    
    
    def change_current_page(e):
        selected_page = e.control.selected_index
        if selected_page == 0:
            view.visible = True
            about.visible = False
        elif selected_page == 1:
            view.visible = False
            about.visible = True
        
        page.update()
        
    
    page.appbar = ft.AppBar(title=ft.Text('Counter'))
    
    page.drawer = ft.NavigationDrawer(controls=[
        ft.NavigationDrawerDestination(
            icon=ft.icons.HOME_OUTLINED,
            label='Home',
            selected_icon=ft.icons.HOME_ROUNDED),
        
        ft.Divider(thickness=1),
        
        ft.NavigationDrawerDestination(
            icon=ft.icons.LIGHTBULB_OUTLINED,
            label='About',
            selected_icon=ft.icons.LIGHTBULB_ROUNDED)
    ], selected_index=0, on_change=change_current_page)
    
    
    button_reset = ft.IconButton(ft.icons.ROTATE_90_DEGREES_CCW_ROUNDED, on_click=reset_counter)
    counter_label  = ft.TextField(value='0', read_only=True)
    button_inc   = ft.IconButton(ft.icons.ADD_ROUNDED, on_click=increment_counter)
    
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.LIGHT_MODE_OUTLINED, bgcolor='#1a1c1e', on_click=change_theme_mode)
    
    view = ft.Row([
        button_reset,
        counter_label,
        button_inc
    ], alignment='center', vertical_alignment='center', expand=True, visible=True)
    
    about = ft.Column([
        ft.Text('Written by:', size=40),
        ft.Text('Muhammad Altaaf', size=20),
        ft.Row([
            ft.Text('Source: ', size=15),
            ft.IconButton(ft.icons.SOURCE_ROUNDED, on_click=lambda _:page.launch_url(github_repo))
        ], alignment='center', vertical_alignment='center')
    ], alignment='center', horizontal_alignment='center', expand=True, visible=False)
    
    page.add(view, about)
    
    
if __name__ == '__main__':
    ft.app(target=main)
