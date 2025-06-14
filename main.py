from flet import *

def main(page:Page):
    BG = "#041955"
    FWG = "#097b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    create_task_view = Container(
        content=Container(height=40,width=40,content=Text("X"),on_click=lambda _: page.go("/"))
    )

    tasks = Column(
        height=300,
        scroll="auto",

    )
    for i in range(10):
        tasks.controls.append(
            Container(height=70, width=400,bgcolor=BG,border_radius=25)
        )

    CategoryCard = Row(
        scroll="auto"
    )
    categories = ["Business", "Family", "Friends"]
    for category in categories:
        CategoryCard.controls.append(
            Container(
                bgcolor=BG,height=110,width=170,padding=15,border_radius=20,
                content=Column(
                    controls=[
                        Text("40 Tasks"),
                        Text(category),
                        Container(
                            width=160,
                            height = 5,
                            bgcolor = "white12",
                            padding=padding.only(right=50),
                            content=Container(
                                bgcolor=PINK
                            )
                        )
                    ]
                )
            )
        )
    first_page_contents = Container(
        content = Column(
            controls=[
                Row(alignment="spaceBetween",
                    controls=[
                        Container(content=Icon(icons.MENU)),
                        Row(
                            controls=[
                                Icon(Icons.SEARCH),
                                Icon(Icons.NOTIFICATIONS_ACTIVE_OUTLINED)
                            ]
                        )
                    ]
                ),
                Container(height=20),
                Text(
                    value="Whats\'s up, Olivia!"
                ),
                Text(
                    value="Categories"
                ),
                Container(
                    padding=padding.only(top=10,bottom=20),
                    content=CategoryCard
                ),
                Text("Today's Task"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(icon=icons.ADD,bottom=2,right=20,on_click=lambda _: page.go("/create_task"))
                    ]
                )
            ]
        )
    )

    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=750,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(top=50,left=20,right=20,bottom=5),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )


    container = Container(
        width=400,height=750,bgcolor=BG,border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )
    pages = {
        "/":View(
            "/",
            [
                container
            ],
        ),
        "/create_task":View(
            "/create_task",
            [
                create_task_view
            ]
        )
    }
    page.add(container)

    page.on_route_change = route_change
    page.go(page.route)


app(target=main)
