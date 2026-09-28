users = []
user_id_counter = 1  # 用于生成唯一的用户 ID

def show_menu():
    print("========== 用户管理系统 ==========")
    print("1. 添加用户")
    print("2. 查看所有用户")
    print("3. 查询用户")
    print("4. 修改用户")
    print("5. 删除用户")
    print("0. 退出系统")


def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def get_user_by_email(email):
    for user in users:
        if user["email"] == email:
            return user
    return None

def add_user():
    # 1. 输入姓名
    name=input("请输入姓名：").strip()    # .strip() 去掉首尾空格
    if not name:
        print("姓名不能为空")
        return
    # 2. 输入年龄
    age=int(input("请输入年龄："))
    if age <0 or age > 150:
        print("年龄必须为有效值")
        return
    # 3. 输入邮箱
    email=input("请输入邮箱：").strip()
    if not email:
        print("邮箱不能为空")
        return

    if get_user_by_email(email):
        print("该邮箱已被注册")
        return

    #定义id为用户的唯一标识符，使用len(users) + 1来生成新的用户id
    global user_id_counter
    user_id = user_id_counter

    # 4. 创建 user 字典
    user = {
        "id": user_id,
        "name": name,
        "age": age,
        "email": email
    }
    # 5. 添加到 users
    users.append(user)
    user_id_counter += 1
    print("用户添加成功")

def show_users():
    # 1. 判断 users 是否为空
    if not users:
        print("没有用户信息")
        return
    # 2. 使用 for 遍历
    for user in users:
    # 3. 打印每个用户
        print(f"id:{user['id']}, 姓名：{user['name']}, 年龄：{user['age']}, 邮箱：{user['email']}")


def query_user():
    # 1. 输入要查询的用户 ID
    user_id = int(input("请输入要查询的用户 ID："))
    # 2. 调用 get_user_by_id 函数
    user = get_user_by_id(user_id)
    if user is None:
        print("未找到该用户")
    else:
        print(f"id:{user['id']}, 姓名：{user['name']}, 年龄：{user['age']}, 邮箱：{user['email']}")

def modify_user():
    # 1. 输入要修改的用户 ID
    user_id = int(input("请输入要修改的用户 ID："))
    # 2. 调用 get_user_by_id 函数
    user = get_user_by_id(user_id)
    if user is None:
        print("未找到该用户")
        return
    # 3. 输入新的姓名、年龄、邮箱
    name = input(f"请输入新的姓名（当前：{user['name']}，直接回车保持不变）：").strip()
    if name == "":
        name = user["name"]

    age_str = input(f"请输入新的年龄（当前：{user['age']}，直接回车保持不变）：").strip()
    if age_str == "":
        age = user["age"]
    else:
        age = int(age_str)    
        if age < 0 or age > 150:
            print("年龄必须为有效值")
            return

    email = input(f"请输入新的邮箱（当前：{user['email']}，直接回车保持不变）：").strip()
    if email == "":
        email = user["email"]

    if email != user["email"] and get_user_by_email(email):
        print("该邮箱已被注册")
        return
    
    # 4. 修改用户信息
    user["name"] = name
    user["age"] = age
    user["email"] = email
    print("用户信息已修改")
    return

def delete_user():
    # 1. 输入要删除的用户 ID
    user_id = int(input("请输入要删除的用户 ID："))
    # 2. 调用 get_user_by_id 函数
    user = get_user_by_id(user_id)
    #异常情况先返回思想（帮助判断）
    if user is None:
        print("未找到该用户")
        return
    # 3. 从 users 中删除该用户
    users.remove(user)
    print("用户已删除")

show_menu()

while True:

    try:
        choice = int(input("请选择操作："))
        if choice == 1:
            add_user()
        elif choice == 2:
            show_users()
        elif choice == 3:
            query_user()
        elif choice == 4:
            modify_user()
        elif choice == 5:
            delete_user()
        elif choice == 0:
            print("系统已退出")
            break
        else:
            print("输入错误，请重新输入")
    #尽量捕获你预期会发生的具体异常，而不是无脑捕获所有 Exception。 
    except ValueError:
        print("输入错误，请输入有效的数字")