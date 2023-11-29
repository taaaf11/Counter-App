import flet as ft


counter_value = 0

def main(page):
    page.title = 'Counter'
    
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
        
    
    button_reset = ft.IconButton(ft.icons.ROTATE_90_DEGREES_CCW_ROUNDED, on_click=reset_counter)
    counter_label  = ft.TextField(value='0', read_only=True)
    button_inc   = ft.IconButton(ft.icons.ADD_ROUNDED, on_click=increment_counter)
    
    
    view = ft.Row([
        button_reset,
        counter_label,
        button_inc
    ], alignment='center', vertical_alignment='center', expand=True)
    
    page.add(view)
    
    
if __name__ == '__main__':
    ft.app(target=main)