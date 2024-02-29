def can_pass(attendance):
    """
    This function checks if a student can pass based on their attendance record. 
    The attendance record is a string where 'О' represents an absence and 'З' represents being late. 
    A student cannot pass if they have more than 2 absences or if they are late 3 times in a row.

    Parameters:
    attendance (str): The attendance record of the student.

    Returns:
    bool: True if the student can pass, False otherwise.
    """
     
    if attendance.count("О") > 2:
        return False

    late_counter = 0
    for char in attendance:
        if char == "З":
            late_counter += 1
            if late_counter == 3:
                return False
        else:
            late_counter = 0

    return True


print(can_pass('ППОЗЗП'))
print(can_pass('PPОЗЗЗ'))
