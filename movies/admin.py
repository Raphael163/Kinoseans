"""импорт из models"""
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category
from .models import Actor
from .models import Genre
from .models import Movie
from .models import MovieShots
from .models import RatingStar
from .models import Rating
from .models import Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInline(admin.TabularInline):
    """Класс ReviewInline мы наследуем к MovieAdmin
    для обработки полей отзыва в фильмах
    """
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """появится категории"""
    list_display = ("title", "category", "url", "draft")

    """фильтр по нужному полю"""
    list_filter = ("category", "year")

    """поисковик"""
    search_fields = ("title", "category__name")

    """добавляем поля для обработки наследуем от ReviewInline а встроенного класса django TabularInline """
    inlines = [ReviewInline]

    """добавляем кнопку сохранить на верх"""
    save_on_top = True

    """добавляем сохранения из этого же окна с возможность оставить заполненные графы """
    save_as = True

    """Делаем чек боксы черновика сразу в списке фильмов(возможность редактирования черновика вкд выкл)"""
    list_editable = ("draft",)

    """Добавляем группы и скрытие групп <<"classes": ("collapse",),>> дает возможность сворачивать таблицы 
    в fields группируем наши поля как нам нужно 
    """
    fieldsets = (
        ("Группа - Название, Слоган", {
            "classes": ("collapse",),
            "fields": (('title', "tagline"),)
        }),
        ("Группа - Описание, Постер", {
            "classes": ("collapse",),
            "fields": (('description', "poster"),)
        }),
        ("Группа - Год, Страна", {
            "classes": ("collapse",),
            "fields": (('year', "country"),)
        }),
        ("Группа - Актеры, режиссеры, жанр, категория", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        ("Группа - Мировая примера, Бюджет", {
            "classes": ("collapse",),
            "fields": (('world_premiere', "budget"),)
        }),
        ("Группа - Сборы в США, Сборы в Мире", {
            "classes": ("collapse",),
            "fields": (('fees_in_usa', "fees_in_world"),)
        }),
        ("options - URL, DRAFT(Черновик) ", {
            "classes": ("collapse",),
            "fields": (('url', "draft"),)
        }),
    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    search_fields = ("name",)
    readonly_fields = ("name", "email",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image",)
    search_fields = ("name",)
    list_filter = ("name",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):

        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "url")
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "descriptions", "get_poster", "movie",)
    search_fields = ("title", )
    list_filter = ("title",)
    readonly_fields = ("get_poster",)

    def get_poster(self, obj):

        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_poster.short_description = "Постер"




@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("movie", "ip", "star",)


""" Регистрируем модельки """
admin.site.register(RatingStar)

