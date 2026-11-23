import flet as ft

from app.ui.components import (
    sidebar,
    stat_card,
    section_title,
    note_card,
)


BLUE = "#1455A0"
YELLOW = "#FFD740"


def student_screen(page, show_login):

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

        elif current_page == "browse":
            main_area.controls.append(browse_notes())

        elif current_page == "upload":
            main_area.controls.append(upload_note())

        elif current_page == "my_notes":
            main_area.controls.append(my_notes())

        elif current_page == "saved":
            main_area.controls.append(saved_notes())

        elif current_page == "points":
            main_area.controls.append(learn_points())

        elif current_page == "ai":
            main_area.controls.append(ai_assistant())

        elif current_page == "profile":
            main_area.controls.append(profile())

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
                            "Learn2Earn Student Portal",
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
                        "S",
                        color=ft.Colors.WHITE,
                    ),
                    bgcolor=BLUE,
                ),
            ],
        )

    def dashboard():

        notes = note_card(
            "Introduction to Data Structures",
            "Data Structures",
            "Linked Lists",
            "BSCS",
            "1st Year",
            points=15,
        )

        notes2 = note_card(
            "Python Programming Reviewer",
            "Programming",
            "Python Basics",
            "BSCS",
            "1st Year",
            points=10,
        )

        return ft.Column(
            controls=[
                top_bar("Dashboard"),

                ft.Container(height=20),

                ft.Text(
                    "Welcome back, Student!",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    "Explore resources, share your notes, and earn Learn Points.",
                    size=13,
                    color="#71808A",
                ),

                ft.Container(height=18),

                ft.Row(
                    controls=[
                        stat_card(
                            "My Notes",
                            "12",
                            ft.Icons.DESCRIPTION_OUTLINED,
                            "Uploaded resources",
                        ),
                        stat_card(
                            "Saved Notes",
                            "8",
                            ft.Icons.BOOKMARK_BORDER,
                            "Saved resources",
                        ),
                        stat_card(
                            "Learn Points",
                            "150",
                            ft.Icons.STARS_OUTLINED,
                            "Current points",
                        ),
                    ],
                    spacing=15,
                ),

                ft.Container(height=30),

                section_title(
                    "Recent Learning Resources",
                    "Recently available academic materials",
                ),

                ft.Container(height=12),

                notes,
                notes2,
            ],
            spacing=8,
        )

    def browse_notes():

        search = ft.TextField(
            hint_text="Search learning resources...",
            prefix_icon=ft.Icons.SEARCH,
            expand=True,
            border_radius=10,
        )

        return ft.Column(
            controls=[
                top_bar("Browse Notes"),

                ft.Container(height=20),

                section_title(
                    "Learning Resources",
                    "Search and explore shared academic materials.",
                ),

                ft.Container(height=15),

                ft.Row(
                    controls=[
                        search,
                        ft.ElevatedButton(
                            "Search",
                            icon=ft.Icons.SEARCH,
                            style=ft.ButtonStyle(
                                bgcolor=BLUE,
                                color=ft.Colors.WHITE,
                            ),
                        ),
                    ],
                    spacing=10,
                ),

                ft.Container(height=20),

                note_card(
                    "Python Programming Reviewer",
                    "Programming",
                    "Python Basics",
                    "BSCS",
                    "1st Year",
                    points=10,
                ),

                note_card(
                    "Database Management Notes",
                    "Database",
                    "SQL Fundamentals",
                    "BSCS",
                    "2nd Year",
                    points=15,
                ),

                note_card(
                    "Computer Networks Reviewer",
                    "Networking",
                    "Network Fundamentals",
                    "BSCS",
                    "2nd Year",
                    points=20,
                ),
            ],
            spacing=12,
        )

    def upload_note():

        title = ft.TextField(
            label="Resource Title",
            width=500,
        )

        subject = ft.TextField(
            label="Subject",
            width=500,
        )

        topic = ft.TextField(
            label="Topic",
            width=500,
        )

        course = ft.TextField(
            label="Course",
            width=500,
        )

        description = ft.TextField(
            label="Description",
            width=500,
            multiline=True,
            min_lines=3,
            max_lines=5,
        )

        message = ft.Text("")

        def submit(e):

            if not title.value or not subject.value:
                message.value = "Please enter the required information."
                message.color = ft.Colors.RED_400
            else:
                message.value = (
                    "Resource submitted for moderation. "
                    "Approved contributions may earn Learn Points."
                )
                message.color = ft.Colors.GREEN_700

            page.update()

        return ft.Column(
            controls=[
                top_bar("Upload Note"),

                ft.Container(height=20),

                section_title(
                    "Upload Learning Resource",
                    "Submit academic material for review.",
                ),

                ft.Container(height=15),

                title,
                subject,
                topic,
                course,
                description,

                ft.ElevatedButton(
                    "Choose File",
                    icon=ft.Icons.UPLOAD_FILE,
                    width=500,
                ),

                ft.ElevatedButton(
                    "Submit for Review",
                    icon=ft.Icons.SEND,
                    width=500,
                    on_click=submit,
                    style=ft.ButtonStyle(
                        bgcolor=BLUE,
                        color=ft.Colors.WHITE,
                    ),
                ),

                message,
            ],
            spacing=12,
        )

    def my_notes():

        return ft.Column(
            controls=[
                top_bar("My Notes"),

                ft.Container(height=20),

                section_title(
                    "My Learning Resources",
                    "Manage your submitted academic materials.",
                ),

                ft.Container(height=15),

                note_card(
                    "Python Programming Reviewer",
                    "Programming",
                    "Python Basics",
                    "BSCS",
                    "1st Year",
                    status="Approved",
                    points=10,
                ),

                note_card(
                    "Data Structures Notes",
                    "Data Structures",
                    "Linked Lists",
                    "BSCS",
                    "1st Year",
                    status="Pending",
                    points=15,
                ),

                note_card(
                    "Database Reviewer",
                    "Database",
                    "SQL",
                    "BSCS",
                    "2nd Year",
                    status="Approved",
                    points=15,
                ),
            ],
            spacing=12,
        )

    def saved_notes():

        return ft.Column(
            controls=[
                top_bar("Saved Notes"),

                ft.Container(height=20),

                section_title(
                    "Saved Learning Resources",
                    "Resources you saved for later study.",
                ),

                ft.Container(height=15),

                note_card(
                    "Computer Networks Reviewer",
                    "Networking",
                    "Network Fundamentals",
                    "BSCS",
                    "2nd Year",
                    points=20,
                ),

                note_card(
                    "Database Management Notes",
                    "Database",
                    "SQL Fundamentals",
                    "BSCS",
                    "2nd Year",
                    points=15,
                ),
            ],
            spacing=12,
        )

    def learn_points():

        return ft.Column(
            controls=[
                top_bar("Learn Points"),

                ft.Container(height=20),

                ft.Container(
                    padding=25,
                    bgcolor="#FFF8D8",
                    border_radius=15,
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.STARS,
                                color="#C79500",
                                size=45,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        "150 Learn Points",
                                        size=25,
                                        weight=ft.FontWeight.BOLD,
                                        color="#9A7300",
                                    ),
                                    ft.Text(
                                        "Earn points by contributing valuable academic resources.",
                                        size=13,
                                        color="#806A2B",
                                    ),
                                ],
                            ),
                        ],
                        spacing=15,
                    ),
                ),

                ft.Container(height=25),

                section_title(
                    "Contribution History",
                    "Your recent Learn Points activity.",
                ),

                ft.Container(height=12),

                ft.ListTile(
                    leading=ft.Icon(
                        ft.Icons.ADD_CIRCLE_OUTLINE,
                        color=ft.Colors.GREEN_600,
                    ),
                    title=ft.Text(
                        "Python Programming Reviewer"
                    ),
                    subtitle=ft.Text(
                        "Approved contribution"
                    ),
                    trailing=ft.Text(
                        "+10",
                        color=ft.Colors.GREEN_700,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),

                ft.ListTile(
                    leading=ft.Icon(
                        ft.Icons.ADD_CIRCLE_OUTLINE,
                        color=ft.Colors.GREEN_600,
                    ),
                    title=ft.Text(
                        "Database Management Notes"
                    ),
                    subtitle=ft.Text(
                        "Approved contribution"
                    ),
                    trailing=ft.Text(
                        "+15",
                        color=ft.Colors.GREEN_700,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),

                ft.Container(height=20),

                section_title(
                    "Premium Feature Redemption",
                    "Learn Points may unlock selected in-platform features.",
                ),
            ],
            spacing=5,
        )

    def ai_assistant():

        note_input = ft.TextField(
            label="Paste or type your notes here",
            multiline=True,
            min_lines=8,
            max_lines=12,
        )

        result = ft.Column()

        def analyze(e):

            result.controls.clear()

            result.controls.extend(
                [
                    ft.Text(
                        "AI Analysis",
                        size=19,
                        weight=ft.FontWeight.BOLD,
                        color=BLUE,
                    ),
                    ft.Text(
                        "Classification: Programming",
                    ),
                    ft.Text(
                        "Key Concepts: Variables, Functions, Loops, Conditions",
                    ),
                    ft.Text(
                        "Summary: The notes discuss fundamental programming concepts and their use in Python.",
                    ),
                    ft.Text(
                        "Review Questions:",
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "1. What is a variable?\n"
                        "2. What is the purpose of a function?\n"
                        "3. How are loops used in programming?"
                    ),
                ]
            )

            page.update()

        return ft.Column(
            controls=[
                top_bar("AI Note Assistant"),

                ft.Container(height=20),

                section_title(
                    "AI Note Assistant",
                    "Use AI to organize notes and prepare study materials.",
                ),

                ft.Container(height=15),

                note_input,

                ft.ElevatedButton(
                    "Analyze Notes",
                    icon=ft.Icons.AUTO_AWESOME,
                    on_click=analyze,
                    style=ft.ButtonStyle(
                        bgcolor=BLUE,
                        color=ft.Colors.WHITE,
                    ),
                ),

                ft.Container(height=20),

                result,

                ft.Container(height=20),

                ft.Text(
                    "AI-generated results are study aids and should be reviewed for accuracy.",
                    size=12,
                    color="#71808A",
                    italic=True,
                ),
            ],
            spacing=10,
        )

    def profile():

        return ft.Column(
            controls=[
                top_bar("Profile"),

                ft.Container(height=20),

                ft.Container(
                    padding=25,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=15,
                    border=ft.Border.all(1, "#E1E7ED"),
                    content=ft.Column(
                        controls=[
                            ft.CircleAvatar(
                                radius=40,
                                bgcolor=BLUE,
                                content=ft.Text(
                                    "S",
                                    size=25,
                                    color=ft.Colors.WHITE,
                                ),
                            ),
                            ft.Text(
                                "Student User",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                "student@cspc.edu.ph",
                                color="#71808A",
                            ),
                            ft.Divider(),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.SCHOOL),
                                title=ft.Text("Course"),
                                subtitle=ft.Text("BS Computer Science"),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.NUMBERS),
                                title=ft.Text("Year Level"),
                                subtitle=ft.Text("1st Year"),
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
            ],
            spacing=10,
        )

    render_page()

    return ft.Row(
        controls=[
            sidebar(
                change_page,
                logout,
                admin=False,
            ),

            ft.Container(
                expand=True,
                padding=30,
                content=main_area,
            ),
        ],
        expand=True,
    )