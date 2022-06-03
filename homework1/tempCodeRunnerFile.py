    #     item_list = []
    #     visit = set()
    #     for num in bgm_list:
    #         item_id = bgm_to_id[num][random.randint(0, len(bgm_to_id[num])-1)]
    #         while item_id in visit:
    #             item_id = bgm_to_id[random.randint(0, len(bgm_to_id[num])-1)]
    #             visit.add(item_id)
    #         item_list.append(DATA[item_id])
    #     status = check(item_list)
    #     if status == 4:
    #         cnt += 1
    #     if status == 1:
    #         author_fail += 1
    #     if status == 2:
    #         tag_fail += 1
    #     if status == 3:
    #         bgm_fail += 1
    # print(cnt/epoch)
    # print(1-author_fail/epoch)
    # print(1-tag_fail/epoch)
    # print(1-bgm_fail/epoch)