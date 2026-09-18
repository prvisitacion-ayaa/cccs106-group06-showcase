import flet as ft


BLUE = "#1455A0"
BLUE_DARK = "#0D3B73"
YELLOW = "#FFD740"

LIGHT_BG = "#F4F7FA"
DARK_BG = "#26343B"

LIGHT_CARD = "#FFFFFF"
DARK_CARD = "#37474F"


def login_screen(page, show_student, show_admin, show_register):

    dark = page.theme_mode == ft.ThemeMode.DARK

    email = ft.TextField(
        label="CSPC Email",
        hint_text="you@cspc.edu.ph",
        width=400,
        height=55,
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        border_radius=10,
    )

    password = ft.TextField(
        label="Password",
        width=400,
        height=55,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK_OUTLINED,
        border_radius=10,
    )

    message = ft.Text(
        "",
        size=13,
        text_align=ft.TextAlign.CENTER,
    )

    page_bg = ft.Container(
        expand=True,
        bgcolor=LIGHT_BG if not dark else DARK_BG,
    )

    learn_text = ft.Text(
        "Learn",
        size=42,
        weight=ft.FontWeight.BOLD,
        color=BLUE if not dark else ft.Colors.WHITE,
    )

    number_text = ft.Text(
        "2",
        size=42,
        weight=ft.FontWeight.BOLD,
        color=YELLOW,
    )

    earn_text = ft.Text(
        "Earn",
        size=42,
        weight=ft.FontWeight.BOLD,
        color=BLUE if not dark else ft.Colors.WHITE,
    )

    title = ft.Row(
        controls=[
            learn_text,
            number_text,
            earn_text,
        ],
        spacing=0,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    subtitle = ft.Text(
        "Academic Note-Sharing and Reward Platform",
        size=16,
        color="#526875" if not dark else "#B8C5CB",
        text_align=ft.TextAlign.CENTER,
    )

    welcome_title = ft.Text(
        "Welcome Back!",
        size=27,
        weight=ft.FontWeight.BOLD,
        color=BLUE if not dark else ft.Colors.WHITE,
    )

    welcome_text = ft.Text(
        "Sign in to your Learn2Earn account",
        size=14,
        color="#607784" if not dark else "#C4CED3",
    )

    def login(e):

        if not email.value or not password.value:
            message.value = "Please enter your email and password."
            message.color = ft.Colors.RED_400
            page.update()
            return

        if not email.value.lower().endswith("@cspc.edu.ph"):
            message.value = "Please use a valid CSPC email address."
            message.color = ft.Colors.RED_400
            page.update()
            return

        if email.value.lower() == "admin@cspc.edu.ph":
            show_admin()
        else:
            show_student()

    forgot_password = ft.TextButton(
        "Forgot Password?",
        style=ft.ButtonStyle(
            color=BLUE,
        ),
    )

    login_button = ft.ElevatedButton(
        "Login",
        width=400,
        height=50,
        icon=ft.Icons.LOGIN,
        on_click=login,
        style=ft.ButtonStyle(
            bgcolor=BLUE,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    register_text = ft.Text(
        "Don't have an account?",
        color="#263238" if not dark else ft.Colors.WHITE,
    )

    register_row = ft.Row(
        controls=[
            register_text,
            ft.TextButton(
                "Register",
                style=ft.ButtonStyle(
                    color=BLUE,
                ),
                on_click=lambda e: show_register(),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    card = ft.Container(
        width=470,
        padding=30,
        bgcolor=LIGHT_CARD if not dark else DARK_CARD,
        border_radius=18,
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=1,
            offset=ft.Offset(0, 7),
        ),
        content=ft.Column(
            controls=[
                welcome_title,
                welcome_text,

                ft.Container(height=8),

                email,
                password,

                ft.Container(
                    alignment=ft.Alignment(1, 0),
                    content=forgot_password,
                ),

                ft.Container(height=3),

                login_button,

                ft.Container(height=5),

                register_row,

                message,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
        ),
    )

    def toggle_theme(e):

        nonlocal dark

        dark = not dark

        page.theme_mode = (
            ft.ThemeMode.DARK
            if dark
            else ft.ThemeMode.LIGHT
        )

        page_bg.bgcolor = DARK_BG if dark else LIGHT_BG
        card.bgcolor = DARK_CARD if dark else LIGHT_CARD

        learn_text.color = ft.Colors.WHITE if dark else BLUE
        earn_text.color = ft.Colors.WHITE if dark else BLUE

        subtitle.color = "#B8C5CB" if dark else "#526875"

        welcome_title.color = (
            ft.Colors.WHITE
            if dark
            else BLUE
        )

        welcome_text.color = (
            "#C4CED3"
            if dark
            else "#607784"
        )

        register_text.color = (
            ft.Colors.WHITE
            if dark
            else "#263238"
        )

        theme_button.icon = (
            ft.Icons.LIGHT_MODE
            if dark
            else ft.Icons.DARK_MODE
        )

        page.update()

    theme_button = ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        icon_size=22,
        tooltip="Switch theme",
        on_click=toggle_theme,
    )

    theme_button_container = ft.Container(
        width=44,
        height=44,
        border_radius=22,
        bgcolor="#E7EBEF" if not dark else "#455A64",
        alignment=ft.Alignment(0, 0),
        content=theme_button,
    )

    footer = ft.Text(
        "CSPC • College of Computer Studies",
        size=13,
        color="#607784" if not dark else "#B8C5CB",
    )

    content = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Container(expand=True),
                    theme_button_container,
                ],
            ),

            ft.Container(expand=True),

            title,

            ft.Container(height=5),

            subtitle,

            ft.Container(height=15),

            card,

            ft.Container(expand=True),

            footer,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return ft.Stack(
        controls=[
            page_bg,

            ft.Container(
                expand=True,
                padding=25,
                content=content,
            ),
        ],
        expand=True,
    )