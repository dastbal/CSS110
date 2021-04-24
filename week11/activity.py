with open('hr_system.txt') as info_list:
    for parts in info_list:
        parts = parts.strip()
        parts = parts.split(' ')

        names = parts[0]
        id_num = parts[1]
        job_title = parts[2]
        salary = float(parts[3])

        # Calculate paycheck per pay period
        paycheck = salary / 24

        # Bonus if Engineer
        if job_title.lower() == 'engineer':
            paycheck += 1000
        print(
            f'Name: {names} (ID: {id_num}) Title: {job_title} - ${paycheck:,.2f}')
