from database import Base,engine,Session
from models import User,Post


Base.metadata.create_all(engine)

def register():
    username = input("username: ").lower()

    with Session() as session:
        result = session.query(User).filter(User.username == username).first()

        if result:
            print("bu username tanlangan")
            return
        
        user = User(username=username)
        session.add(user)
        session.commit()

        print('Siz muvaffaqaiyali royxatdan otdiz')


def login():
    username = input("username: ").lower()

    with Session() as session:
        user = session.query(User).filter(User.username == username).first()

        if user:
            print("siz kirdiz sayitga")
            return user
        
        print("user topilmadi")

def create_post(user:User):
    title = input("title: ").strip()
    content = input("Content: ").strip()

    with Session() as session:
        user = session.query(User).filter(User.username == user.username).first()
        post = Post(title=title,content=content)

        user.posts.append(post)
        session.add(user)
        session.commit()

        print("post qoshildi ")

def show_posts(user:User):

    with Session() as session:
        user = session.query(User).filter(User.username == user.username).first()

        print("Mening postlrim")
        posts = user.posts
        for post in posts:
            print(post.title)

def main():
    print('menu\n' \
    '1. regsiter\n' \
    '2. login\n' \
    '3. chiqish\n')

    choice = input("> ")

    if choice == '1':
        register()
    elif choice == '2':
        user = login()

        if user:
            print('\nmenu\n' \
            '1. post yozish\n' \
            '2. postlarim\n' \
            '3. chiqish\n')

            option = input("> ")

            if option == '1':
                create_post(user)
            elif option == '2':
                show_posts(user)

main()


