print('-'*20,'欢迎使用员工管理系统','-'*20)

while True:
    print('请选择你要做的操作')
    print('\t1,查询员工')
    print('\t2,添加员工')
    print('\t3,删除员工')
    print('\t4,退出系统')
    user_choose = input('请选择:')
    print('-'*62)
    
    if user_choose == '1' :
        print('\t序号\t姓名\t年龄\t性别\t住址')
        n = 1
        for emp in emps:
            print(f'\t{n}\t{emp}') 
            n += 1
    elif user_choose == '2' :
        emp_name1 = input('请输入姓名:')
        emp_age1 = input('请输入年龄:')
        emp_gender1 = input('请输入性别:')
        emp_address1 = input('请输入住址:')
        emp1 =f'{emp_name1}\t{emp_age1}\t{emp_gender1}\t{emp_address1}'
        print('以下员工将被添加到系统')
        print('-'*62)
        print('姓名\t年龄\t性别\t住')
        print(emp1)
        print('-'*62)

        user_confirm1 = input('是否确认该操作[Y/N]:')
        if user_confirm1 == 'y' or user_confirm1 =='yes':
            emps.append(emp1)
            
            print('添加成功')
        else:
            print('添加取消')

    elif user_choose == '3' :
        del_num = int(input('请输入要删除员工的序号'))    
        del_i = del_num - 1
        print('以下员工将从系统中删除')
        print('-'*62)
        print('\t序号\t姓名\t年龄\t性别\t住址')
        print(f'\t{del_num}\t{emps[del_i]}')
        print('-'*62)
        user_confirm = input('是否确认该操作[Y/N]:')
        if user_confirm == 'y' or user_confirm == 'yes' :
                emps.pop(del_i)
                print('删除成功')
        else:
                print('删除取消')
    elif user_choose == '4' :
        #退出
        print('欢迎使用，再见!')
        input('按下enter退出')
        break
    else :
        print('你输入有误，请重新输入')   

    print('-'*62)