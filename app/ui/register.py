import flet as ft
from app.backend.auth import register_user


BLUE = "#1455A0"
YELLOW = "#FFD740"

LIGHT_BG = "#F4F7FA"
DARK_BG = "#26343B"

LIGHT_CARD = "#FFFFFF"
DARK_CARD = "#37474F"


def register_screen(page, show_login):

    dark = page.theme_mode == ft.ThemeMode.DARK

    full_name = ft.TextField(
        label="Full Name",
        width=400,
        height=55,
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        border_radius=10,
    )

    email = ft.TextField(
        label="CSPC Email",
        hint_text="you@my.cspc.edu.ph",
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

    course = ft.TextField(
        label="Course",
        hint_text="Example: BS Computer Science",
        width=400,
        height=55,
        prefix_icon=ft.Icons.SCHOOL_OUTLINED,
        border_radius=10,
    )

    year_level = ft.TextField(
        label="Year Level",
        hint_text="Example: 1st Year",
        width=400,
        height=55,
        prefix_icon=ft.Icons.NUMBERS,
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
        size=36,
        weight=ft.FontWeight.BOLD,
        color=BLUE if not dark else ft.Colors.WHITE,
    )

    number_text = ft.Text(
        "2",
        size=36,
        weight=ft.FontWeight.BOLD,
        color=YELLOW,
    )

    earn_text = ft.Text(
        "Earn",
        size=36,
        weight=ft.FontWeight.BOLD,
        color=BLUE if not dark else ft.Colors.WHITE,
    )

    logo = ft.Row(
        controls=[
            learn_text,
            number_text,
            earn_text,
        ],
        spacing=0,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # =========================
    # REGISTER FUNCTION
    # =========================

    def register(e):

        if (
            not full_name.value
            or not email.value
            or not password.value
            or not course.value
            or not year_level.value
        ):
            message.value = "Please complete all fields."
            message.color = ft.Colors.RED_400
            page.update()
            return

        email_address = email.value.strip().lower()

        if not email_address.endswith("@my.cspc.edu.ph"):
            message.value = "Please use a valid CSPC email address."
            message.color = ft.Colors.RED_400
            page.update()
            return

        result = register_user(
            full_name.value,
            email_address,
            password.value,
            course.value,
            year_level.value,
        )

        message.value = result["message"]

        if result["success"]:

            message.color = ft.Colors.GREEN_600

            full_name.value = ""
            email.value = ""
            password.value = ""
            course.value = ""
            year_level.value = ""

        else:

            message.color = ft.Colors.RED_400

        page.update()

    # =========================
    # CARD CONTENT
    # =========================

    welcome_title = ft.Text(
        "Create Account",
        size=25,
        weight=ft.FontWeight.BOLD,
        color=BLUE if not dark else ft.Colors.WHITE,
    )

    welcome_text = ft.Text(
        "Join the Learn2Earn academic community",
        size=14,
        color="#607784" if not dark else "#C4CED3",
    )

    create_button = ft.ElevatedButton(
        "Create Account",
        width=400,
        height=50,
        icon=ft.Icons.PERSON_ADD,
        on_click=register,
        style=ft.ButtonStyle(
            bgcolor=BLUE,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
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

                ft.Container(height=5),

                full_name,
                email,
                password,
                course,
                year_level,

                ft.Container(height=3),

                create_button,

                ft.Row(
                    controls=[
                        ft.Text(
                            "Already have an account?",
                            color=(
                                "#263238"
                                if not dark
                                else ft.Colors.WHITE
                            ),
                        ),
                        ft.TextButton(
                            "Login",
                            style=ft.ButtonStyle(
                                color=BLUE,
                            ),
                            on_click=lambda e: show_login(),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),

                message,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
    )

    # =========================
    # THEME FUNCTION
    # =========================

    def toggle_theme(e):

        nonlocal dark

        dark = not dark

        page.theme_mode = (
            ft.ThemeMode.DARK
            if dark
            else ft.ThemeMode.LIGHT
        )

        page_bg.bgcolor = (
            DARK_BG
            if dark
            else LIGHT_BG
        )

        card.bgcolor = (
            DARK_CARD
            if dark
            else LIGHT_CARD
        )

        learn_text.color = (
            ft.Colors.WHITE
            if dark
            else BLUE
        )

        earn_text.color = (
            ft.Colors.WHITE
            if dark
            else BLUE
        )

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

        theme_button.icon = (
            ft.Icons.LIGHT_MODE
            if dark
            else ft.Icons.DARK_MODE
        )

        theme_button_container.bgcolor = (
            "#455A64"
            if dark
            else "#E7EBEF"
        )

        page.update()

    # =========================
    # THEME BUTTON
    # =========================

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
        bgcolor=(
            "#E7EBEF"
            if not dark
            else "#455A64"
        ),
        alignment=ft.Alignment(0, 0),
        content=theme_button,
    )

    # =========================
    # PAGE CONTENT
    # =========================

    content = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Container(expand=True),
                    theme_button_container,
                ],
            ),

            ft.Container(height=10),

            logo,

            ft.Container(height=10),

            card,

            ft.Container(expand=True),

            ft.Text(
                "CSPC • College of Computer Studies",
                size=13,
                color=(
                    "#607784"
                    if not dark
                    else "#B8C5CB"
                ),
            ),
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