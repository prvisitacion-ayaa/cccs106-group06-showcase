import flet as ft

from login import login_screen
from register import register_screen
from student import student_screen
from admin import admin_screen


def main(page: ft.Page):

    page.title = "Learn2Earn"
    page.window.width = 1100
    page.window.height = 750
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    def show_login():
        page.controls.clear()
        page.add(
            login_screen(
                page,
                show_student,
                show_admin,
                show_register
            )
        )
        page.update()

    def show_register():
        page.controls.clear()
        page.add(
            register_screen(
                page,
                show_login
            )
        )
        page.update()

    def show_student():
        page.controls.clear()
        page.add(
            student_screen(
                page,
                show_login
            )
        )
        page.update()

    def show_admin():
        page.controls.clear()
        page.add(
            admin_screen(
                page,
                show_login
            )
        )
        page.update()

    show_login()


if __name__ == "__main__":
    ft.run(main)