import flet as ft


BLUE = "#1455A0"
BLUE_DARK = "#0D3B73"
YELLOW = "#FFD740"


def logo(size=26, dark=False):

    return ft.Row(
        controls=[
            ft.Text(
                "Learn",
                size=size,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
            ft.Text(
                "2",
                size=size,
                weight=ft.FontWeight.BOLD,
                color=YELLOW,
            ),
            ft.Text(
                "Earn",
                size=size,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
        ],
        spacing=0,
    )


def sidebar(on_page_change, on_logout, admin=False):

    if admin:
        items = [
            ("Dashboard", ft.Icons.DASHBOARD_OUTLINED, "dashboard"),
            ("Users", ft.Icons.PEOPLE_OUTLINE, "users"),
            ("Submissions", ft.Icons.RATE_REVIEW_OUTLINED, "submissions"),
            ("Activity", ft.Icons.ANALYTICS_OUTLINED, "activity"),
        ]
    else:
        items = [
            ("Dashboard", ft.Icons.DASHBOARD_OUTLINED, "dashboard"),
            ("Browse Notes", ft.Icons.SEARCH, "browse"),
            ("Upload Note", ft.Icons.UPLOAD_FILE_OUTLINED, "upload"),
            ("My Notes", ft.Icons.DESCRIPTION_OUTLINED, "my_notes"),
            ("Saved Notes", ft.Icons.BOOKMARK_BORDER, "saved"),
            ("Learn Points", ft.Icons.STARS_OUTLINED, "points"),
            ("AI Note Assistant", ft.Icons.AUTO_AWESOME_OUTLINED, "ai"),
            ("Profile", ft.Icons.PERSON_OUTLINE, "profile"),
        ]

    controls = [
        ft.Container(
            padding=ft.Padding(
                left=22,
                right=15,
                top=25,
                bottom=20,
            ),
            content=logo(27),
        ),
        ft.Divider(
            height=1,
            color="#3972B7",
        ),
    ]

    for label, icon, key in items:

        controls.append(
            ft.Container(
                padding=ft.Padding(
                    left=20,
                    right=10,
                    top=6,
                    bottom=6,
                ),
                content=ft.TextButton(
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                icon,
                                color=ft.Colors.WHITE,
                                size=21,
                            ),
                            ft.Text(
                                label,
                                color=ft.Colors.WHITE,
                                size=14,
                            ),
                        ],
                        spacing=14,
                    ),
                    on_click=lambda e, k=key: on_page_change(k),
                ),
            )
        )

    controls.append(
        ft.Container(
            expand=True,
        )
    )

    controls.append(
        ft.Container(
            padding=20,
            content=ft.TextButton(
                content=ft.Row(
                    controls=[
                        ft.Icon(
                            ft.Icons.LOGOUT,
                            color=ft.Colors.WHITE,
                        ),
                        ft.Text(
                            "Logout",
                            color=ft.Colors.WHITE,
                            size=14,
                        ),
                    ],
                    spacing=14,
                ),
                on_click=lambda e: on_logout(),
            ),
        )
    )

    return ft.Container(
        width=240,
        bgcolor=BLUE_DARK,
        content=ft.Column(
            controls=controls,
            spacing=2,
        ),
    )


def stat_card(title, value, icon, description=""):

    return ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=14,
        border=ft.Border.all(1, "#E1E7ED"),
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            width=42,
                            height=42,
                            border_radius=10,
                            bgcolor="#E8F0FA",
                            alignment=ft.Alignment(0, 0),
                            content=ft.Icon(
                                icon,
                                color=BLUE,
                                size=22,
                            ),
                        ),
                        ft.Container(expand=True),
                        ft.Text(
                            value,
                            size=25,
                            weight=ft.FontWeight.BOLD,
                            color=BLUE,
                        ),
                    ]
                ),
                ft.Text(
                    title,
                    size=14,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    description,
                    size=12,
                    color="#71808A",
                ),
            ],
            spacing=8,
        ),
    )


def section_title(title, subtitle=""):

    controls = [
        ft.Text(
            title,
            size=21,
            weight=ft.FontWeight.BOLD,
            color=BLUE,
        )
    ]

    if subtitle:
        controls.append(
            ft.Text(
                subtitle,
                size=13,
                color="#71808A",
            )
        )

    return ft.Column(
        controls=controls,
        spacing=3,
    )


def note_card(
    title,
    subject,
    topic,
    course,
    level,
    status="Approved",
    points=10,
    on_view=None,
):

    return ft.Container(
        padding=18,
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        border=ft.Border.all(1, "#E1E7ED"),
        content=ft.Row(
            controls=[
                ft.Container(
                    width=48,
                    height=48,
                    border_radius=10,
                    bgcolor="#E8F0FA",
                    alignment=ft.Alignment(0, 0),
                    content=ft.Icon(
                        ft.Icons.DESCRIPTION_OUTLINED,
                        color=BLUE,
                    ),
                ),

                ft.Container(
                    expand=True,
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                title,
                                size=16,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                f"{subject} • {topic}",
                                size=13,
                                color="#607784",
                            ),
                            ft.Text(
                                f"{course} • {level}",
                                size=12,
                                color="#7B8790",
                            ),
                        ],
                        spacing=3,
                    ),
                ),

                ft.Column(
                    controls=[
                        ft.Text(
                            status,
                            size=11,
                            color=(
                                ft.Colors.GREEN_700
                                if status == "Approved"
                                else ft.Colors.ORANGE_700
                            ),
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            f"+{points} Learn Points",
                            size=12,
                            color="#C79500",
                            weight=ft.FontWeight.BOLD,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                ),

                ft.IconButton(
                    icon=ft.Icons.CHEVRON_RIGHT,
                    icon_color=BLUE,
                    on_click=on_view,
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )