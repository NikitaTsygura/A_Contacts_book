from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactsForms

# ////////////////////
# def index(request):
#     return render(request, 'index.html')  # Рендерит твой index.html
#
# def contact_list(request):
#     contacts = Contact.objects.all()
#     return render(request, 'contact_list.html', {'contact': contacts})
# ///////////


# def add_contactt(request):
#     if request.method == "Post":
#         form = ContactsForms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('contact_list')
#
#     else:
#         form = ContactsForms()
#         return render(request, 'contact_form.html', {'form': form})

# ////////////////
# def new_contact(request):
#     if request.method == "POST":
#         first_name = request.POST["name"]
#         last_name = request.POST["last_name"]
#         phone_number = request.POST["phone"]
#         email = request.POST["email"]
#
#         # Сохраняем новый контакт
#         contact = Contact(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)
#         contact.save()
#
#         # Редирект на главную страницу после сохранения
#         return redirect('home')  # Или 'base', если используешь base
#
#     return render(request, 'new_contact.html')
#
# def base(request):
#     return render(request, 'base.html')
# ///////////////


# def add_contact(request):
#     if request.method == "POST":
#         # Получаем данные из формы
#         first_name = request.POST.get('name')
#         last_name = request.POST.get('last_name')
#         phone_number = request.POST.get('phone')
#         email = request.POST.get('email')
#
#         # Проверяем, что все данные получены
#         if not first_name or not last_name or not phone_number or not email:
#             # Если чего-то не хватает, возвращаем ошибку
#             return render(request, 'new_contact.html', {'error': 'All fields are required!'})
#
#         # Создаем новый контакт
#         contact = Contact(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)
#         contact.save()  # Сохраняем контакт в базу данных
#
#         # Редиректим на главную страницу после сохранения
#         return redirect('home')  # Или 'base', если ты используешь base
#
#     return render(request, 'new_contact.html')  # Если метод GET, показываем форму


def add_contact(request):
    if request.method == "POST":
        # Получаем данные из формы
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # phone_number = request.POST.get('phone_number')
        # email = request.POST.get('email')

    #     # Создаем новый контакт и сохраняем в базу
    #     contact = Contact(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)
    #     contact.save()
    #
    #     # Редирект на список контактов после добавления
    #     return render(request, 'contact_list.html', {'contacts': Contact.objects.all()})
    #
    # return render(request, 'contact_form.html')  # Если GET-запрос, показываем форму для добавления
        form = ContactsForm(request.POST, request.FILES)  # Створюємо форму

        if form.is_valid():  # Перевіряємо, чи форма заповнена коректно
            form.save()  # Зберігаємо новий контакт у базу даних
            return redirect('contact_list')  # Перенаправляємо користувача на

    else:  # Якщо запит не POST (користувач просто відкрив сторінку)
        form = ContactsForm()  # Створюємо порожню форму
        return render(request, 'contact_form.html', {'form': form})  #



def contact_list(request):
    # Получаем все контакты из базы данных
    contacts = Contact.objects.all()

    return render(request, 'contact_list.html', {'contacts': contacts})  # Пере