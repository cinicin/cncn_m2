import item

default_grade_need_count = [2, 2, 2, 2]
default_grade_fee = [30000, 50000, 70000, 100000]
default_step_need_count = [2, 2, 2, 2]
default_step_fee = [20000, 30000, 40000, 50000]
 
strength_fee = {
        item.MATERIAL_DS_REFINE_NORMAL : 10000,
        item.MATERIAL_DS_REFINE_BLESSED : 20000,
        item.MATERIAL_DS_REFINE_HOLLY : 30000,
}
 
# �ơ�?���Ƣ� ?i��? ��U��? ��iAo �Ƣ���E C?Ao
# table(GRADE, STEP) = max strength.
default_strength_max_table = [
        [2, 2, 3, 3, 4],
        [3, 3, 3, 4, 4],
        [4, 4, 4, 4, 4],
        [4, 4, 4, 4, 5],
        [4, 4, 4, 5, 6],
]
 
# ??��U ��a?????����I��A strength �ơ�?��?C ��???, �ơ�?��?��?�� ?CC? fee�Ƣ� ?A??��C��a �ҡ�?��?��,
# dragon_soul_refine_info?�� ��OAo ????��?.
# (�ơ�?��?�碬�� ��O?i��� ?o���� C??aC?Ao ?��?? ?o ?O��졤? C?��a ?��C?)
# ��?���� ?��?o?��?����A ?e???�� ?��?O ?�ơ�I �ơ�?��?�� fee��| ?A??C? ?o ?O��졤? C?��?��a �ҡ�?��?��,
# ����?? ?e???�� ?�ơ�I �ơ�?��?�� fee��| ��?������O C?��i ��I��?��e,
# ?����o AU��?��| ?oA��C??��C? ��I??��?.
default_refine_info = {
        "grade_need_count" : default_grade_need_count,
        "grade_fee" : default_grade_fee,
        "step_need_count" : default_step_need_count,
        "step_fee" : default_step_fee,
        "strength_max_table" : default_strength_max_table,
}
 
dragon_soul_refine_info = {
        11 : default_refine_info,
        12 : default_refine_info,
        13 : default_refine_info,
        14 : default_refine_info,
        15 : default_refine_info,
        16 : default_refine_info,
}

