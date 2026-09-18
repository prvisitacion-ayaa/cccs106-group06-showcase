import flet as ft


BLUE = "#1769C2"
BLUE_DARK = "#0D4380"
YELLOW = "#FFD43B"

LIGHT_BG = "#F5F9FE"
DARK_BG = "#0A2030"

LIGHT_CARD = "#FFFFFF"
DARK_CARD = "#203B50"

LIGHT_TEXT = "#263B4D"
MUTED_TEXT = "#607B91"
DARK_MUTED = "#C1D0DB"


def login_screen(page, show_student, show_admin, show_register):

    dark = page.theme_mode == ft.ThemeMode.DARK

    # ==========================================
    # LOGIN INPUTS
    # ==========================================

    email = ft.TextField(
        hint_text="Email or Username",
        width=440,
        height=56,
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        border_radius=12,
        border_width=1,
        border_color="#C9D9E8" if not dark else "#557187",
        focused_border_color=BLUE,
        bgcolor="#FFFFFF" if not dark else "#294559",
        color=LIGHT_TEXT if not dark else ft.Colors.WHITE,
        hint_style=ft.TextStyle(
            color=MUTED_TEXT if not dark else "#B7C8D4"
        ),
    )

    password = ft.TextField(
        hint_text="Enter your password",
        width=440,
        height=56,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK_OUTLINED,
        border_radius=12,
        border_width=1,
        border_color="#C9D9E8" if not dark else "#557187",
        focused_border_color=BLUE,
        bgcolor="#FFFFFF" if not dark else "#294559",
        color=LIGHT_TEXT if not dark else ft.Colors.WHITE,
        hint_style=ft.TextStyle(
            color=MUTED_TEXT if not dark else "#B7C8D4"
        ),
    )

    message = ft.Text(
        "",
        size=13,
        text_align=ft.TextAlign.CENTER,
    )

    # ==========================================
    # BACKGROUND
    # ==========================================

    page_bg = ft.Container(
        expand=True,
        bgcolor=LIGHT_BG if not dark else DARK_BG,
    )

    top_circle = ft.Container(
        width=330,
        height=330,
        border_radius=165,
        bgcolor="#DCEEFF" if not dark else "#153B59",
        opacity=0.75,
        left=-100,
        top=-120,
    )

    bottom_circle = ft.Container(
        width=280,
        height=280,
        border_radius=140,
        bgcolor="#E5F1FF" if not dark else "#12354F",
        opacity=0.75,
        right=-100,
        bottom=-120,
    )

    # ==========================================
    # LOGO
    # ==========================================

    logo_book = ft.Container(
        width=76,
        height=62,
        border_radius=15,
        bgcolor="#DCEEFF" if not dark else "#294D69",
        alignment=ft.Alignment(0, 0),
        content=ft.Icon(
            ft.Icons.MENU_BOOK_ROUNDED,
            size=43,
            color=BLUE if not dark else "#65B2FF",
        ),
    )

    logo_cap = ft.Container(
        width=31,
        height=31,
        border_radius=16,
        bgcolor=YELLOW,
        alignment=ft.Alignment(0, 0),
        content=ft.Icon(
            ft.Icons.SCHOOL_ROUNDED,
            size=19,
            color=BLUE_DARK,
        ),
    )

    logo_star1 = ft.Text(
        "★",
        size=18,
        color=YELLOW,
        weight=ft.FontWeight.BOLD,
    )

    logo_star2 = ft.Text(
        "✦",
        size=13,
        color=YELLOW,
        weight=ft.FontWeight.BOLD,
    )

    logo = ft.Stack(
        controls=[
            ft.Container(
                content=logo_book,
                left=8,
                top=20,
            ),

            ft.Container(
                content=logo_cap,
                left=51,
                top=1,
            ),

            ft.Container(
                content=logo_star1,
                left=69,
                top=27,
            ),

            ft.Container(
                content=logo_star2,
                left=3,
                top=12,
            ),
        ],
        width=100,
        height=88,
    )

    # ==========================================
    # APP TITLE
    # ==========================================

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
        color="#315E84" if not dark else "#C1D0DB",
        text_align=ft.TextAlign.CENTER,
    )

    # ==========================================
    # WELCOME
    # ==========================================

    welcome_title = ft.Text(
        "Welcome Back!",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=BLUE_DARK if not dark else ft.Colors.WHITE,
    )

    welcome_text = ft.Text(
        "Sign in to continue learning and sharing.",
        size=14,
        color=MUTED_TEXT if not dark else DARK_MUTED,
        text_align=ft.TextAlign.CENTER,
    )

    # ==========================================
    # LOGIN FUNCTION
    # ==========================================

    def login(e):

        username = email.value.strip()
        user_password = password.value.strip()

        if not username or not user_password:

            message.value = (
                "Please enter your email/username and password."
            )

            message.color = ft.Colors.RED_400

            page.update()

            return

        if username.lower() in (
            "admin",
            "admin@cspc.edu.ph",
        ):

            show_admin()

        else:

            show_student()

    # ==========================================
    # FORGOT PASSWORD
    # ==========================================

    def forgot_password_clicked(e):

        reset_email = ft.TextField(
            label="Email or Username",
            hint_text="Enter your registered email",
            prefix_icon=ft.Icons.EMAIL_OUTLINED,
            width=400,
        )

        reset_message = ft.Text(
            "",
            size=13,
            text_align=ft.TextAlign.CENTER,
        )

        def send_reset(e):

            if not reset_email.value.strip():

                reset_message.value = (
                    "Please enter your email or username."
                )

                reset_message.color = ft.Colors.RED

            else:

                reset_message.value = (
                    "Password reset instructions have been sent."
                )

                reset_message.color = ft.Colors.GREEN

            page.update()

        def close_dialog(e):

            page.pop_dialog()

        dialog = ft.AlertDialog(
            modal=True,

            title=ft.Text(
                "Forgot Password?"
            ),

            content=ft.Column(
                controls=[
                    ft.Text(
                        "Enter your email or username "
                        "to reset your password."
                    ),

                    reset_email,

                    reset_message,
                ],

                tight=True,
            ),

            actions=[
                ft.TextButton(
                    "Cancel",
                    on_click=close_dialog,
                ),

                ft.ElevatedButton(
                    "Send Reset Link",
                    icon=ft.Icons.SEND,
                    on_click=send_reset,
                ),
            ],

            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.show_dialog(dialog)

    forgot_password = ft.TextButton(
        "Forgot Password?",

        style=ft.ButtonStyle(
            color=BLUE,
            padding=ft.Padding(
                0,
                0,
                0,
                0,
            ),
        ),

        on_click=forgot_password_clicked,
    )

    # ==========================================
    # REMEMBER ME
    # ==========================================

    remember_checkbox = ft.Checkbox(
        label="Remember me",
        value=False,
        active_color=BLUE,
        check_color=ft.Colors.WHITE,

        label_style=ft.TextStyle(
            size=13,
            color=LIGHT_TEXT if not dark else "#D7E1E8",
        ),
    )

    account_options = ft.Row(
        controls=[
            remember_checkbox,

            ft.Container(
                expand=True,
            ),

            forgot_password,
        ],

        width=440,

        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # ==========================================
    # LOGIN BUTTON
    # ==========================================

    login_button = ft.ElevatedButton(
        "Login",

        width=440,
        height=55,

        icon=ft.Icons.LOGIN_ROUNDED,

        on_click=login,

        style=ft.ButtonStyle(
            bgcolor=BLUE,
            color=ft.Colors.WHITE,
            elevation=3,

            shape=ft.RoundedRectangleBorder(
                radius=12,
            ),
        ),
    )

    # ==========================================
    # REGISTER
    # ==========================================

    register_text = ft.Text(
        "Don't have an account?",
        size=13,
        color=LIGHT_TEXT if not dark else "#D7E1E8",
    )

    register_button = ft.TextButton(
        "Register",

        style=ft.ButtonStyle(
            color=BLUE,

            padding=ft.Padding(
                4,
                0,
                4,
                0,
            ),
        ),

        on_click=lambda e: show_register(),
    )

    divider_left = ft.Container(
        width=65,
        height=1,

        bgcolor=(
            "#D5E1EB"
            if not dark
            else "#50697B"
        ),
    )

    divider_right = ft.Container(
        width=65,
        height=1,

        bgcolor=(
            "#D5E1EB"
            if not dark
            else "#50697B"
        ),
    )

    register_row = ft.Row(
        controls=[
            divider_left,

            register_text,

            register_button,

            divider_right,
        ],

        alignment=ft.MainAxisAlignment.CENTER,

        vertical_alignment=ft.CrossAxisAlignment.CENTER,

        spacing=6,
    )

    # ==========================================
    # LOGIN CARD
    # ==========================================

    card = ft.Container(
        width=520,

        padding=ft.Padding(
            42,
            30,
            42,
            25,
        ),

        bgcolor=(
            LIGHT_CARD
            if not dark
            else DARK_CARD
        ),

        border_radius=22,

        border=ft.Border.all(
            1,

            (
                "#DDE8F1"
                if not dark
                else "#3E5A6D"
            ),
        ),

        shadow=ft.BoxShadow(
            blur_radius=28,
            spread_radius=1,

            offset=ft.Offset(
                0,
                10,
            ),

            color=(
                "#00000022"
                if not dark
                else "#00000060"
            ),
        ),

        content=ft.Column(
            controls=[
                welcome_title,

                welcome_text,

                ft.Container(
                    height=10,
                ),

                email,

                password,

                account_options,

                ft.Container(
                    height=2,
                ),

                login_button,

                ft.Container(
                    height=8,
                ),

                register_row,

                message,
            ],

            horizontal_alignment=(
                ft.CrossAxisAlignment.CENTER
            ),

            spacing=9,
        ),
    )

    # ==========================================
    # THEME BUTTON
    # ==========================================

    theme_button = ft.IconButton(
        icon=(
            ft.Icons.DARK_MODE_ROUNDED
            if not dark
            else ft.Icons.LIGHT_MODE_ROUNDED
        ),

        icon_size=22,

        icon_color=(
            "#344D60"
            if not dark
            else "#FFFFFF"
        ),

        tooltip="Switch theme",
    )

    theme_button_container = ft.Container(
        width=50,
        height=50,

        border_radius=25,

        bgcolor=(
            "#E4EFF8"
            if not dark
            else "#2B4A62"
        ),

        alignment=ft.Alignment(
            0,
            0,
        ),

        content=theme_button,
    )

    # ==========================================
    # FOOTER
    # ==========================================

    footer = ft.Text(
        "CSPC • College of Computer Studies",

        size=13,

        color=(
            MUTED_TEXT
            if not dark
            else "#B7C8D4"
        ),
    )

    # ==========================================
    # THEME TOGGLE
    # ==========================================

    def toggle_theme(e):

        nonlocal dark

        dark = not dark

        page.theme_mode = (
            ft.ThemeMode.DARK
            if dark
            else ft.ThemeMode.LIGHT
        )

        # Background

        page_bg.bgcolor = (
            DARK_BG
            if dark
            else LIGHT_BG
        )

        top_circle.bgcolor = (
            "#153B59"
            if dark
            else "#DCEEFF"
        )

        bottom_circle.bgcolor = (
            "#12354F"
            if dark
            else "#E5F1FF"
        )

        # Card

        card.bgcolor = (
            DARK_CARD
            if dark
            else LIGHT_CARD
        )

        card.border = ft.Border.all(
            1,
            (
                "#3E5A6D"
                if dark
                else "#DDE8F1"
            ),
        )

        # Logo

        logo_book.bgcolor = (
            "#294D69"
            if dark
            else "#DCEEFF"
        )

        logo_book.content.color = (
            "#65B2FF"
            if dark
            else BLUE
        )

        # Title

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

        number_text.color = YELLOW

        # Subtitle

        subtitle.color = (
            "#C1D0DB"
            if dark
            else "#315E84"
        )

        # Welcome

        welcome_title.color = (
            ft.Colors.WHITE
            if dark
            else BLUE_DARK
        )

        welcome_text.color = (
            DARK_MUTED
            if dark
            else MUTED_TEXT
        )

        # Inputs

        email.bgcolor = (
            "#294559"
            if dark
            else "#FFFFFF"
        )

        password.bgcolor = (
            "#294559"
            if dark
            else "#FFFFFF"
        )

        email.border_color = (
            "#557187"
            if dark
            else "#C9D9E8"
        )

        password.border_color = (
            "#557187"
            if dark
            else "#C9D9E8"
        )

        email.hint_style = ft.TextStyle(
            color=(
                "#B7C8D4"
                if dark
                else MUTED_TEXT
            )
        )

        password.hint_style = ft.TextStyle(
            color=(
                "#B7C8D4"
                if dark
                else MUTED_TEXT
            )
        )

        # Remember Me

        remember_checkbox.label_style = ft.TextStyle(
            size=13,

            color=(
                "#D7E1E8"
                if dark
                else LIGHT_TEXT
            ),
        )

        # Register

        register_text.color = (
            "#D7E1E8"
            if dark
            else LIGHT_TEXT
        )

        divider_left.bgcolor = (
            "#50697B"
            if dark
            else "#D5E1EB"
        )

        divider_right.bgcolor = (
            "#50697B"
            if dark
            else "#D5E1EB"
        )

        # Theme Button

        theme_button.icon = (
            ft.Icons.LIGHT_MODE_ROUNDED
            if dark
            else ft.Icons.DARK_MODE_ROUNDED
        )

        theme_button.icon_color = (
            "#FFFFFF"
            if dark
            else "#344D60"
        )

        theme_button_container.bgcolor = (
            "#2B4A62"
            if dark
            else "#E4EFF8"
        )

        # Footer

        footer.color = (
            "#B7C8D4"
            if dark
            else MUTED_TEXT
        )

        page.update()

    theme_button.on_click = toggle_theme

    # ==========================================
    # MAIN CONTENT
    # ==========================================

    content = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Container(
                        expand=True,
                    ),

                    theme_button_container,
                ],
            ),

            ft.Container(
                height=0,
            ),

            logo,

            ft.Container(
                height=0,
            ),

            title,

            ft.Container(
                height=2,
            ),

            subtitle,

            ft.Container(
                height=10,
            ),

            card,

            ft.Container(
                expand=True,
            ),

            footer,

            ft.Container(
                height=3,
            ),
        ],

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # ==========================================
    # RETURN PAGE
    # ==========================================

    return ft.Stack(
        controls=[
            page_bg,

            top_circle,

            bottom_circle,

            ft.Container(
                expand=True,

                padding=ft.Padding(
                    25,
                    10,
                    25,
                    8,
                ),

                content=content,
            ),
        ],

        expand=True,
    )