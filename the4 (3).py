def inheritance(example):
    a=example[::]  
    def descriptions_regulator(descriptions):
        re_descriptions = []
        child_list = []
        married_list = []
        departed_list = []
        deceased_list = []
        for i in descriptions:
            x = i.split()
            re_descriptions.append(x)
        for i in re_descriptions:
            if i[0] == "CHILD":
                child_list.append(i[1:])
            elif i[0] == "MARRIED":
                married_list.append(i[1:])
            elif i[0] == "DEPARTED":
                departed_list.append(i[1:])
            elif i[0] == "DECEASED":
                deceased_list.append(i[1:])
                if i not in departed_list:
                    departed_list.append(i[1])

        final_description = [child_list, married_list, departed_list, deceased_list]
        return final_description
    desc=descriptions_regulator(a)
    
    def remove_duplicates(lst):
        new_k = []
        for elem in lst:
            if elem not in new_k:
                new_k.append(elem)
        return new_k

    def regulator1(lst):
        lst_new = []
        for i in lst:
            for j in lst:
                if i != j and i[0] == j[0]:
                    lst_new.append(i)
                    lst_new.append(j)
        lst_new_1 = remove_duplicates(lst_new)
        lst_new_1.sort()
        lst_new_2 = []
        for i in range(0, len(lst_new_1)):
            temporary_list = []
            for j in range(0, len(lst_new_1)):
                if lst_new_1[i][0] == lst_new_1[j][0]:
                    temporary_list.append(lst_new_1[i])
                    temporary_list.append(lst_new_1[j])
            temporary_list = remove_duplicates(temporary_list)
            lst_new_2.append(temporary_list)
        for i in lst_new_2:
            i.sort()
        lst_new_2 = remove_duplicates(lst_new_2)
        lst_new_3 = []
        for i in lst_new_2:
            k_lst = []
            for j in i:
                k_lst = k_lst + j
            k_lst = remove_duplicates(k_lst)
            lst_new_3.append(k_lst)
        extra_list = lst[::]
        for i in lst_new_1:
            extra_list.remove(i)
        final_list = lst_new_3 + extra_list
        return final_list

    def bracket_remover(lst):
        if not lst:
            return []
        elif type(lst[0]) == list:
            return bracket_remover(lst[0]) + bracket_remover(lst[1:])
        return [lst[0]] + bracket_remover(lst[1:])

    def lineage_creator_regulator():
        last_lineages_list = []
        for i in lineage_creator():
            if len(i) == 1:
                last_lineages_list.append(i[0])
            else:
                element1 = i[0]
                element2 = i[1]
                last_lineages_list.append(element1)
                last_lineages_list.append(element2)
        new_lst = []
        for elem in last_lineages_list:
            if elem not in new_lst:
                new_lst.append(elem)
        last_lineages_list = new_lst

        return last_lineages_list

    def lineage_creator():
        families = desc[0]
        seperated_families = []
        revised_seperated = []
        lst_x = []
        for i in families:
            lst1 = [i[0]] + i[2:]
            lst2 = [i[1]] + i[2:]
            seperated_families.append(lst1)
            seperated_families.append(lst2)
        seperated_families = regulator1(seperated_families)
        for i in seperated_families:
            lst2 = [i[0]] + [i[1:]]
            revised_seperated.append(lst2)
        for i in range(0, len(revised_seperated)):
            current_element = revised_seperated[i]
            temporary_list = [(current_element)]
            for j in range(0, len(revised_seperated)):
                if current_element[0] in revised_seperated[j][1]:
                    temporary_list.append(revised_seperated[j])
            lst_x.append(temporary_list)
        for x_lists in lst_x:
            if len(x_lists) > 1:
                k_person = x_lists[0][0]
                index1 = x_lists[1][1].index(k_person)
                index2 = x_lists[2][1].index(k_person)
                x_lists[1][1].insert(index1 + 1, x_lists[0][1])
                x_lists[2][1].insert(index2 + 1, x_lists[0][1])
                x_lists.pop(0)
        return lst_x

    def family_tree():
        lineage_list = lineage_creator_regulator()
        BR_lineage_list = []
        indexes = []
        temp_lst = []
        for i in lineage_list:
            BR_lineage_list.append(bracket_remover(i))
        for i in range(0, len(BR_lineage_list)):
            for j in range(0, len(BR_lineage_list)):
                if (BR_lineage_list[i] != BR_lineage_list[j]) and (BR_lineage_list[i][0] in BR_lineage_list[j]) and (
                        BR_lineage_list[i][0] != BR_lineage_list[j][0]):
                    indexes.append(i)
        for i in list(set(indexes)):
            temp_lst.append(lineage_list[i])
        for i in temp_lst:
            lineage_list.remove(i)
        return lineage_list

    def PG1_finder(deceased, lst):
        if deceased == lst[0] and type(lst[1]) == list:
            return lst[1]
        if deceased != lst[0] and len(lst) == 2:
            return PG1_finder(deceased, lst[1:][0])
        if deceased != lst[0] and len(lst) > 2:
            return PG1_finder(deceased, lst[1:])
        if type(lst[0]) == list:
            return PG1_finder(deceased, lst[0])
        else:
            return []

    def PG1_regulator(pg1, RD):
        if pg1 !=[]:
            if type(pg1[0]) == str:
                if pg1[0] in RD and len(pg1) > 1:
                    pg1.pop(0)
                    return PG1_regulator(pg1, RD)
                elif pg1[0] not in RD and len(pg1) > 1 and type(pg1[1]) == list:
                    pg1.pop(1)
                    return PG1_regulator(pg1, RD)
                elif pg1[0] not in RD and len(pg1) > 1 and type(pg1[1]) != list:
                    return [pg1[0]] + PG1_regulator(pg1[1:], RD)
                elif len(pg1) == 1:
                    if pg1[0] in RD:
                        pg1.pop(0)
                        return pg1
                    elif pg1[0] not in RD:
                        return pg1
            elif type(pg1[0]) == list and len(pg1) > 1:
                return [PG1_regulator(pg1[0], RD)] + PG1_regulator(pg1[1:], RD)
            elif type(pg1[0]) == list and len(pg1) == 1:
                return [PG1_regulator(pg1[0], RD)]
        else:
            return []
    
    def stack_PG1_regulator(lst):
        e_str = ""
        a = str(lst)
        b = []
        open = "["
        close = "]"
        stack = []
        for i in a:
            b.append(i)
        for i in b:
            if i == open:
                stack.append(i)
            elif i == close and stack[-1] == open and len(stack)>1:
                stack.pop()
            elif (i != open or i != close) and i != ",":
                stack.append(i)
            elif i == close and stack[-1] != open:
                stack.append(i)
            elif i == "," and stack[-1] != open:
                stack.append(i)
            elif i == close and stack[-1] == open and len(stack)>1:
                stack.append(i)
        for i in stack:
            e_str = e_str + i

        return eval(e_str)

    def share_distrubutor(e, obj):
        if type(obj) == list and e in bracket_remover(obj):
            a = len(obj)
            if e in obj:
                return a
            elif e not in obj:
                for i in obj:
                    a = a * share_distrubutor(e, i)
                return a
        if type(obj) == str:
            return 1
        if type(obj) == list and e not in bracket_remover(obj):
            return 1
    
    def possible_inheritance():
        tree = family_tree()
        bracket_removed_tree = []
        for i in tree:
            bracket_removed_tree.append(bracket_remover(i))
        inheritance_list1 = []
        deceased = tuple(desc[-1][0])
        marriage_lst = desc[1]
        k = []
        for i in marriage_lst:
            if deceased[0] in i:
                i.remove(deceased[0])
                k = k + i
        for i in range(0, len(tree)):
            if deceased[0] in bracket_removed_tree[i]:
                inheritance_list1.append(tree[i])
        return ((inheritance_list1), deceased, k)

    def share_distrubutor_helper(amount, lst, obj):
        distrubitions = []
        for i in lst:
            distrubitions.append((i, amount / share_distrubutor(i, obj)))
        return distrubitions
    
    def parents_for_pg2(deceased):
        a=desc[0]
        parents=[]
        for i in a:
            if deceased in i[2:]:
                parents.append(i[0])
                parents.append(i[1])
        return parents
                
    def inheritance_allocator():
        def PG1():
            spouse=possible_inheritance()[2]
            possibles_list_PG1 = possible_inheritance()[0]
            deceased_info = possible_inheritance()[1]
            departeds = bracket_remover(desc[2])
            PG1 = PG1_finder(deceased_info[0], possibles_list_PG1[0])
            revised_departeds = []
            for i in departeds:
                if i in bracket_remover(PG1):
                    revised_departeds.append(i)
            PG1_revised=PG1_regulator(PG1, revised_departeds)
            PG1_revised = stack_PG1_regulator(PG1_revised)
            PG1_revised_RB = bracket_remover(PG1_revised)
            #####################################################
    
            if PG1_revised !=[]:
                if spouse ==[]:
                    return share_distrubutor_helper(float(deceased_info[1]),PG1_revised_RB,PG1_revised)
                elif spouse != [] and spouse[0] not in departeds:
                    return [(spouse[0],float(deceased_info[1])/4)]+share_distrubutor_helper((3*float(deceased_info[1]))/4,PG1_revised_RB,PG1_revised)
                elif spouse != [] and spouse[0] in departeds:
                    return share_distrubutor_helper(float(deceased_info[1]),PG1_revised_RB,PG1_revised)
            else:
                return []
        def PG2():
            spouse=possible_inheritance()[2]
            possibles_list_PG1 = possible_inheritance()[0]
            deceased_info = possible_inheritance()[1]
            departeds = bracket_remover(desc[2])
            parents=parents_for_pg2(deceased_info[0])
            ##################################################
            possibles_list_for_parent1=[]
            parent1=parents[0]
            possibles_list_for_parent2=[]
            parent2=parents[1]
            for i in possibles_list_PG1:
                if parent1 in bracket_remover(i):
                    possibles_list_for_parent1=possibles_list_for_parent1+i
                if parent2 in bracket_remover(i):
                    possibles_list_for_parent2=possibles_list_for_parent2+i
            ############ PG1 for parent1 #####################
            PG1_for_parent1 = PG1_finder(parent1, possibles_list_for_parent1)
            revised_departeds = []
            for i in departeds:
                if i in bracket_remover(PG1_for_parent1):
                    revised_departeds.append(i)
            PG1_for_parent1_revised=PG1_regulator(PG1_for_parent1, revised_departeds)
            PG1_for_parent1_revised = stack_PG1_regulator(PG1_for_parent1_revised)
            PG1_revised_RB_parent1 = bracket_remover(PG1_for_parent1_revised)
            ############ PG1 for parent2 #####################
            PG1_for_parent2 = PG1_finder(parent2, possibles_list_for_parent2)
            revised_departeds = []
            for i in departeds:
                if i in bracket_remover(PG1_for_parent2):
                    revised_departeds.append(i)
            PG1_for_parent2_revised=PG1_regulator(PG1_for_parent2, revised_departeds)
            PG1_for_parent2_revised = stack_PG1_regulator(PG1_for_parent2_revised)
            PG1_revised_RB_parent2 = bracket_remover(PG1_for_parent2_revised)
            PG1sLST=[PG1_for_parent1_revised,PG1_for_parent2_revised]
            ############ SHARING #############################
            if PG1sLST != [[],[]]:
                if spouse==[] or spouse[0] in departeds:
                    if parent1 not in departeds and parent2 not in departeds:
                        return [(parent1,float(deceased_info[1])/2),(parent2,float(deceased_info[1])/2)]
                    elif parent1 in departeds and parent2 not in departeds:
                        return share_distrubutor_helper(float(deceased_info[1])/2, PG1_revised_RB_parent1, PG1sLST[0])+[(parent2,float(deceased_info[1])/2)]
                    elif parent1 not in departeds and parent2 in departeds:
                        return share_distrubutor_helper(float(deceased_info[1])/2, PG1_revised_RB_parent2, PG1sLST[1])+[(parent1,float(deceased_info[1])/2)]
                    elif parent1 in departeds and parent2 in departeds:
                        return share_distrubutor_helper(float(deceased_info[1])/2, PG1_revised_RB_parent1, PG1sLST[0])+share_distrubutor_helper(float(deceased_info[1])/2, PG1_revised_RB_parent2, PG1sLST[1])                
                if spouse !=[] and spouse[0] not in departeds:
                    if parent1 not in departeds and parent2 not in departeds:
                        return [(parent1,float(deceased_info[1])/4),(parent2,float(deceased_info[1])/4),(spouse[0],float(deceased_info[1])/2)]
                    elif parent1 in departeds and parent2 not in departeds:
                        return share_distrubutor_helper(float(deceased_info[1])/4, PG1_revised_RB_parent1, PG1sLST[0])+[(parent2,float(deceased_info[1])/4)]+[(spouse[0],float(deceased_info[1])/2)]
                    elif parent1 not in departeds and parent2 in departeds:
                        return share_distrubutor_helper(float(deceased_info[1])/4, PG1_revised_RB_parent2, PG1sLST[1])+[(parent1,float(deceased_info[1])/4)]+[(spouse[0],float(deceased_info[1])/2)]
                    elif parent1 in departeds and parent2 in departeds:
                        return share_distrubutor_helper(float(deceased_info[1])/2, PG1_revised_RB_parent1, PG1sLST[0])+share_distrubutor_helper(float(deceased_info[1])/2, PG1_revised_RB_parent2, PG1sLST[1])                
        def PG3():
            return []
            
        if PG1() != []:
            return PG1()   
        elif PG1() ==[] and PG2 !=[]:
            return PG2()
        elif PG1() ==[] and PG2 ==[] and PG3() !=[]:
            return PG3()
        else:
            return []
    return inheritance_allocator()

