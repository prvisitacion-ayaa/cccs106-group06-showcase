import flet as ft
from team_profiles import get_initial_team, build_profile_card


def main(page: ft.Page):

    page.title = "Learn2Earn"
    page.window.width = 1000
    page.window.height = 700
    page.theme_mode = ft.ThemeMode.LIGHT

    team_members = get_initial_team()

    completed_tasks = 0
    sprint_goal = 5

    # ---------------------------------------------------------
    # SPRINT STATUS
    # ---------------------------------------------------------
    sprint_counter = ft.Text(
        "Sprint Counter: 0",
        size=18,
        weight=ft.FontWeight.BOLD,
    )

    sprint_status = ft.Text(
        "IN PROGRESS",
        size=16,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.ORANGE,
    )

    # ---------------------------------------------------------
    # COMPLETE TASK BUTTON
    # ---------------------------------------------------------
    def complete_task(e):

        nonlocal completed_tasks

        if completed_tasks < sprint_goal:
            completed_tasks += 1

        sprint_counter.value = f"Sprint Counter: {completed_tasks}"

        if completed_tasks >= sprint_goal:
            sprint_status.value = "SPRINT GOAL MET (5/5)"
            sprint_status.color = ft.Colors.GREEN
            complete_button.disabled = True
        else:
            sprint_status.value = "IN PROGRESS"
            sprint_status.color = ft.Colors.ORANGE

        page.update()

    complete_button = ft.ElevatedButton(
        "Complete Task",
        icon=ft.Icons.CHECK,
        on_click=complete_task,
    )

    # ---------------------------------------------------------
    # DARK MODE
    # ---------------------------------------------------------
    def toggle_theme(e):

        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    theme_button = ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        tooltip="Toggle Dark Mode",
        on_click=toggle_theme,
    )

    # ---------------------------------------------------------
    # HEADER
    # ---------------------------------------------------------
    header = ft.Row(
        controls=[
            ft.Text(
                "Learn2Earn",
                size=28,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Text(
                "Camarines Sur Polytechnic Colleges",
                size=14,
            ),
            ft.Container(expand=True),
            theme_button,
        ],
        alignment=ft.MainAxisAlignment.START,
    )

    # ---------------------------------------------------------
    # TEAM MEMBER CARDS
    # ---------------------------------------------------------
    team_cards = ft.Column(
        controls=[
            build_profile_card(member)
            for member in team_members
        ],
        spacing=10,
    )

    # ---------------------------------------------------------
    # MAIN CONTENT
    # ---------------------------------------------------------
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    header,

                    ft.Divider(),

                    ft.Text(
                        "Team Members",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                    ),

                    team_cards,

                    ft.Divider(),

                    ft.Text(
                        "Sprint Progress",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                    ),

                    sprint_counter,

                    sprint_status,

                    complete_button,
                ],
                spacing=15,
            ),
            padding=25,
        )
    )


ft.app(target=main)
