import flet as ft

from app.ui.components import (
    sidebar,
    stat_card,
    section_title,
    note_card,
)


BLUE = "#1455A0"
YELLOW = "#FFD740"


def admin_screen(page, show_login):

    current_page = "dashboard"

    main_area = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
    )

    def change_page(key):
        nonlocal current_page
        current_page = key
        render_page()

    def logout():
        show_login()

    def toggle_theme(e):

        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        render_page()

    def render_page():

        main_area.controls.clear()

        if current_page == "dashboard":
            main_area.controls.append(dashboard())

        elif current_page == "users":
            main_area.controls.append(users())

        elif current_page == "submissions":
            main_area.controls.append(submissions())

        elif current_page == "activity":
            main_area.controls.append(activity())

        page.update()

    def top_bar(title):

        return ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            title,
                            size=25,
                            weight=ft.FontWeight.BOLD,
                            color=(
                                BLUE
                                if page.theme_mode == ft.ThemeMode.LIGHT
                                else ft.Colors.WHITE
                            ),
                        ),
                        ft.Text(
                            "Learn2Earn Administration",
                            size=13,
                            color="#71808A",
                        ),
                    ],
                    spacing=2,
                ),
                ft.Container(expand=True),
                ft.IconButton(
                    icon=(
                        ft.Icons.DARK_MODE
                        if page.theme_mode == ft.ThemeMode.LIGHT
                        else ft.Icons.LIGHT_MODE
                    ),
                    tooltip="Switch theme",
                    on_click=toggle_theme,
                ),
                ft.CircleAvatar(
                    content=ft.Text(
                        "A",
                        color=ft.Colors.WHITE,
                    ),
                    bgcolor=BLUE,
                ),
            ],
        )

    def dashboard():

        return ft.Column(
            controls=[
                top_bar("Admin Dashboard"),

                ft.Container(height=20),

                ft.Text(
                    "System Overview",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    "Monitor users, resources, and submitted academic content.",
                    size=13,
                    color="#71808A",
                ),

                ft.Container(height=18),

                ft.Row(
                    controls=[
                        stat_card(
                            "Total Users",
                            "120",
                            ft.Icons.PEOPLE_OUTLINE,
                            "Registered students",
                        ),
                        stat_card(
                            "Resources",
                            "340",
                            ft.Icons.DESCRIPTION_OUTLINED,
                            "Learning resources",
                        ),
                        stat_card(
                            "Pending",
                            "8",
                            ft.Icons.PENDING_ACTIONS,
                            "Awaiting moderation",
                        ),
                    ],
                    spacing=15,
                ),

                ft.Container(height=30),

                section_title(
                    "Pending Submissions",
                    "Resources waiting for admin review.",
                ),

                ft.Container(height=12),

                submission_card(
                    "Python Programming Reviewer",
                    "Programming",
                ),

                submission_card(
                    "Database Management Notes",
                    "Database",
                ),

                submission_card(
                    "Computer Networks Reviewer",
                    "Networking",
                ),
            ],
            spacing=8,
        )

    def submission_card(title, subject):

        def approve(e):

            e.control.disabled = True
            e.control.text = "Approved"
            e.control.icon = ft.Icons.CHECK
            page.update()

        def reject(e):

            e.control.disabled = True
            e.control.text = "Rejected"
            e.control.icon = ft.Icons.CLOSE
            page.update()

        return ft.Container(
            padding=18,
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            border=ft.Border.all(1, "#E1E7ED"),
            content=ft.Row(
                controls=[
                    ft.Icon(
                        ft.Icons.DESCRIPTION_OUTLINED,
                        color=BLUE,
                        size=30,
                    ),

                    ft.Column(
                        controls=[
                            ft.Text(
                                title,
                                size=15,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                subject,
                                size=12,
                                color="#71808A",
                            ),
                        ],
                        expand=True,
                    ),

                    ft.ElevatedButton(
                        "Approve",
                        icon=ft.Icons.CHECK,
                        on_click=approve,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.GREEN_600,
                            color=ft.Colors.WHITE,
                        ),
                    ),

                    ft.OutlinedButton(
                        "Reject",
                        icon=ft.Icons.CLOSE,
                        on_click=reject,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def users():

        return ft.Column(
            controls=[
                top_bar("Users"),

                ft.Container(height=20),

                section_title(
                    "Registered Users",
                    "Manage Learn2Earn student accounts.",
                ),

                ft.Container(height=15),

                ft.TextField(
                    hint_text="Search users...",
                    prefix_icon=ft.Icons.SEARCH,
                ),

                ft.Container(height=10),

                user_row(
                    "Student User",
                    "student@cspc.edu.ph",
                    "BS Computer Science",
                ),

                user_row(
                    "Maria Santos",
                    "maria@cspc.edu.ph",
                    "BS Information Technology",
                ),

                user_row(
                    "John Cruz",
                    "john@cspc.edu.ph",
                    "BS Computer Science",
                ),
            ],
            spacing=10,
        )

    def user_row(name, email, course):

        return ft.Container(
            padding=16,
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            border=ft.Border.all(1, "#E1E7ED"),
            content=ft.Row(
                controls=[
                    ft.CircleAvatar(
                        content=ft.Text(
                            name[0],
                            color=ft.Colors.WHITE,
                        ),
                        bgcolor=BLUE,
                    ),

                    ft.Column(
                        controls=[
                            ft.Text(
                                name,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                email,
                                size=12,
                                color="#71808A",
                            ),
                            ft.Text(
                                course,
                                size=12,
                                color="#71808A",
                            ),
                        ],
                        expand=True,
                    ),

                    ft.TextButton("View"),
                ],
            ),
        )

    def submissions():

        return ft.Column(
            controls=[
                top_bar("Resource Submissions"),

                ft.Container(height=20),

                section_title(
                    "Content Moderation",
                    "Review and evaluate submitted learning resources.",
                ),

                ft.Container(height=15),

                submission_card(
                    "Python Programming Reviewer",
                    "Programming",
                ),

                submission_card(
                    "Database Management Notes",
                    "Database",
                ),

                submission_card(
                    "Data Structures Reviewer",
                    "Data Structures",
                ),

                submission_card(
                    "Software Engineering Notes",
                    "Software Engineering",
                ),
            ],
            spacing=12,
        )

    def activity():

        return ft.Column(
            controls=[
                top_bar("Activity"),

                ft.Container(height=20),

                section_title(
                    "System Activity",
                    "Recent activity within the platform.",
                ),

                ft.Container(height=15),

                activity_row(
                    "New resource submitted",
                    "Python Programming Reviewer",
                ),

                activity_row(
                    "Resource approved",
                    "Database Management Notes",
                ),

                activity_row(
                    "New student registered",
                    "Student User",
                ),

                activity_row(
                    "Resource reported",
                    "Computer Networks Reviewer",
                ),
            ],
            spacing=10,
        )

    def activity_row(action, detail):

        return ft.Container(
            padding=18,
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            border=ft.Border.all(1, "#E1E7ED"),
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=42,
                        height=42,
                        border_radius=21,
                        bgcolor="#E8F0FA",
                        alignment=ft.Alignment(0, 0),
                        content=ft.Icon(
                            ft.Icons.HISTORY,
                            color=BLUE,
                        ),
                    ),

                    ft.Column(
                        controls=[
                            ft.Text(
                                action,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                detail,
                                size=12,
                                color="#71808A",
                            ),
                        ],
                        expand=True,
                    ),

                    ft.Text(
                        "Today",
                        size=12,
                        color="#71808A",
                    ),
                ],
            ),
        )

    render_page()

    return ft.Row(
        controls=[
            sidebar(
                change_page,
                logout,
                admin=True,
            ),

            ft.Container(
                expand=True,
                padding=30,
                content=main_area,
            ),
        ],
        expand=True,
    )