import flet as ft

from app.database.database import create_tables
from app.ui.login import login_screen
from app.ui.register import register_screen
from app.ui.student import student_screen
from app.ui.admin import admin_screen


def main(page: ft.Page):

    create_tables()

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
