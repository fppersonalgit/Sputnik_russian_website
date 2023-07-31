from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/company")
async def get_company_info():
    quote = (
        "That's one small step for man, one giant leap for mankind.\n"
        "Neil Armstrong, the first man on the moon, 1969"
    )
    main_text = (
        "Космические ИТ-решения для бизнеса\n\n"
        "9 лет опыта    80+ проектов реализовано\n\n"
        "Расскажите экспертам Sputnik о своем бизнесе или идее продукта и мы вместе "
        "подумаем как создать лучшее решение. Это может быть одним маленьким шагом "
        "для вас и огромным скачком для вашего бизнеса."
    )

    services = [
        {
            "title": "МОБИЛЬНАЯ РАЗРАБОТКА И СОПРОВОЖДЕНИЕ",
            "icon": "url_to_mobile_icon.jpg",
            "description": "Мы разрабатываем нативные и кросс-платформенные мобильные приложения для iOS и Android. "
                           "Питаем особую слабость к нестандартным задачам, требующим таких же нестандартных подходов и алгоритмов. "
                           "С радостью применяем самый современный инструментарий – дополненную реальность, нейронные сети – для успешной "
                           "реализации проектов. Сопровождение приложений в течение всего жизненного цикла – неотъемлемая часть нашей работы. "
                           "Мы анализируем пользовательское поведение и развиваем приложение в соответствии с полученными результатами."
        },
        {
            "title": "ВЕБ-РАЗРАБОТКА",
            "icon": "url_to_web_icon.jpg",
            "description": "Чтобы расширить свое присутствие на рынке и привлечь как можно больше целевого трафика, "
                           "наши клиенты, в дополнение к мобильному, заказывают разработку и веб-приложения. Мы используем "
                           "ReactJS– один из популярнейших на сегодняшний день фреймворков – для того, чтобы создать "
                           "веб-приложение с богатым функционалом и моментальной загрузкой на любом устройстве."
        },
        # Add more service entries as needed
    ]

    content = {
        "quote": quote,
        "main_text": main_text,
        "services": services,
    }

    return JSONResponse(content=content)


@app.get("/")
async def root():
	return {"message": "Hello this is Satellite comany website! Use /company or /portfolio or /contacts "}

 
@app.get("/portfolio")
async def get_portfolio():
    portfolio = [
        {
            "title": "E-Parliament (Egoverment)",
            "description": "Выборы - это удобно и высокотехнологично\n"
                           "Спутник разработал эффективный инструмент, изменяющий подход к взаимодействию между избирателями и кандидатами. "
                           "Система, состоящая из мобильных приложений на Flutter и веб-сервиса для кандидатов и администраторов, позволяет существенно "
                           "экономить на избирательной компании, сохраняя бюджетные средства. Система внедрена в Ираке, в нее постоянно добавляются новые "
                           "функции, сейчас количество пользователей перевалило за 1.5 млн.",
            "images": [
                "url_to_image1.jpg",  # Replace with the URL to the first image
                "url_to_image2.jpg",  # Replace with the URL to the second image
                # Add more image URLs as needed
            ],
        },
        {
            "title": "BoaBee (Events)",
            "description": "Свой среди своих\n"
                           "В мире большого бизнеса каждая секунда – на вес золота. Скорость обмена информацией прямо пропорциональна вероятности заключить "
                           "сделку века. А печатные визитки, каталоги и презентации – будем честны – давно не вписываются в формат современных бизнес-ивентов. "
                           "Мобильное приложение Boabee максимально упрощает коммуникацию между потенциальными партнерами, выводя ее скорость и эффективность "
                           "на новый уровень. Отсканировать бейдж с QR-кодом и моментально получить контактные данные собеседника, сразу зафиксировать его "
                           "интересы в своей базе данных, отправить ему рекламные материалы, прайсы, любую документацию с автоматическим сохранением истории "
                           "переписки – что может быть быстрее и проще?! Пока другие только устанавливают контакт, вы с помощью Boabee уже стали лучшими друзьями "
                           "и заключаете сделку!\n"
                           "Nokia, Porsche, Volkswagen, Easyfairs оценили все преимущества Boabee и активно используют приложение на выставках, конференциях и "
                           "прочих мероприятиях. База клиентов продолжает расти.",
            "images": [
                "url_to_image3.jpg",  # Replace with the URL to the first image
                "url_to_image4.jpg",  # Replace with the URL to the second image
                # Add more image URLs as needed
            ],
        },
        # Add more portfolio cases as needed
    ]
    return portfolio

@app.get("/contacts")
def get_contacts():
    contacts =  {
        "phone": "+79231332084",
        "address": "Новосибирск, ул. Мусы Джалиля, д. 3/1, офис 1022-1023",
        "upwork": "https://www.upwork.com/your-profile-url",  # Replace with your Upwork profile URL
        "linkedin": "https://www.linkedin.com/in/your-profile-url",  # Replace with your LinkedIn profile URL
        "good_firms": "https://www.goodfirms.co/your-profile-url",  # Replace with your Good Firms profile URL
        "email": "info@wearethesatellite.com",
        "telegram": "t.me/wearesputnik",
        "intergalactic_address": "Солнечная система, планета Земля, 54°51'47.4\" с. ш. 83°05'25.8\" в. д."
    }

    return {"contacts": contacts}
