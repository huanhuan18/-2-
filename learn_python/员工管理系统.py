# 搭建业务框架

employee = {}

def show_menu():
    """显示系统菜单"""

    print('*' * 20 + '员工管理系统菜单' + '*' * 20)
    print('1. 添加员工信息')
    print('2. 删除员工信息')
    print('3. 修改员工信息')
    print('4. 显示员工信息')
    print('5. 退出管理系统')
    print('*' * 48)

def add_new_employee():
    """添加员工信息"""

    # 1.员工编号、员工姓名、性别、薪资
    employee_id = input('请输入员工的编号：')
    # 1.1 判断员工编号是否存在，如果存在拒绝添加，并提示员工重复，添加失败！
    all_employee_id = list(employee.keys())
    if employee_id in all_employee_id:
        print('员工编号重复，添加失败！')
        return
    # 1.2 如果不重复则进行下面的操作
    employee_name = input('请输入员工姓名：')
    employee_gender = input('请输入员工性别：')
    employee_salary = input('请输入员工工资：')
    # 2.将员工信息保存在字典中
    # 2.1编号作为键，剩下信息作为值
    employee_info = {'name': employee_name, 'gender': employee_gender, 'salary': employee_salary}
    # 2.2 1001:{'name': xxx, 'age': xxx, 'salary' xxx}
    employee[employee_id] = employee_info
    print('员工编号为 %s 的员工信息添加成功' % employee_id)

def remove_employee():
    """删除员工信息"""

    # 1.获得要删除的员工编号
    employee_id = input('请输入您要删除的员工的编号：')
    all_employee_id = list(employee.keys())
    if employee_id not in all_employee_id:
        print('员工编号不存在，删除失败！')
        return
    # 1.1如果员工编号不存在的话，提示错误信息，终止函数执行
    del employee[employee_id]
    print('员工编号为 %s 的员工信息删除' % employee_id)
    # 1.2如果编号存在，则删除对应编号的员工信息

def edit_employee():
    """修改员工信息"""
    # 1.拿到要修改员工的编号
    employee_id = input('请输入要修改的员工的编号：')
    # 1.1如果不存在，则提示错误信息，并且终止函数执行
    all_employee_id = list(employee.keys())
    if employee_id in all_employee_id:
        print('员工编号重复，修改失败！')
        return
    # 1.2如果存在，则修改对应信息
    # 1.2.1显示原来的信息，然后再修改
    new_employee_name = input('您的姓名是：%s,您要修改为：' % employee[employee_id]['name'])
    new_employee_salary = input('您的工资是：%s,您要修改为：' % employee[employee_id]['salary'])
    new_employee_gender = input('您的性别是：%s,您要修改为：' % employee[employee_id]['gender'])
    # 如果用户直接回车，表示没有任何输入，则不更新
    if new_employee_name != '':
        employee[employee_id]['name'] = new_employee_name

    if new_employee_gender != '':
        employee[employee_id]['gender'] = new_employee_gender

    if new_employee_salary != '':
        employee[employee_id]['salary'] = new_employee_salary

    print('员工编号为：%s 的员工信息修改成功！' % employee_id)

def show_employee():
    """显示员工信息"""

    for employeeid in employee.items():
        print('%s\t\t%s\t\t%s\t\t%s' % (employeeid[0], employeeid[1]['name'], employeeid[2]['gender'], employeeid[3]['salary'])

while True:
    # 1.显示系统菜单
    show_menu()
    # 2.获得用户输入的菜单
    my_operate = input('请输入你的操作：')
    # 3.根据用户输入来判断做什么事情
    if my_operate == '1':
        add_new_employee()
        print(employee)
    elif my_operate == '2':
        remove_employee()
    elif my_operate == '3':
        edit_employee()
    elif my_operate == '4':
        show_employee()
    elif my_operate == '5':
        print('退出系统！')
        break
    else:
        print('您的输入有误！')